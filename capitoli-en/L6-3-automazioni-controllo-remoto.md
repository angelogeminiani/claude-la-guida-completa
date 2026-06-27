# Chapter L6.3 — Automations and remote control

> Level 6 — Advanced.
> Product details verified on 24/06/2026 against official sources.

## Goal

By the end you'll know how to make Claude work over time without sitting in front
of it: **Scheduled Tasks** in Cowork, Claude Code's cloud **Routines**, and
**Dispatch**, which turns your phone into a remote control. Above all you'll
understand which to choose, because they run in different places.

## Prerequisites

- Cowork (ch. L3.1) for scheduled tasks; Claude Code (ch. L2.2) for routines.
- A paid plan. (VOLATILE)

## Three tools, three places (EVERGREEN)

The difference that matters isn't what they do, but **where they run**: that's what
decides whether they work with the computer off, and how suited they are to
non-technical work.

Table L6.3.1 — Where each tool runs.

| Tool | Where it runs | With computer off |
|---|---|---|
| Scheduled Task | Cowork, Desktop | no |
| Routine | Anthropic cloud | yes |
| Dispatch | your computer | no |

## Scheduled Tasks (VOLATILE)

**Scheduled Tasks** run a Cowork task automatically, on a schedule or on demand:
"every morning check my email," "every Friday prepare the report." They live in
**Cowork on Desktop**, on paid plans.

The limit to know: they run **only with the computer on and the Desktop app open**.
If the computer is off or the app is closed at the scheduled time, the task is
**skipped** and runs on its own as soon as you turn the computer back on or reopen
the app. They're perfect for someone who leaves the computer on, less so for
someone who needs a guarantee that it runs no matter what.

## Routines (VOLATILE)

Claude Code's **Routines** are saved configurations — a prompt, one or more
repositories, and your connectors — that run on **Anthropic's cloud**, not on your
computer. That's why they work even with the machine off.

Their strong point is **combinable triggers**: the same routine can start on a
schedule, in response to an API call, and on a GitHub event, all at once. They're
the tool for development automations that need to be reliable and independent of
your machine.

## Dispatch (VOLATILE)

**Dispatch** turns your phone into a remote control for Claude on your computer.
You send a message from the mobile app and Claude runs the task **on your
machine**: it reads local files, pulls data from connectors, searches the web, and
reports the result back to you. Between the mobile app and the Desktop a **single,
persistent thread** opens up, like a walkie-talkie: you assign remotely, Claude
works locally.

It's the answer to "I'd like to kick off that job while I'm out": the computer has
to be on, but you don't.

## Which to choose (EVERGREEN)

- **Non-technical, recurring** work, and you keep the computer on → **Scheduled
  Task**.
- **Development** automation that must run **always**, even with the machine off,
  with various triggers → cloud **Routine**.
- You want to **kick off a job remotely** that uses your local files → **Dispatch**.

## In practice: schedule a recurring task

1. In Cowork, describe the task as you would for normal work (ch. L3.1).
2. Set the recurrence (for example "every morning at 8").
3. Leave the computer on and the Desktop app open at the scheduled time.
4. For independent development automations, consider a **Routine** in Claude Code
   instead.
5. To start it from outside, use **Dispatch** from the mobile app.

## Common mistakes

- **Scheduled Task with computer off.** It's skipped and runs on reopening: for
  guaranteed execution use a cloud Routine. (VOLATILE)
- **Confusing Routine and Scheduled Task.** Routines run on the cloud (Code), Cowork
  tasks on your Desktop.
- **Expecting Dispatch with the machine off.** It runs locally: the computer has to
  be on. (VOLATILE)

## Summary

1. The key difference is **where** the tool **runs**.
2. **Scheduled Tasks**: Cowork on Desktop; only with computer on and app open.
3. **Routines**: Anthropic's cloud (Code); always run, combinable triggers.
4. **Dispatch**: you start it from your phone, Claude runs it on your computer (which must be on).
5. Choose based on the reliability required and the type of work.

## Next step

In **ch. L6.4 — Managing usage limits** we'll see what consumption depends on and
how to work for a long time without hitting the limits.

---

*Data on Scheduled Tasks, Routines, and Dispatch verified on 24/06/2026 against
support.claude.com (scheduled tasks, dispatch) and code.claude.com/docs
(scheduled-tasks/routines). The features require a paid account, so they were not
run here.*
