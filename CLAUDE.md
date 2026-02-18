# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is the **KnoxDevs community website** — a GitHub Pages-hosted static site for a 501(c)(3) nonprofit umbrella of tech meetups in Knoxville, TN. Built with Astro and Tailwind CSS v4.

## Development Commands

```bash
npm install             # Install dependencies
npm run dev             # Dev server at http://localhost:4321
npm run build           # Build to dist/
npm run preview         # Preview the built site locally
```

Deployment is automatic: push to `master` → GitHub Actions builds and deploys to GitHub Pages.

> **First-time GitHub Pages setup:** Go to Settings → Pages → Source and set it to **GitHub Actions** (not the legacy "Deploy from branch" option).

## Architecture

### Stack
- **Astro 5** — static site generator, file-based routing, content collections
- **Tailwind CSS v4** — utility styling via `@tailwindcss/vite` plugin (no `tailwind.config.js` needed)
- Brand color defined in `src/styles/global.css` as `--color-brand: #0180ab`

### Content Collections

All editable data lives in `src/content/` as YAML files. Schemas are defined in `src/content/config.ts`.

| Collection | Path | Purpose |
|---|---|---|
| `groups` | `src/content/groups/*.yml` | Developer meetup groups |
| `organizers` | `src/content/organizers/*.yml` | Community organizers |
| `conferences` | `src/content/conferences/*.yml` | Regional conferences |
| `organizations` | `src/content/organizations/*.yml` | Supporting orgs |
| `spaces` | `src/content/spaces/*.yml` | Coworking/event spaces |

### Adding or Updating an Entry

1. Edit (or create) the YAML file in `src/content/{collection}/`
2. If adding a new entry with an image, drop the image in `public/images/{collection}/` and add `image: yourfile.jpg` to the YAML
3. Commit and push — the site redeploys automatically

### Image Convention

Images live in `public/images/{collection}/`. Each YAML entry has an optional `image` field containing just the filename (e.g., `image: knoxpy.jpg`). Cards show a fallback initial avatar if no image is set.

### Pages

| Page | Source | Route |
|---|---|---|
| Home | `src/pages/index.astro` | `/` |
| About + Organizers + CoC | `src/pages/about.astro` | `/about/` |
| Groups | `src/pages/groups.astro` | `/groups/` |
| Resources | `src/pages/resources.astro` | `/resources/` |

### Components

- `src/layouts/Layout.astro` — base HTML shell (nav + footer)
- `src/components/Nav.astro` — sticky nav with mobile menu
- `src/components/Footer.astro` — simple dark footer
- `src/components/Card.astro` — reusable card for groups, organizers, conferences, etc.
- `src/components/SlackModal.astro` — Slack join button + CoC modal dialog
