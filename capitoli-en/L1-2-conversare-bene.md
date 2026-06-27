# Chapter L1.2 — Talking to Claude well

> Level 1 — Foundations.
> Product details verified on 22/06/2026 against official sources.

## Goal

By the end you will know how to write requests (prompts) that get useful answers
on the first try: clear, with the right context and in the format you need. It's
the skill that makes the difference between using Claude and using it well.

## Prerequisites

- Having sent your first message (ch. L1.1).

## The golden rule (EVERGREEN)

Think of Claude as a new collaborator: skilled, but with no context on your
habits. If your request would confuse a competent person who doesn't know your
work, it will confuse Claude too. From this come five practical principles.

None of these principles requires technical jargon: they're the same common
sense you'd use when delegating a task to a person. The difference is that with
Claude the cost of retrying is almost nil, so you can afford to be explicit
without fearing you're "asking too much."

## 1. Be clear and specific (EVERGREEN)

Say explicitly what you want, for whom and with what constraints. Indicate the
length, tone and format of the output. When the order matters, use numbered
steps. "Write something about the product" leaves too much room; "Write three
lines of description for product X, professional tone, for a technical audience"
guides the answer.

## 2. Give context and motivation (EVERGREEN)

Explaining the why of a request helps Claude get it right. "Summarize this report
**for an executive who has two minutes**" leads to a different result than a
generic summary. Context isn't an extra: it's what guides the choices. Even a
constraint, if framed positively, helps: instead of "don't be technical," write
"use words a customer outside the field would understand."

## 3. Use examples (EVERGREEN)

Showing one or two examples of the result you want is one of the most reliable
ways to guide format and tone. If you need a product sheet with a certain
structure, paste in a finished sheet as a template. Three to five well-chosen
examples are worth more than a thousand explanations.

## 4. Control the format (EVERGREEN)

Say what you want, not what you don't want. "Reply with a bulleted list of at
most five items" is better than "don't be wordy." If you want a table, ask for
it; if you want JSON or Markdown, specify it. Stating the format saves round
trips: if you need a three-column table or a numbered list, say so up front
instead of reformatting later.

## 5. Iterate (EVERGREEN)

The first answer is a draft. Instead of starting over, course-correct: "Shorter",
"More informal tone", "Add a concrete example". Refining in two or three passes
is faster than searching for the perfect prompt on the first try.

## Giving role, structure and constraints (EVERGREEN)

Beyond the five principles, two moves raise the quality on complex requests.

**Assign a role.** Indicating the point of view to answer from steers tone and
depth: "Answer as an auditor" or "Explain it the way you would to a non-technical
colleague." It's not a gimmick: it narrows the field of plausible answers to the
ones you actually need.

**Structure long requests.** When a request has many parts, separate them: one
block for the context, one for the task, one for the desired format. Even just
using dashes or sub-headings helps Claude not miss anything. An orderly request
produces an orderly answer.

## Before and after (EVERGREEN)

The table shows how to go from a weak request to an effective one. The principle
is always the same: add purpose, audience and format.

Table L1.2.1 — Same intent, weak prompt and better prompt.

| Intent | Weak prompt | Better prompt |
|---|---|---|
| Email | "write an email" | "short email, customer, courteous tone" |
| Summary | "summarize" | "5 points for a busy executive" |
| Code | "make a function" | "function that validates an email, with tests" |

> **Tip:** if you don't know where to start, write the objective first ("I want
> to get…"), then the context, finally the format. Three lines are enough.

## A complete example (EVERGREEN)

Let's put the principles together on a real case. Start from a gut-instinct
request:

> Write me a post to announce the new product.

It's vague: no audience, no channel, no tone. Here's the same request rewritten
applying purpose, audience and format:

> Write a LinkedIn post (max 120 words) to announce the launch of product X to
> professionals in the field. Competent but warm tone, no superlatives. Close
> with a question that invites a comment.

The second version declares purpose, audience, channel, length, tone and even the
closing. Claude has little left to guess, and the first answer is already close
to what you wanted: the time spent writing the request well is time you get back
on the corrections you won't have to make.

## Iterate or start over? (EVERGREEN)

Iterating in the same chat preserves the context: it's the right choice when
you're refining a result. It's better, instead, to open a **new chat** when you
change topic entirely, so the old context doesn't "contaminate" the new answers.
Practical rule: same objective, same chat; different objective, new chat.

## Breaking up a big task (EVERGREEN)

Huge requests ("write me the complete marketing plan") produce generic answers,
because Claude has to guess too much. It's better to proceed in stages: first the
outline, then one section at a time, finally the overall review. At each step you
give a clear objective and check the result before moving on. This way you keep
control and get consistent quality, instead of a wall of text to fix all at once.
This applies to texts, analysis and code alike: it's the difference between
delegating a project and delegating a step.

## Longer doesn't mean better (EVERGREEN)

Being specific doesn't mean writing paragraphs. Often three well-aimed lines —
objective, context, format — beat half a page of muddled instructions. Aim for
clarity, not quantity: every word that doesn't add a constraint is noise. If you
notice you're repeating yourself, cut instead of adding. That's how you know a
good prompt: none of its parts can be deleted without losing something.

## Common mistakes

- **A generic request.** Without a purpose and audience, the answer is anonymous.
- **Too many objectives at once.** Break complex tasks into steps.
- **Saying only what you don't want.** Indicate the desired result, not the
  prohibitions.
- **Not giving examples.** When the format matters, a template is worth more than
  a description.
- **Giving up at the first answer.** Iterate: it's part of the method, not a
  failure.

## In practice: transform a weak prompt

1. Start from a vague request you'd use on instinct.
2. Add **purpose** ("it's for…") and **audience** ("for…").
3. Specify the **format** (length, structure, tone).
4. If you have an example of the desired result, paste it in.
5. Send, evaluate and **iterate** with a targeted correction.

## Summary

1. Treat Claude as a competent colleague but without your context.
2. Be **clear and specific**: purpose, audience, constraints.
3. Give **context** and **examples**; they guide more than a thousand words.
4. Control the **format** by saying what you want, not what you avoid.
5. **Iterate**: the first answer is a draft to refine.

## Next step

In **ch. L1.3 — Settings and styles** we'll configure tone, preferences and
capabilities (Web search, Code execution, Memory) so you don't have to repeat
them in every chat.
