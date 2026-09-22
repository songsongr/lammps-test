"""Playwright headless 截图脚本: 仪表盘 + 任务详情 + 任务列表
捕获每个页面的 console.error 列表, 用于 v1.8.4 布局升级视觉/console 验证。"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE = "http://127.0.0.1:8911"
OUT = Path(r"C:\Users\23653\Desktop\cc-proj\lammps-test")
errors: dict[str, list[str]] = {}


def cap(page, name: str) -> None:
    errors.setdefault(name, [])
    page.on("console", lambda msg, n=name: msg.type == "error" and errors[n].append(msg.text))
    page.on("pageerror", lambda exc, n=name: errors[n].append(f"pageerror: {exc}"))


def wait_rendered(page, sel: str, timeout: int = 4000) -> None:
    try:
        page.wait_for_selector(sel, timeout=timeout)
    except Exception:
        pass


def main() -> int:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        ctx = browser.new_context(viewport={"width": 1440, "height": 900})
        page = ctx.new_page()
        cap(page, "dashboard")

        # 1) 仪表盘
        page.goto(f"{BASE}/", wait_until="networkidle")
        wait_rendered(page, ".kpi-bar")
        wait_rendered(page, ".card")
        page.wait_for_timeout(1200)  # 让 Recharts 渲染
        page.screenshot(path=str(OUT / "verify-v185-dashboard.png"), full_page=True)

        # 2) 任务列表 (创建一个 dummy job 来确保有数据可见; 没有 job 也行)
        page.click("text=任务记录")
        page.wait_for_timeout(800)
        cap(page, "jobs")
        wait_rendered(page, ".filter-chip")
        page.screenshot(path=str(OUT / "verify-v185-jobs.png"), full_page=True)

        # 3) 任务详情 — 如果列表为空直接跳空态, 否则点第一个任务
        page.evaluate("""() => {
          const r = document.querySelectorAll('.row-table tbody tr');
          if (r.length > 0) r[0].click();
        }""")
        page.wait_for_timeout(1500)
        wait_rendered(page, ".sticky-status")
        # 滚到顶部
        page.evaluate("window.scrollTo(0, 0)")
        page.wait_for_timeout(500)
        page.screenshot(path=str(OUT / "verify-v185-detail.png"), full_page=True)

        browser.close()

    print("=== console.error / pageerror per page ===")
    for name, msgs in errors.items():
        print(f"[{name}] {len(msgs)} errors:")
        for m in msgs[:20]:
            print(f"  - {m[:200]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())