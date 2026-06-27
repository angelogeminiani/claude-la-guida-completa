# Chapter L1.3 — Settings and styles

> Level 1 — Foundations.
> Product details verified on 22/06/2026 against official sources.

## Goal

By the end you will know how to configure Claude so it answers in your tone and
with the right capabilities, without repeating the same instructions in every
chat. We'll look at account preferences, Styles and the Web search, Code
execution and Memory capabilities.

## Prerequisites

- Knowing how to start a conversation (ch. L1.1).

## Account-level instructions (VOLATILE)

In **Settings → Instructions for Claude** you set preferences that apply to all
conversations: what your name is, what language to write in, the tone you prefer,
recurring terms from your work. It's the right place for the things you'd say in
every chat: writing them once saves you time.

It's different from an instruction given in a single chat, which applies only
there: these apply everywhere. Useful examples to put here: "always write in
English", "I prefer concise answers with examples", "I'm a developer", "don't use
emoji". Keep them short and update them when your needs change: it's the most
convenient level for stable preferences.

## Response styles (VOLATILE)

**Styles** control *how* Claude communicates. There are a few presets — Normal,
Concise, Formal, Explanatory — and you can create custom ones, even by uploading
samples of your writing. You'll find them in the "Search and tools" menu next to
the text box.

When to use them? **Concise** for quick, dense answers; **Explanatory** when
you're learning and want more context; **Formal** for professional texts. The
**custom** style is the most powerful: you upload some of your own texts and
Claude imitates their register and rhythm. It's the first step toward "making
Claude sound like you," which we go deeper into with Skills in Level 5.

> **Warning:** Styles are evolving toward Skills (see Level 5). Features and names
> may change: it's a volatile area, so check the current state in the settings.

## The capabilities to know (VOLATILE)

Beyond tone, you can turn on capabilities that broaden what Claude can do. The
table summarizes them; below, the detail.

Table L1.3.1 — Main capabilities and availability.

| Feature | What it's for | Availability |
|---|---|---|
| Web search | up-to-date facts | all plans |
| Code execution | create files | all plans |
| Memory | remembers history | all plans |
| Chat search | search past chats | paid |

**Web search.** Turns on live search on the web, with source citations. It's
indispensable for recent information, where the model's "from memory" knowledge
isn't enough. It's activated from the "+" button or the tools menu. It consumes
your usage limits. On Team and Enterprise it must be enabled by an administrator.
In practice: ask "search for the latest news on X" and Claude brings results with
the links, so you can trace the source. Without it, it answers with what it
"knows" and on recent facts it can be wrong.

**Code execution and file creation.** Gives Claude a sandbox environment to run
code and produce real files: Excel, PowerPoint, Word, PDF, charts. It's also
needed to upload XLSX files. It's available on all plans, with an indicative
limit of ~30 MB per file. It's what makes requests like "create an Excel with
these expenses and a pie chart" possible: Claude writes the file and hands it
back to you ready to download.

**Memory and chat search.** **Memory** builds a summary of your history, so
Claude can draw on past context; it's available on all plans. **Search across
past chats**, by contrast, is reserved for paid plans. Incognito conversations
(ghost icon) are excluded from both.

## Privacy and data control (EVERGREEN)

Three things to keep in mind. **Incognito** chats don't end up in your history or
in Memory: use them when you don't want to leave a trace. **Memory** is a
summary, not a faithful copy: if a fact is important, repeat it in the chat
instead of trusting it was remembered. Finally, on **Team** and **Enterprise**
some capabilities are enabled by an administrator from *Admin → Capabilities*: if
you don't see them, it's not your fault, ask whoever manages the organization.

> **Tip:** you don't have to turn everything on right away. Start from Web search
> and Code execution: they cover most everyday cases; you add the rest when
> needed.

## Projects, in a nutshell (VOLATILE)

A **Project** is a workspace with its own knowledge base and dedicated
instructions, shared across the chats of that project. It's useful when you work
for a long time on the same topic. Free users can create up to five; sharing is
reserved for Team and Enterprise. We go deeper into them in ch. L3.2.

## Preferences, Styles or Projects? (EVERGREEN)

They overlap, but they serve different purposes. **Instructions for Claude** are
personal preferences that apply everywhere. **Styles** change how Claude
communicates and you turn them on as needed. A **Project** isolates context and
instructions for a specific topic or client, without polluting your other chats.
Practical rule: stable preferences → Instructions; how to write → Styles; a
standalone job → Project.

A concrete example: to write this book you could keep a Project with the style
rules and the finished chapters, so each new chat starts "up to speed" without
your having to repeat the context.

> **Note:** the settings seen here are personal. In an organization, some choices
> (security, data use for training) are defined by the administrator: your account
> inherits those rules.

## In practice: configure your Claude

1. Open **Settings → Instructions for Claude** and write your name, language and
   tone.
2. Choose a **style** from the "Search and tools" menu (try Concise).
3. Turn on **Web search** and ask a question about a recent fact.
4. In **Settings → Capabilities**, verify that **Code execution** is active.
5. Check the **Memory** settings and decide whether to keep it on.
6. If you're in an organization, check in **Admin → Capabilities** what is
   enabled on your account.

## Common mistakes

- **Repeating the same instructions in every chat.** Put them once in
  "Instructions for Claude".
- **Forgetting Web search on recent facts.** Without it, Claude answers "from
  memory" and can get dates or numbers wrong.
- **Expecting an Excel file without Code execution.** It must be turned on,
  otherwise no file generation.
- **Trusting Memory for everything.** It's a synthesis, not a precise archive:
  for important facts, repeat them in the chat.
- **Thinking it's a bug when a feature is missing.** On Team/Enterprise the
  administrator may have disabled it: check in Admin → Capabilities.
- **Creating a Project for every question.** Projects are for ongoing work; for an
  isolated request a regular chat is enough.

## Summary

1. **Instructions for Claude** applies your preferences to every conversation.
2. **Styles** control tone; they're evolving toward Skills.
3. **Web search** is for up-to-date facts and consumes usage.
4. **Code execution** enables file creation; **Memory** remembers the history.
5. **Search across chats** is paid only; incognito stays excluded.

## Next step

You've completed the foundations. In **Level 2** we move on to local
installation: we start from **ch. L2.1 — Installing Claude Desktop**.
