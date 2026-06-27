# Chapter L6.1 — Advanced Claude Code

> Level 6 — Advanced.
> Product details verified on 24/06/2026 against official sources.

## Goal

By the end you'll know three advanced levers in Claude Code: **hooks** to attach
your own commands to events, **sub-agents** to delegate tasks to separate
contexts, and granular **permissions**. These are the tools that turn Claude Code
from an assistant into an integral part of your workflow.

## Prerequisites

- Claude Code installed and a project configured (ch. L2.2, L2.4).
- Comfortable with `settings.json` and basic permissions (ch. L2.4).

## Hooks: attaching commands to events (VOLATILE)

A **hook** is a shell command that Claude Code runs automatically at a given
**event** in its lifecycle: before using a tool, after, when a prompt is sent,
and so on. They're there to enforce rules you don't want to leave to good
intentions: run the linter after every edit, block writes to certain files, log
what happened.

You configure them in `settings.json`, organized by **matcher** (the tool's name,
a regex, or empty for all). The main events are `PreToolUse` (before a tool is
called) and `PostToolUse` (after).

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit",
        "hooks": [
          { "type": "command",
            "command": "npm run lint" }
        ]
      }
    ]
  }
}
```

### The exit-code trap (VOLATILE)

The thing that trips everyone up is the hook's **exit code**. It's not a detail:
it changes Claude's behavior.

- **exit 0:** all good, carry on.
- **exit 2:** **blocking** error. stdout is ignored; **stderr** goes back to
  Claude as an error message. On `PreToolUse`, the tool call is blocked.
- **other non-zero codes:** **non**-blocking error, shown to you.

So if you want a hook to **stop** an action and explain to Claude why, you must
exit with **exit 2** and write the reason to **stderr**. Getting the code wrong
is the most common cause of hooks that "don't block."

## Sub-agents: delegating to a separate context (VOLATILE)

A **sub-agent** is a specialized assistant that Claude Code calls on for a task,
with its **own context window**, its own system prompt, and its own tool
permissions. It's there to isolate a piece of work (a code review, for example)
without cluttering the main conversation.

You define it as a Markdown file with frontmatter in `.claude/agents/` (project)
or `~/.claude/agents/` (personal). Claude decides which sub-agent to delegate to
by reading the `description`, just like with Skills.

```markdown
---
name: code-reviewer
description: Reviews changes for quality
  and correctness. Use it before committing.
tools: Read, Grep, Glob
---

You are a careful reviewer. Look for logic
errors, edge cases, and readability issues.
```

> **Tip:** the `/agents` command guides you through creating a sub-agent and can
> generate a first draft from a description.

## Granular permissions (EVERGREEN)

Basic permissions (`allow`/`deny`, ch. L2.4) decide what Claude can do without
asking. Hooks raise the bar: a `PreToolUse` hook can **evaluate** the individual
action and decide at runtime whether to allow it, deny it, or ask for
confirmation. So you move from static rules ("never `rm -rf`") to dynamic ones
("block writes outside `src/`"). The principle stays the one from ch. L2.4: grant
the repetitive and safe, guard the destructive.

## In practice: a hook that blocks

1. Open `.claude/settings.json`.
2. Add a `PreToolUse` hook with the matcher for the tool you want to watch.
3. In the command, check the condition; if it should be blocked, write the reason
   to stderr and exit with **exit 2**.
4. Start Claude Code and try an action that should be blocked.
5. Check that Claude receives the message and stops.

## Common mistakes

- **Hook that doesn't block.** Missing the **exit 2**: with other codes the
  action proceeds. (VOLATILE)
- **Message in the wrong place.** On a block, write to **stderr**, not stdout:
  stdout is ignored. (VOLATILE)
- **Sub-agent without a clear description.** Claude won't know when to delegate
  the task: take care with the `description`.
- **Permissions too broad.** Opening everything removes the safety net (ch.
  L2.4).

## Summary

1. **Hooks** run your commands on Claude Code's events, from `settings.json` by
   matcher.
2. The **exit-code trap**: only **exit 2** blocks, and the reason goes to
   **stderr**.
3. **Sub-agents** delegate a task to a separate context; Claude picks based on the
   `description`.
4. Granular permissions: hooks evaluate at runtime what to allow.
5. Philosophy unchanged: grant the safe, guard the destructive.

## Next step

In **ch. L6.2 — MCP custom** we'll see how to connect to Claude what doesn't
already have a ready connector, and the pattern that pairs a skill with an MCP
server.

---

*Data on hooks, sub-agents, and permissions verified on 24/06/2026 against
code.claude.com/docs (hooks, sub-agents). The configuration examples were not run
here.*
