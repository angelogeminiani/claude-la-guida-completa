# Chapter C.2 — Appendices

> Closing — reference material.
> Product details verified on 24/06/2026 against official sources.

## How to use these appendices

They aren't read in sequence: they're consulted. You'll find a glossary of the
recurring terms, a troubleshooting table for the most common problems, and the
official links from which to verify the volatile data.

## Glossary (EVERGREEN)

- **Agentic:** a way of working in which Claude carries a task forward over several
  steps, not just a single answer.
- **API:** programmatic access to the models, to integrate Claude into your own
  software (ch. L6.6).
- **Canvas:** Claude Design's canvas where the generated interfaces appear (ch.
  L4.1).
- **Connector:** a link that gives Claude access to an app, with your permissions
  (ch. L3.3).
- **Context window:** the working memory of a single chat, measured in tokens (ch.
  L6.4).
- **Cowork:** non-code agentic work in the desktop app, in an isolated VM (ch.
  L3.1).
- **Design / `/design-sync`:** the canvas and the command that syncs design and
  code both ways (ch. L4.3).
- **Dispatch:** starting from your phone a task that Claude runs on your computer
  (ch. L6.3).
- **Effort level:** how deeply Claude reasons; higher consumes more usage (ch.
  L6.4).
- **Handoff:** passing a design to Claude Code so it becomes software (ch. L4.3).
- **Hook:** a command attached to a Claude Code event (ch. L6.1).
- **MCP:** open standard that connects Claude to external tools and data (ch.
  L6.2).
- **Native installer:** the recommended method to install Claude Code, without Node
  (ch. L2.2).
- **OAuth:** delegated access via the browser, without typing the password in the
  terminal (ch. L2.3).
- **Prompt:** the request you write to Claude (ch. L1.2).
- **Project:** a workspace with instructions and a knowledge base shared across
  chats (ch. L3.2).
- **Routine:** a Claude Code automation that runs on the cloud (ch. L6.3).
- **Scheduled Task:** a recurring Cowork task, runs with the computer on (ch.
  L6.3).
- **Skill / `SKILL.md`:** reusable knowledge that Claude loads on its own (ch.
  L5.1).
- **Sub-agent:** an assistant with its own context and permissions, that Code
  delegates to (ch. L6.1).
- **Tool use:** the use, via API, of tools you provide (ch. L6.6).
- **Usage limit:** how much you can use Claude in a period (ch. L6.4).
- **Isolated VM:** the virtual machine Cowork runs in; it sees only the connected
  folders (ch. L3.1).

## Troubleshooting (VOLATILE)

Table C.2.1 — Common problems and first solution.

| Problem | Cause | Solution |
|---|---|---|
| `command not found` | PATH | new terminal (L2.2) |
| Login failed | extra API key | `unset` the key (L2.3) |
| Function missing | admin | Admin > Capabilities (L1.3) |
| Hook doesn't block | exit code | use exit 2 (L6.1) |
| Connector inert | not activated | toggle in chat (L3.3) |
| Task skipped | PC off | reopen the app (L6.3) |
| Chat saturated | length limit | new chat (L6.4) |

## Official links (VOLATILE)

From here you verify the data that changes over time. These are the only sources
this book relies on for product details.

- **claude.ai** — access to Claude (web).
- **claude.com** and **claude.com/pricing** — products and plans.
- **support.claude.com** — official guides and troubleshooting.
- **code.claude.com/docs** — Claude Code documentation.
- **platform.claude.com/docs** — API and Console documentation.
- **agentskills.io** — the open standard for Skills.
- **github.com/anthropics/skills** — example skills.

## Legal notes (EVERGREEN)

**Independent publication, not affiliated with or endorsed by Anthropic**. Claude
and Anthropic are trademarks of their respective owners. The product details
(versions, commands, prices, menus, plans) are **verified as of the date
indicated** in each chapter and in the ledger, and are **subject to change**: for
current values refer to the official sources above and to the companion repo.

## Summary

1. The **glossary** collects the recurring terms, with the cross-reference to the
   chapter.
2. The **troubleshooting** table gives the first move for common problems.
3. The **official links** are the only sources for the volatile data.
4. The publication is **independent** and not affiliated with Anthropic.
5. The data is verified as of the date indicated and should be rechecked against
   the sources.

## The end

You've gone through the whole journey: from your first messages in chat all the way
to the API and automation. The product will keep changing — that's why the volatile
data is dated and collected in the companion repo. The underlying ideas, on the
other hand, stay: describe the result, give context, iterate, and make the pieces
of the ecosystem work together.

---

*Reference material. The glossary and cross-references are evergreen;
troubleshooting, links, and product details verified on 24/06/2026 against the
official sources listed.*
