# Chapter L4.2 — Design system import

> Level 4 — Design.
> Product details verified on 24/06/2026 against official sources.

## Goal

By the end you'll know why to make Claude Design start from your brand instead of
from scratch, which sources to import a design system from, what Claude extracts
from it, and how to avoid the anonymous, generic output — the so-called "AI
slop".

## Prerequisites

- Having used the canvas (ch. L4.1).
- Having at least one source of your brand: a codebase, a deck, or graphic
  assets.

## Why import the brand (EVERGREEN)

Without a design system, Claude generates with a default style: correct but
neutral, recognizable as "made by AI". It's the problem of **AI slop**:
plausible results with no identity, all looking the same. The cure is to give
Claude your brand as a foundation, so every screen starts with your colors,
fonts and components instead of the defaults.

Importing a design system is the step that turns Design from a generator of
generic drafts into a tool that produces material that's already "yours".

## What Claude extracts and from where (VOLATILE)

Claude analyzes the sources you give it and extracts a **reusable design
system**:

- **Color palette:** primary, secondary and accent colors.
- **Typography:** font families, sizes, weights.
- **Components:** buttons, cards, navigation elements and other patterns.
- **Layout:** spacing, grids, page structures.

The possible sources are more than one, and just one is enough to start from:

Table L4.2.1 — Sources to import from and what they give.

| Source | What it contains | Result |
|---|---|---|
| Codebase | real components | the most faithful |
| Deck / PDF | colors, layout | good for the look |
| Brand assets | logo, palette | minimal base |

A **codebase** (for example a React component library) is the richest source:
Claude reads the real components and reuses them. A well-made **deck** or PDF is
enough to extract colors and layout. Even just a logo and a palette give a
starting point. The more sources you provide, the more Claude has to work from.

## How to set it up (VOLATILE)

Configuring the design system is an operation for a **brand owner or designer**,
to be done **once**: afterwards, the team's projects inherit it automatically
(Team/Enterprise). The steps, in brief:

1. In Claude Design, select or create your **organization**.
2. Upload the brand **assets** (codebase, deck, graphic assets).
3. Claude generates a **UI kit**: review it by creating a test project.
4. When you're satisfied, turn on the **"Published" toggle**: from then on, the
   org's new projects use your design system.

> **Note:** in teams, the **Claude Design Admin** role lets you approve a
> standard design system and lock down changes, so the output always stays
> within the company guidelines. (VOLATILE)

## Importing from Claude Code (VOLATILE)

If your design system lives in code, you can import it **from the terminal** with
Claude Code's `/design-sync` command: it brings the local codebase's design
system into Design, so every screen starts from your real components. It's the
bridge between code and canvas, which we go deeper into in ch. L4.3.

## Reducing AI slop (EVERGREEN)

The import is worth only as much as its source: a messy codebase or an
incomplete file shows in the output. A few moves raise the quality:

- **Give real examples, not just specs.** A finished landing page says more than
  an isolated color palette: it conveys the "feel" of the brand.
- **Iterate on the extraction.** If the first result doesn't capture the brand,
  upload different or additional assets.
- **Name the components in the prompt.** "Use the Primary Button component" or
  "Apply the Card pattern" guides Claude toward your system instead of toward a
  default.

## In practice: bring in your brand

1. Gather the best source you have: ideally the codebase, otherwise a curated
   deck.
2. Create/select the organization in Claude Design and upload the assets.
3. Review the generated UI kit with a test project ("Create a landing page for
   our product").
4. If it doesn't capture the brand, add assets and iterate.
5. Turn on **Published** and check that new projects use your style.

## Common mistakes

- **Starting without a design system.** You get AI slop: anonymous style. Import
  the brand first.
- **Messy source.** A confused codebase or incomplete file is reflected in the
  output: clean the source or pick a better one.
- **Only specs, no examples.** A palette alone says little: add a real page.
- **Not naming the components.** If you know a component exists, call it by name
  in the prompt.

## Summary

1. Without a design system the output is anonymous (**AI slop**); importing the
   brand is the cure.
2. Claude extracts **colors, typography, components and layout** from the
   sources.
3. The most faithful source is a **codebase**; decks and assets give a base.
4. The setup is for a brand owner, **once**: the team inherits the system.
5. The import is worth as much as the source: give real examples and iterate to
   reduce AI slop.

## Next step

In **ch. L4.3 — From Design to code** we walk the complete bridge: the
`/design-sync` command in both directions and the handoff to Claude Code that
builds real software starting from the canvas.

---

*Data on the design system import (sources, extraction, setup, admin role)
verified on 24/06/2026 on support.claude.com/en/articles/14604397. The setup
requires a paid account and was not executed here.*
