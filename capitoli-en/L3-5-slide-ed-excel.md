# Chapter L3.5 — Slides and Excel

> Level 3 — Daily work.
> Product details verified on 22/06/2026 against official sources.

## Goal

By the end you'll know how to build a presentation with a three-step method
(structure, content, style), set up a spreadsheet moving from data to formulas
to charts, and understand when the add-in inside Office is worth it instead of
generating in chat.

## Prerequisites

- Having read how to ask for documents (ch. L3.4).
- Code execution / file creation active (see ch. L1.3). (VOLATILE)

## Slides: structure, then content, then style (EVERGREEN)

A presentation built all in one shot almost always comes out muddled. The method
that works has three steps, and follows the same "content first" principle as
the previous chapter:

1. **Structure.** Decide the slide sequence first: how many, with which title, in
   what order. It's the backbone of the talk. Have it reviewed until the thread
   holds.
2. **Content.** Fill each slide: few points per slide, one idea per slide. Here
   what matters is what you say, not how it looks.
3. **Style.** Only at the end, the appearance: theme, colors, visual
   consistency.

Reversing the order is costly: polishing the style of slides you'll later rewrite
is wasted work. An example of a first move:

```text
Prepare the OUTLINE of an 8-slide presentation
on project X for management: titles only, plus
one line of content per slide.
```

Once the outline holds, you move to the content slide by slide, and only at the
end do you ask for the `.pptx` with the theme.

## Excel: data, then formulas, then charts (EVERGREEN)

For spreadsheets the right order is just as clear:

1. **Data.** First clean, well-structured data: columns with clear headers, one
   row per record. Everything else rests on this.
2. **Formulas.** Then the calculations: totals, percentages, aggregations. On
   well-structured data the formulas come out simple and correct.
3. **Charts.** Finally the visualization, built on the data and calculations
   already in place.

If the data is messy, formulas and charts will inherit the mess. It's worth
spending the first step tidying up the columns.

> **Tip:** ask Claude to **explain the formulas** it adds. A sheet you don't
> understand is a sheet you can't trust: having them commented gives you a check.

Table L3.5.1 — The right order, at a glance.

| Output | First | Last |
|---|---|---|
| Slides | Structure | Style |
| Excel | Data | Charts |

## The add-in inside Office (VOLATILE)

Beyond generating files in chat, Claude lives **inside** Office as an add-in for
**Excel, Word and PowerPoint** (Claude for Microsoft 365). It's in beta
(research preview) for the **Max, Team and Enterprise** plans. (VOLATILE)

The practical difference is where you work:

- **In chat:** Claude **creates** the file from scratch. Handy when you start
  from nothing or produce many similar documents.
- **In the add-in:** Claude works **on the open document** in Office. Handy when
  the file already exists, is large, or you want to stay in the tool where you'll
  then refine it by hand.

Quick rule: if the document is being created now, chat is just fine; if you're
editing something already in Excel or PowerPoint, the add-in saves you the
back-and-forth between apps.

## In practice: a presentation in three steps

1. Ask for the **outline** (titles only + one line). Adjust it.
2. For each slide, ask for the **content**: few points, one per idea.
3. Ask for the **.pptx** with a consistent theme:

   ```text
   Generate the .pptx from the approved outline:
   restrained theme, one accent color, consistent titles.
   ```

4. Open the file. For touch-ups, targeted edits (ch. L3.4) or, if you have it,
   the PowerPoint add-in.

## Common mistakes

- **Starting from style.** Theme and colors come last. First structure and
  content.
- **Too much per slide.** One idea per slide. Walls of text don't present.
- **Dirty data in Excel.** Formulas and charts inherit the mess: tidy the
  columns first.
- **Trusting formulas you don't understand.** Have them explained: it's your
  check.
- **Looking for the add-in on the wrong plan.** It's beta on
  Max/Team/Enterprise. (VOLATILE)

## Summary

1. Slides in three steps: **structure → content → style**. Style last.
2. Excel in three steps: **data → formulas → charts**. Clean data first of all.
3. Have the formulas explained: a sheet you don't understand isn't reliable.
4. In chat Claude **creates** the files; in the add-in it works **on the open
   document** in Office.
5. The M365 add-in is beta on Max/Team/Enterprise. (VOLATILE)

## Next step

With daily work wrapped up, **Level 4 — Design** opens the canvas: generating
and iterating on interfaces, starting from your own brand and bringing the
result into Claude Code. We begin with **ch. L4.1 — Design: the canvas**.

---

*Data on the Microsoft 365 add-in (products, beta, plans) from the ledger,
verified on 22/06/2026 on claude.com and support.claude.com. The examples were
not executed here.*
