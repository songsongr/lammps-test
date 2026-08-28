import React from "react";
import { ConfigProvider } from "antd";
import zhCN from "antd/locale/zh_CN";
import { createRoot } from "react-dom/client";
import "@fontsource-variable/inter";
import App from "./App";
import "./theme.css";

createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <ConfigProvider
      locale={zhCN}
      theme={{
        hashed: false,
        token: {
          colorPrimary: "#3547e8",
          colorInfo: "#3547e8",
          colorLink: "#3547e8",
          colorBgLayout: "#f6f6f3",
          colorBgContainer: "#ffffff",
          colorBgElevated: "#ffffff",
          colorText: "#1d1d1a",
          colorTextSecondary: "#6f6f67",
          colorTextTertiary: "#a3a39a",
          colorBorder: "rgba(29, 29, 26, 0.14)",
          colorBorderSecondary: "rgba(29, 29, 26, 0.08)",
          borderRadius: 10,
          controlHeight: 34,
          fontFamily:
            "'Inter Variable', -apple-system, 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif",
        },
        components: {
          Button: { fontWeight: 550, primaryShadow: "0 1px 3px rgba(53, 71, 232, 0.3)" },
          Checkbox: { fontSize: 12.5 },
          Modal: { borderRadiusLG: 16, titleFontSize: 15 },
          Popconfirm: {},
          Tooltip: { fontSize: 12 },
        },
      }}
    >
      <App />
    </ConfigProvider>
  </React.StrictMode>,
);
