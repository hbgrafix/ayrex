# AYREX Network — Extracted Style Guide

Source: `index.html`. This guide documents the existing CSS; it does not introduce a redesign.

## Design direction
- Dark, research-oriented visual identity.
- Deep green surfaces, warm gold accents, and muted mint highlights.
- Fine low-contrast borders, restrained gradients, rounded cards, and pill-shaped buttons.
- Abstract orbital/network imagery and thin-line SVG icons.
- Responsive, framework-free CSS.

## Design tokens

| Token | Value | Intended use |
|---|---|---|
| `--bg` | `#06100e` | Main page background |
| `--bg2` | `#091713` | Secondary background |
| `--panel` | `#0c1c17` | Panel surface |
| `--line` | `rgba(205,225,211,.13)` | Borders and dividers |
| `--text` | `#f0f5f0` | Primary text |
| `--muted` | `#a8b8ae` | Supporting text |
| `--gold` | `#d8ae5b` | Primary accent, buttons, icons |
| `--mint` | `#8dc9a2` | Highlighted text and secondary accent |
| `--max` | `1180px` | Main content max width |

Additional colors in component rules include `#e7c578` (button hover), `#d5e0d8` (hero lead), `#c3d0c8` (navigation), and `#08130f` (insights section).

## Typography
- Font stack: `Inter`, system UI, Apple system fonts, BlinkMacSystemFont, Segoe UI, sans-serif.
- Body line-height: `1.6`.
- Eyebrows: uppercase, `0.7rem`, weight `750`, letter spacing `.19em`, gold.
- Brand name: `1.25rem`, weight `350`, letter spacing `.22em`.
- Brand subtitle: `.53rem`, letter spacing `.53em`.
- Hero heading: responsive `clamp(3rem, 6vw, 5.3rem)`, weight `450`, line-height `1.02`, letter spacing `-.055em`.
- Section headings: responsive, weight `450`, tight line-height and negative letter spacing.
- Body/supporting text uses muted colors and smaller sizes for secondary hierarchy.

## Layout and spacing
- Content wrapper: `min(1180px, calc(100% - 48px))`; on small screens uses `calc(100% - 32px)`.
- Sticky header: `78px` desktop, `68px` mobile; translucent background with `18px` backdrop blur.
- Hero: minimum height `570px`, padding `90px 0 82px`.
- Standard sections: `82px` vertical padding; mobile `60px`.
- Primary grids: two-column hero; five-column pillars; three-column cards; footer grid in three columns.
- Card and pillar grids collapse at responsive breakpoints.

## Components
- Buttons: inline-flex, pill-shaped (`999px` radius), gold fill for primary action, transparent gold outline for secondary action.
- Cards: subtle gradient surfaces, thin borders, `15px` radius, slight upward hover movement.
- Pillar container: `18px` radius, thin grid dividers.
- Inputs: dark surface, thin border, pill radius.
- Notice/toast: fixed bottom-right, dark green surface, mint-tinted border.
- Focus: visible `2px` gold outline with `4px` offset.
- Icons: inline SVG with thin strokes; gold used for key icon accents.

## Motion and interaction
- Most transitions are `0.2s`.
- Navigation links change to gold on hover.
- Buttons move upward by `2px` on hover.
- Cards move upward by `4px` and shift border toward gold on hover.
- Smooth scrolling is enabled, except when reduced motion is requested.
- `prefers-reduced-motion: reduce` disables transitions and smooth scrolling.

## Responsive breakpoints
- `max-width: 900px`: compact navigation spacing, reduced hero art, stacked initiative/insight layouts.
- `max-width: 680px`: mobile navigation menu, single-column hero, two-column pillars, single-column card content, stacked footer, reduced section spacing.

## Accessibility details present in source
- Visible keyboard focus styles.
- Mobile menu updates `aria-expanded`.
- Status/notice regions use `aria-live`.
- Reduced-motion preference is respected.

## Files
- `ayrex-style.css`: exact CSS extracted from the embedded `<style>` block in the supplied HTML.
- `ayrex-style.html`: design system for the reference as style guide.
