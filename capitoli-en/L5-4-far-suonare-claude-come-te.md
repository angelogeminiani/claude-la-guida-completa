# Chapter L5.4 — Making Claude sound like you

> Level 5 — Skills and identity.
> Stable concepts; product details from the ledger (verified 24/06/2026).

## Goal

By the end you'll know how to compose the identity tools — account instructions,
Styles, Projects, context files and Skills — to give Claude a stable, recognizable
voice, and you'll do a practical exercise to extract yours. It's the chapter that
closes Level 5 by lining up what you've learned.

## Prerequisites

- Settings and Styles (ch. L1.3), Projects (ch. L3.2), Skills (ch. L5.1-5.3).

## Why voice matters (EVERGREEN)

Claude, without guidance, writes in a correct but neutral register. If you use it
to produce texts that carry your name — emails, articles, documents — that
neutrality shows: it's the sign that the text isn't "yours". Giving Claude your
voice isn't an aesthetic indulgence, it's what makes the result publishable without
rewriting it.

Voice doesn't live in one single place. It's composed of several tools, each with a
different reach. Choosing them well avoids putting everything everywhere.

## The scale of tools (EVERGREEN)

From the lightest to the most structured, here's where identity lives and what it
governs.

Table L5.4.1 — The identity tools, from light to structured.

| Tool | Reach | For what |
|---|---|---|
| Instructions | every chat | stable preferences |
| Styles | as needed | how to communicate |
| Projects | a topic/client | isolated context |
| Skills | wherever needed | repeatable rules |

- **Instructions for Claude** (ch. L1.3): personal preferences valid in every chat
  — name, language, base tone. The most convenient level for what always holds.
- **Styles** (ch. L1.3): they govern *how* Claude communicates; you activate them
  when needed, and a custom style can learn from your text.
- **Projects** (ch. L3.2): they isolate context and instructions for a topic or a
  client, without polluting the other chats.
- **Skills** (ch. L5.1-5.3): they package repeatable rules that trigger on their
  own, in chat, Cowork and Code.

## Context files (EVERGREEN)

There's a level that precedes all the others: the **context files**. They are
documents where you gather the raw material of your voice — examples of your texts,
a list of words to avoid, "before/after" pairs. They aren't a product in
themselves: they're the raw material from which a custom Style, a Project's
instructions or a voice skill are then born.

This book works that way: a context file gathers examples and style rules, and from
there it feeds the `voce` skill and the Project's instructions. Writing the context
first avoids scattering the voice across many small, disconnected instructions.

## Compose them, don't pile them up (EVERGREEN)

The mistake is putting the same rule in all the tools. Better to assign each one its
reach: the always-valid preferences in the Instructions; the "how to write" in the
Styles or in a `voce` skill; a client's material in a Project. A rule lives in one
place only — the right one — so that, when it changes, you update it once.

## Exercise: extract your voice (EVERGREEN)

A concrete path for giving Claude your voice:

1. **Gather** 3-5 real texts of yours (emails, articles, notes). They're the most
   precious material.
2. **Have the traits extracted:** ask Claude "From these texts of mine, describe my
   register, the recurring words and the ones I avoid".
3. **Write the context file:** save those traits, with examples and a list of words
   to avoid.
4. **Choose the container:** for general use, a **custom Style**; for recurring
   work, a **`voce` skill**; for a client, a **Project**.
5. **Test and correct:** have a text produced, compare it with yours, and refine
   the context until it "sounds" like you.

> **Tip:** the voice test is simple. Have Claude write a short text and ask
> yourself: would you sign it? If not, a trait is missing: add it to the context.

## Common mistakes

- **Leaving Claude its default register.** On texts that carry your name it shows.
  Give it your voice.
- **The same rule everywhere.** Assign each tool its reach; one rule, one place.
- **Describing the voice in words.** Real examples are worth more than a thousand
  adjectives: start from your texts.
- **Stopping at the first rendering.** Voice is refined by iterating on the context
  file.

## Summary

1. Giving Claude your voice makes texts publishable without rewriting them.
2. The tools have different reach: **Instructions** (always), **Styles** (how to
   write), **Projects** (a topic), **Skills** (repeatable rules).
3. **Context files** are the raw material from which Style, Project and voice skill
   are born.
4. **Compose** the tools: one rule in one place only.
5. Extract the voice from your **real texts**, then choose the container and
   iterate.

## Next step

You've completed Level 5. In **Level 6 — Advanced** we move on to fine control of
the tools, starting from **ch. L6.1 — Advanced Claude Code**: hooks, sub-agents and
granular permissions.

---

*Synthesis chapter between Instructions/Styles (ch. L1.3), Projects (ch. L3.2) and
Skills (ch. L5.1-5.3). Product details from the ledger, verified on 24/06/2026. No
command executed here.*
