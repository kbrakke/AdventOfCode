import { defineConfig } from 'astro/config';
import node from "@astrojs/node";

// https://astro.build/config
export default defineConfig({
  site: 'https://kbrakke.github.io',
  base: '/AdventOfCode/AOC-2022',
  output: "server",
  adapter: node({
    mode: 'standalone'
  }),
});