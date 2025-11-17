import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// Detecta o ambiente do GitHub Codespaces para configurar o HMR (Hot Module Replacement)
const hmrConfig = process.env.CODESPACE_NAME
  ? {
      // O Codespaces expõe o servidor na porta 443 (HTTPS)
      clientPort: 443,
      // A URL pública do servidor de desenvolvimento
      host: `${process.env.CODESPACE_NAME}-5173.app.github.dev`,
      protocol: "wss", // Protocolo seguro de websocket
    }
  : true; // Usa a configuração padrão se não estiver no Codespaces

export default defineConfig({
  plugins: [react()],
  server: {
    host: "0.0.0.0",
    port: 5173,
    hmr: hmrConfig,
  },
});
