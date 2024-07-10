import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { config } from "dotenv";

config();

// https://vitejs.dev/config/
export default () => {
  return defineConfig({
    plugins: [react()],
    server: {
      port: parseInt(process.env.VITE_PORT || "3001"),
    },
  });
};
