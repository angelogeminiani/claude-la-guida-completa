# Chapter L1.1 — First contact

> Level 1 — Foundations.
> Product details verified on 22/06/2026 against official sources.

## Goal

By the end you will have opened Claude on the platform you prefer, sent your
first message, attached a file, and you'll know how to read an answer with a
critical eye. It's the base everything else rests on.

## Prerequisites

- A Claude account (see ch. F.3). The Free plan is enough to start. (VOLATILE)
- An active internet connection.

## Where to find Claude (VOLATILE)

Claude is available on three surfaces, synchronized when you log in with the same
account:

- **Web:** go to claude.ai in your browser. It's the fastest way to try it.
- **Desktop:** the app for macOS and Windows (see ch. L2.1 to install it).
- **Mobile:** the apps for iOS and Android, useful for continuing on the go.

Conversations, projects and preferences follow you across devices. You can start
a chat on your phone and pick it up on your computer.

Which to choose? To try it right away, the **web** requires no installation: just
a browser. The **desktop** app is worth it when you use Claude every day or you
need local features like Cowork and Code (Level 2). **Mobile** is handy for
capturing an idea on the fly or continuing on the go. It's not a final choice:
the account is the same and you switch from one to another whenever you want.

> **Note:** one exception to syncing are incognito chats (ghost icon): they're
> not saved and so don't appear on other devices. They're meant for throwaway
> questions.

## The first message (EVERGREEN)

It's straightforward: type in the text box and send. No special command or
syntax required. Treat Claude as a competent collaborator who has no context on
your work: the clearer you are, the better the answer. We'll go deeper into how
to write good messages in ch. L1.2.

A useful first experiment: ask for something concrete, for example "Summarize
this text in five points" by pasting in a paragraph. You'll immediately see how
Claude structures the answer.

### A concrete example

Imagine pasting in the text of an email you received and writing: "Summarize this
email in three points and suggest a courteous reply." Claude responds with the
three points and a draft ready to adapt. From here you can keep going in the same
thread: "Make the reply more formal" or "Add a proposed date for the call." You
don't start over: as long as you stay in the same chat, Claude keeps the context
of the previous messages.

This is the underlying dynamic: a conversation, not a single command. Each
message builds on the previous ones, and that's what makes the chat more useful
than a plain search.

> **Tip:** when a result only partly satisfies you, course-correct with a short
> message instead of rewriting the whole request. Often a single line ("shorter",
> "informal tone") is enough to get where you want.

## The interface in brief (VOLATILE)

The interface is minimal. Around the text box you'll find a few commands worth
recognizing right away:

- The **"+"** button opens attachments (files and photos).
- The **"Search and tools"** menu (sliders icon) gathers tools and styles, like
  Web search and the response style.
- The **ghost** icon starts an incognito chat: a temporary conversation, not
  saved in your history.

> **Note:** the exact position of the buttons can change between versions and
> across web, desktop and mobile. The names and functions, though, stay the same.

## Attaching files and images (VOLATILE)

You can give Claude documents and images to analyze. The supported formats
include PDF, DOCX, CSV, TXT, HTML, JSON and others; for images, JPEG, PNG, GIF
and WebP. Excel files (XLSX) require that Code execution be active (see ch.
L1.3).

Table L1.1.1 — Ways to attach and typical limits.

| How | What | Indicative limit |
|---|---|---|
| "+" button | files and photos | ~500 MB/file |
| Drag and drop | multiple files | ~20 files/chat |
| Paste | images | from the clipboard |

> **Warning:** from documents that aren't PDFs, Claude usually extracts only the
> text, not the embedded images. For PDFs, the visual analysis is more complete
> under ~100 pages. The limits are volatile: verify them if you upload large
> files.

## What Claude does with attachments (EVERGREEN)

Attaching a file doesn't just mean "feeding it" to Claude: you can ask it to
extract data, summarize it, compare it with another document or translate it. The
more precise you are about what you want it to do, the more on-target the answer.
"Extract the monthly totals from the table" is better than "look at this file."
If a document is long, point to the part that matters: you help Claude focus and
you reduce generic answers.

## Reading an answer with judgment (EVERGREEN)

Claude is useful, but not infallible. Three healthy habits from day one:

- **Check the facts that matter.** For dates, numbers and names, ask for the
  source or verify elsewhere. For recent information, turn on Web search (ch.
  L1.3).
- **Ask it to show its reasoning.** "Explain how you got there" makes the answer
  more transparent and easier to correct.
- **Iterate.** The first answer is a draft. Refine it with a second message
  instead of redoing everything from scratch.
- **Be wary of answers that are too confident on verifiable details.** A language
  model can state a wrong fact with confidence (the phenomenon of
  "hallucinations"): a confident tone doesn't guarantee correctness.

It's not a flaw to fear, but a way of working to learn. Claude is at its best when
it reasons, drafts and transforms the material you provide, rather than when you
ask it to recall facts "from memory." For facts that change over time, Web search
is the natural complement: it brings up-to-date information with sources.

## In practice: your first conversation

1. Open claude.ai (or the app) and log in.
2. Write a concrete request, for example a summary or an email draft.
3. Attach a file with the "+" button and ask Claude to use it.
4. Read the answer and send a second one to improve it.
5. Try the incognito chat (ghost icon) for a throwaway question.
6. Repeat the same request on another surface (web or mobile) and notice that the
   conversation follows you.

## Common mistakes

- **Too vague a request.** "Write me something" produces generic answers. State
  the purpose, audience and format (ch. L1.2).
- **A file not read the way you expect.** If it's a document with images,
  remember that Claude extracts the text; describe in words what matters.
- **Trusting 100%.** Verify sensitive facts; don't take a date or a number for
  granted without checking.
- **Using incognito for work you want to find again.** Those chats aren't saved:
  if you need to pick them up, use a regular chat.

## Summary

1. Claude is on **web, desktop and mobile**, synced with your account.
2. You use it by writing in the text box: no special syntax.
3. Recognize **"+"** (attachments), **Search and tools** (tools/styles) and the
   **ghost** icon (incognito).
4. You can attach many formats; watch out for the limits and the text-only
   extraction.
5. Read answers with judgment: verify, ask for the reasoning, iterate.

## Next step

In **ch. L1.2 — Talking to Claude well** we'll see how to write effective
prompts, with before/after examples and the most common mistakes to avoid.
