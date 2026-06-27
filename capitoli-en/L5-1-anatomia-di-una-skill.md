# Chapter L5.1 — Anatomy of a skill

> Level 5 — Skills and identity.
> Product details verified on 24/06/2026 against official sources.

## Goal

By the end you'll know what a skill is, how it differs from a prompt, how a
`SKILL.md` file is made and why its `description` is the most important part. It's
the conceptual foundation for building one of your own in the next chapter.

## Prerequisites

- Knowing how to write effective requests (ch. L1.2).
- Having **Code execution** active (ch. L1.3): it's required for Skills.
  (VOLATILE)

## Skill or prompt? (EVERGREEN)

A prompt is good for one conversation: you write it, you get the answer, it ends
there. A **skill** is reusable knowledge that Claude loads **on its own** when the
context calls for it, without you pasting it every time. You write a rule once, and
Claude applies it every time it's needed.

The practical difference: the prompt is a throwaway instruction; the skill is a
permanent competence. If you notice yourself re-pasting the same instructions chat
after chat, that text is a candidate to become a skill.

## A folder and a file (VOLATILE)

A skill, in its minimal form, is a **folder** that contains a `SKILL.md` file. Only
that file is mandatory: it alone is enough to make a working skill. The file has
two parts:

- a **frontmatter** at the top (metadata between two `---` lines);
- a **body** in Markdown with the actual instructions.

> **Note:** by convention the file is called `SKILL.md`. The documentation also
> refers to it as `skill.md`: it's the same file. In Claude Code, project skills
> live under `.claude/skills/` (ch. L2.4). (VOLATILE)

## The frontmatter: two mandatory fields (VOLATILE)

The frontmatter declares what the skill is. Two fields are mandatory:

- **name** — the readable name, maximum **64 characters**.
- **description** — what the skill does and **when to use it**, maximum **200
  characters**.

There are optional fields (for example `dependencies` for software packages), but
name and description are enough to get started.

Here's a complete minimal skill:

```markdown
---
name: meeting-minutes
description: From raw notes, create minutes
  with decisions and action items.
---

# Meeting minutes

Turn messy notes into minutes:
1. List the decisions made.
2. Extract action items with an owner.
3. Close with the points still open.
```

## The description is everything (EVERGREEN)

Between the two fields, the `description` is the one that really counts. Claude
reads it to decide **whether** to activate the skill: with dozens or hundreds of
skills available, it's the description that triggers the right one at the right
moment. A vague description ("helps with documents") never triggers precisely; a
specific one ("from raw notes, creates minutes with decisions and action items")
does.

Here's where the mechanism of **progressive disclosure** comes in: Claude first
reads only the metadata — name and description — to understand whether the skill is
needed, and loads the full body **only if** it decides to use it. It's efficient: a
few lines are enough for it to choose, without reading everything. That's why the
description should be written with an eye to when you want the skill to activate,
not just to what it does.

## The body: instructions and examples (EVERGREEN)

Under the frontmatter, the Markdown body contains the instructions Claude follows
when the skill is active: what to do, in what order, with what constraints.
Examples help a lot — showing an input and the expected output is worth more than
an abstract explanation. If the instructions grow too long, you can move part of
them into separate resource files (for example a `REFERENCE.md`) and reference them
from `SKILL.md`.

## Common mistakes

- **Confusing skill and prompt.** The prompt is for one chat; the skill is
  reusable and activates on its own.
- **Vague description.** It's the field that triggers the skill: be specific about
  the "when".
- **Going over the limits.** A name over 64 or a description over 200 characters
  isn't valid. (VOLATILE)
- **Putting everything in the body.** If it's too much, use separate resource
  files.

## Summary

1. A skill is **reusable** knowledge that Claude loads on its own; a prompt is good
   for a single chat.
2. In its minimal form it's a **folder** with a `SKILL.md` file.
3. The frontmatter has two mandatory fields: **name** (≤64) and **description**
   (≤200). (VOLATILE)
4. The **description** decides when the skill triggers: write it with the "when" in
   mind.
5. The Markdown body contains instructions and examples; extra resources go in
   separate files.

## Next step

In **ch. L5.2 — Your first skill** we build a skill from scratch, by hand and with
the help of skill-creator, and we learn to test that it activates when it should.

---

*Data on SKILL.md, frontmatter and limits verified on 24/06/2026 on
support.claude.com/en/articles/12512198 and code.claude.com/docs/en/skills. The
SKILL.md example was not executed here.*
