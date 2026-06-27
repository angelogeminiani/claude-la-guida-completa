# Chapter L6.2 — MCP custom

> Level 6 — Advanced.
> Product details verified on 24/06/2026 against official sources.

## Goal

By the end you'll understand what MCP is in plain terms, when you need a custom
MCP server instead of a ready connector, how to add one to Claude Code, and the
pattern that combines a skill with an MCP. It's the way to connect Claude to what
doesn't already have an integration.

## Prerequisites

- Having used connectors (ch. L3.3).
- Claude Code installed (ch. L2.2), for the hands-on part.

## What MCP is, in plain terms (EVERGREEN)

**MCP** (Model Context Protocol) is an **open standard** for connecting Claude to
external tools and data. Think of a universal power socket: instead of a
custom-built integration for each app, MCP defines a common way for Claude to talk
to a service. An **MCP server** is the component that exposes that service's
actions to Claude.

The connectors in ch. L3.3 are already MCP under the hood: a **custom connector**
is a **remote MCP** (a server reachable over the network). MCP is therefore the
technical layer that sits beneath connectors.

## When you need a custom MCP (EVERGREEN)

The connector directory covers the most common apps. A custom MCP is needed when:

- the app you need **has no ready connector**;
- you want to connect one of your **internal tools** or a company database;
- you need a specific action that no existing connector offers.

In short: first you search the directory; if it's not there, you build or connect
an MCP.

## Local or remote (VOLATILE)

An MCP server can run in two ways, and Claude Code handles both.

Table L6.2.1 — Local and remote MCP compared.

| Type | Where it runs | How |
|---|---|---|
| Local (stdio) | on your computer | child process |
| Remote (HTTP) | on a server | over the network |

The **local** one (`stdio` transport) is started by Claude Code as a child
process that communicates over standard input/output: handy for tools that live
on your machine. The **remote** one (`http` transport) is a server reachable over
the network: it's the form of custom connectors, reached from Anthropic's cloud
(ch. L3.3).

## Adding an MCP to Claude Code (VOLATILE)

From the terminal, the base command is `claude mcp add`. For a local server:

```bash
claude mcp add --transport stdio \
  my-tool -- npx -y my-mcp-server
```

The flags (`--transport`, `--env`, `--scope`) go **before** the name; the `--`
separates the name from the command that starts the server. Environment variables
are passed with `--env` (for example a service's API key).

> **Warning:** a custom MCP gives Claude access to an external service. Only
> connect servers you trust, and don't put secrets in the clear: use environment
> variables. (EVERGREEN)

## The skill + MCP pattern (EVERGREEN)

MCP and Skills solve different problems and complement each other. An **MCP**
gives Claude the **capability** to access a service (the data, the actions). A
**skill** (Level 5) gives Claude the **method**: when to use that capability, in
what order, with what rules.

Example: an MCP exposes your management software; a skill describes the workflow
"how to prepare the monthly report from the management software's data." The MCP
is the arm, the skill is the procedure. Together they make an integration not just
possible, but **repeatable**.

## In practice: connect a tool

1. First check the connector directory (ch. L3.3): if it's there, use that.
2. If it's not, obtain or write an MCP server for your tool.
3. Add it with `claude mcp add`, choosing `stdio` (local) or `http` (remote).
4. Pass credentials with `--env`, never in the clear.
5. If you use it recurrently, write a **skill** that describes its workflow.

## Common mistakes

- **Building an MCP that already exists.** Check the connector directory first.
- **Flags after the name.** They go before; the `--` separates them from the
  server's command. (VOLATILE)
- **Secrets in the clear.** Use `--env`/environment variables, don't write them in
  the command. (EVERGREEN)
- **MCP without a skill for repeated use.** The MCP gives the capability; the skill
  gives the method.

## Summary

1. **MCP** is the open standard that connects Claude to tools and data; an MCP
   server exposes a service's actions.
2. **Custom connectors** (ch. L3.3) are **remote MCPs**.
3. You need a custom MCP when no ready connector exists or for internal tools.
4. In Code: `claude mcp add` with `stdio` (local) or `http` (remote) transport.
5. **Skill + MCP**: the MCP gives the capability, the skill the repeatable method.

## Next step

In **ch. L6.3 — Automations and remote control** we'll see how to make Claude work
on its own over time: scheduled tasks, cloud routines, and control from your
phone.

---

*Data on MCP and `claude mcp add` verified on 24/06/2026 against
code.claude.com/docs/en/mcp and support.claude.com (custom connector). The
commands require Claude Code and an MCP server, so they were not run here.*
