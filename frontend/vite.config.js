import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import { VitePWA } from "vite-plugin-pwa"

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    vueDevTools(),
    VitePWA({
      registerType: 'autoUpdate',
      manifest: {
        name: 'Muscle Maker',
        short_name: 'Muscle Maker',
        description: 'A Progressive Web App for generating workout programs',
        theme_color: '#2563eb',
        background_color: "#ffffff",
        display: "standalone",
        start_url: "/",
        icons: [
          {
            src: 'benchIllustration.png',
            sizes: '192x192',
            type: 'image/png'
          },
          {
            src: 'dumbellIllustration.png',
            sizes: '512x512',
            type: 'image/png'
          }
        ]
      }
    })
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})
