import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

// 开发模式: Vite (5173) 托管前端, /api 与 /ws 反代到后端 (8000)
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      "/api": "http://127.0.0.1:8000",
      "/ws": { target: "ws://127.0.0.1:8000", ws: true },
    },
  },
  build: { outDir: "dist" },
});
