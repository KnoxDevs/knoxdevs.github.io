import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';

export default defineConfig({
  site: 'https://knoxdevs.com',
  trailingSlash: 'always',
  vite: {
    plugins: [tailwindcss()],
  },
});
