# Chapter L6.4 — Managing usage limits

> Level 6 — Advanced.
> Product details verified on 27/06/2026 against official sources.

## Goal

By the end you'll understand the difference between **usage limit** and **length
limit**, what consumption depends on, and how to work for a long time without
hitting the limits. This is what lets you use Claude sustainably,
especially on heavy tasks.

## Prerequisites

- Knowing the plans (ch. F.3) and Projects (ch. L3.2).

## Two different limits (VOLATILE)

Claude has two types of limit, which work in distinct ways:

- **Usage limit:** *how much* you can use Claude in a period. It's your
  "conversation budget." When it runs out, you wait for the reset.
- **Length limit:** *how long* a single chat can get, that is, the **context
  window** (Claude's working memory in that conversation).

The first is about quantity over time; the second about the depth of a single
chat. Confusing them leads to the wrong choices when something "gets stuck."

## What consumption depends on (VOLATILE)

Usage isn't consumed in fixed chunks. Several factors weigh in: the **length and
complexity** of the conversation, the active **features**, the **model** chosen,
and the **effort level** (how deeply it reasons). A detail that surprises people:
all surfaces — claude.ai, Claude Code, Claude Desktop — draw on the **same** usage.
They're not separate budgets.

> **Note:** with Code execution on, long chats trigger **automatic context
> management**: Claude summarizes older messages to keep going. Convenient, but
> long conversations consume **more** usage. (VOLATILE)

## The context window (VOLATILE)

In chat, on paid plans, the context window is **500K tokens** for the flagship
models (Opus 4.6/4.7/4.8 and Sonnet 4.6) and **200K** for the others. In **Claude
Code** the flagship models go up to **1M tokens**: on Pro, for the million, you
need to enable usage credits. You can't enlarge it at will, but you can use it
better: that's where the difference is decided between a chat that holds up and one
that saturates.

## Cheaper tasks: cutting consumption (EVERGREEN)

A few moves lower consumption for the same result:

- **Use Projects.** They leverage RAG (targeted retrieval): they load into context
  only what's needed, instead of everything.
- **Short instructions.** Concise Projects and prompts weigh less and deliver more.
- **Remove what you don't need.** Unneeded files in Projects, and unnecessary
  **tools/connectors**: they're token-intensive, so turn them off when not in use.
- **Lower the effort** and disable **extended thinking** on routine tasks.
- **Choose the right model.** Don't use the most powerful one "just to be safe"
  (ch. F.3): often you pay more with no benefit.

## What to do at the limit (EVERGREEN)

When you hit a limit, the move depends on which one:

- **Usage limit reached:** wait for the **reset**, **upgrade** your plan, or buy
  **usage credits** (on paid plans) to continue right away.
- **Length limit (chat too long):** open a **new conversation**, or move the
  material into a **Project** to work on it more efficiently.

> **Tip:** if you're in a long chat and near the usage limit, it's often worth
> starting over in a new chat: you restart with the essential context instead of
> dragging the whole history along.

## In practice: work for a long time without getting stuck

1. For recurring work, put it in a **Project** instead of endless chats.
2. Keep instructions short and remove files you no longer use.
3. Turn off tools and connectors not needed for that session.
4. On simple tasks, lower the effort and turn off extended thinking.
5. If you near the limit in a long chat, **open a new one**.

## Common mistakes

- **Confusing the two limits.** If it's the chat that's full, no need to wait for
  the reset: open a new chat.
- **Keeping everything on.** Unneeded tools and connectors consume context and
  usage: turn them off. (VOLATILE)
- **Oversized model.** More power than needed costs more with no better output.
- **Endless chats.** Dragging a huge history along consumes usage: split into chats
  or use Projects.

## Summary

1. **Usage limit** = how much you use over time; **length limit** = how long a chat
   is (context window).
2. Consumption depends on length, features, **model**, and **effort**; all surfaces
   count against the **same** usage.
3. Context window in chat: **500K** for flagship models, **200K** for the others;
   in Claude Code up to **1M** (with usage credits on Pro).
4. Cut consumption with Projects, short instructions, fewer active tools, lower
   effort.
5. At the limit: reset/upgrade/**credits** for usage; **new chat**/Project for
   length.

## Next step

In **ch. L6.5 — Claude at work, safely** we'll see how to introduce Claude into an
organization: governance, roles, data, and when not to use a personal account.

---

*Data on usage/length limit and context window verified on 27/06/2026 against
support.claude.com/en/articles/11647753 and /articles/8606394. Values subject to
change: see the ledger and the official sources for updates.*
