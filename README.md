# KnoxDevs Website

Source for [knoxdevs.com](https://knoxdevs.com) — built with [Astro](https://astro.build) and [Tailwind CSS](https://tailwindcss.com). Deployed automatically to GitHub Pages on every push to `master`.

## Development

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # build to dist/
```

## Contributing

### Adding or updating a group, organizer, conference, organization, or space

1. Edit (or create) the relevant YAML file in `src/content/{collection}/`
2. If adding a new entry with a logo/photo, drop the image in `public/images/{collection}/` and add `image: yourfilename.ext` to the YAML
3. Open a pull request

### Collections

| Folder | What it contains |
|---|---|
| `src/content/groups/` | Developer meetup groups |
| `src/content/organizers/` | Community organizers |
| `src/content/conferences/` | Regional conferences |
| `src/content/organizations/` | Supporting organizations |
| `src/content/spaces/` | Coworking and event spaces |

Images live in the matching `public/images/{collection}/` directory.

## Have an issue or request?

[Open an issue](https://github.com/KnoxDevs/knoxdevs.github.io/issues).
