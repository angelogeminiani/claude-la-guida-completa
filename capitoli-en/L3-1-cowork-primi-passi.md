# Chapter L3.1 — Cowork: first steps

> Level 3 — Daily work.
> Product details verified on 27/06/2026 against official sources.

## Goal

By the end you will know what Cowork is and how it differs from Chat and Claude
Code, how to start a task on a folder of your computer, how to describe a result
instead of a sequence of steps, and how to approve the actions Claude proposes
while it works.

## Prerequisites

- Claude Desktop installed (see ch. L2.1).
- A paid plan: **Pro, Max, Team or Enterprise**. Cowork is not included in the
  Free plan (see ch. F.3 and the ledger). (VOLATILE)
- A folder with files it makes sense to work on.

## What Cowork is (VOLATILE)

Cowork is the desktop app's tab for **agentic non-code work**: you hand it a task
on a folder and it carries it forward on its own — reads the files, reasons,
creates or modifies documents, runs steps in sequence — stopping to ask you for
confirmation when needed. It is available on the paid plans on macOS and
Windows. (VOLATILE: the product's status evolves fast; see the ledger.)

It runs in an **isolated VM** (a virtual machine, a computer inside the
computer) on your device. This is the key point for trust: Cowork reads and
writes **only in the folders you connect to it**, and the network follows the
egress settings (what it can reach on the internet). It doesn't see the rest of
your disk unless you give it to it.

## Cowork, Chat and Code: who does what (EVERGREEN)

The app's three tabs answer different needs. Choosing them well is half the job.

Table L3.1.1 — When to use which tab.

| Tab | For what | Form |
|---|---|---|
| Chat | Questions, drafts, ideas | Back and forth |
| Code | Software development | On code files |
| Cowork | File tasks, multi-step | Agentic, long |

In short: if you want an answer, Chat. If you're programming, Code. If you want
someone to **do** an involved thing on your files — reorganize a folder, produce
a report from several documents, prepare a series of files — Cowork.

## End-state, not the steps (EVERGREEN)

The most common mistake on first use is to guide Cowork step by step, the way you
do in chat. The opposite works better: describe the **result you want** (the
"end-state") and let it find the sequence.

- **Weak (steps):** "Open the file. Now read column B. Now copy..."
- **Better (end-state):** "From these three sales Excel files, create a summary
  by region with quarterly totals, saved as `summary.xlsx`."

Describing the result plays to what Cowork is made for: planning the path. You
define the "where to get to" and the constraints; it finds the "how".

## Approving the actions (EVERGREEN)

While it works, Cowork stops before the actions that matter and shows you what
it's about to do: create a file, modify one, run a command. You approve or
correct. It's the same principle as Claude Code's permissions (see ch. L2.4):
the repetitive part flows, the decisions stay yours.

Don't approve sight unseen. Read what it proposes, especially the first few
times: that's how you learn to trust it — or to understand where you need to be
more precise in the request.

Cowork has two **permission modes** that decide how often it stops:

- **Ask before acting:** it stops and asks for confirmation at every action.
  It's the right mode with new files or tools, or when you want to keep
  everything under control.
- **Act without asking:** it proceeds without stopping. Faster, but riskier:
  use it only while you are supervising, on files and sites you trust.

In **both** modes, Claude always asks for confirmation before **deleting** files
permanently: deletion is never automatic.

## In practice: your first task

1. Open Claude Desktop and go to the **Cowork** tab.
2. **Connect a folder**: choose one with real files, but of which you have a
   copy. Cowork will act only inside this folder.
3. Write the task as an **end-state**, with the constraints:

   ```text
   In this folder there are scattered .txt notes.
   Group them by topic into subfolders and
   create an INDEX.md listing what's where.
   ```

4. Let it plan. When it stops for an action, **read and approve**.
5. At the end of the task, check the result in the folder. If it's not what you
   wanted, refine the request and run it again.

## Common mistakes

- **Guiding it step by step.** Wastes its strength. Describe the result, not the
  procedure.
- **Connecting the entire disk or critical folders.** Connect only what's
  needed, and work on copies until you trust it.
- **Expecting Cowork in the Free plan.** It needs a paid plan. (VOLATILE)
- **Approving without reading.** The first few times, check what it proposes:
  that's where you learn to give it better instructions.

## Summary

1. Cowork is the desktop tab for agentic non-code work, in an **isolated VM**
   that sees only the connected folders.
2. Chat for answers, Code for software, Cowork for multi-step tasks on your
   files.
3. Describe the **result** (end-state) and the constraints, not the sequence of
   steps.
4. Approve the actions Cowork proposes: control stays yours.
5. Connect only the necessary folders and start from copies.

## Next step

In **ch. L3.2 — Projects** we look at how to give recurring work a stable home:
instructions, reference files and memory that persist from one session to the
next.

---

*Details on Cowork (isolated VM, plans, connected folders, permission modes)
from the ledger, verified on 27/06/2026 on
support.claude.com/en/articles/13345190 and code.claude.com/docs. The example
task was not run here: it requires the desktop app with a paid account.*
