import { defineConfig, splitVendorChunkPlugin } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react(), splitVendorChunkPlugin()],
  build: {
    sourcemap: false,
  },
  server: {
    host: "0.0.0.0",
    port: 5173,
  },
});
