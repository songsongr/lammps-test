/** 前端 VMD/VESTA 扩展名支持矩阵 (与 common/local_tools_compat.py 同源, 手动同步)。
 *  后端是真相源, 这里只供前端按扩展名筛按钮; 后端 spawn 前会再次校验。 */

const VMD_EXTS = new Set([
  ".lammpstrj", ".dump", ".dcd", ".xtc", ".trr", ".xyz", ".pdb", ".gro",
]);
const VESTA_EXTS = new Set([
  ".vesta", ".cif", ".xsf", ".xyz", ".pdb", ".cssr", ".struct", ".xod", ".xtl", ".fdf",
]);

export function supports(tool: "vmd" | "vesta", ext: string): boolean {
  const e = ext.toLowerCase();
  if (!e.startsWith(".")) return false;
  if (tool === "vmd") return VMD_EXTS.has(e);
  if (tool === "vesta") return VESTA_EXTS.has(e);
  return false;
}
