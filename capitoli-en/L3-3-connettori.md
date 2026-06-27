# Chapter L3.3 — Connectors

> Level 3 — Daily work.
> Product details verified on 24/06/2026 against official sources.

## Goal

By the end you'll know what Connectors are, how to link one from the directory,
how to activate them in a conversation, and what precautions to keep in mind —
both as a user and, in a company, as an administrator.

## Prerequisites

- Knowing how to open a chat (see ch. L1.1) and use the tools menu (see ch.
  L1.3).
- An account on a service you want to connect (Drive, Slack, a task
  manager...).

## What connectors are (VOLATILE)

A connector gives Claude access to an app or service: reading your data and
**performing actions** inside it. It links Claude to Linear to open issues, to
Slack to send messages, to Google Drive to search your files.

The point to grasp clearly is the permission model: **Claude inherits your
permissions** in the connected service. If you can't see a given file, channel
or record at the source, the connector won't reach it from Claude. A connector
doesn't give you more access than you already have — it only brings it into the
conversation.

Web connectors are available to **all users** on Claude, Cowork, Desktop and
Mobile; they also work with Claude Code and via API. (VOLATILE)

## The connectors directory (VOLATILE)

The available connectors live in the **Connectors Directory** (claude.ai/
connectors). Each connector has a card with use cases, read/write capabilities
and availability. Some carry the **Interactive** badge: they render live
interfaces — dashboards, boards, tools — inside the conversation.

Open the directory in two ways:

- **From a chat:** the **"+"** button (or "/") > "Connectors" > "Manage
  connectors" > "+".
- **From settings:** **Customize > Connectors** > "+".

## Connecting and activating a service (VOLATILE)

Connecting a service and using it are two distinct steps.

**Connecting** (once): from the directory, click the connector, review its
capabilities, "Connect"/"Install", follow the authentication prompts (usually
OAuth, meaning you authorize Claude from the service's site), configure the
permissions.

**Activating** (per conversation): "+" (or "/") > "Connectors", then toggle on
the services you want for that chat. From there Claude uses them when relevant —
and it can propose them on its own, without you having to name them every time.

> **Tip:** if you have many connectors, from "Connectors" > "Tool access" choose
> how they load. The default **Auto** is fine for almost everyone; with 10 or
> more active connectors, **On demand** leaves more room for the conversation.

## In a company: the admin's role (VOLATILE)

On **Team and Enterprise** a connector isn't usable until an **Owner** or
**Primary Owner** enables it for the organization (Organization settings >
Connectors > "Browse connectors" > "Add to your team"). Enabling does **not**
give anyone access: everyone still authenticates on their own.

The admin can also **restrict the actions** of a connector for the whole org.
From Customize > Connectors, on the connector, the **Tool permissions** are
split by type (read-only, write/delete) and for each you choose *Always allow*,
*Needs approval* or *Blocked*. It applies to everyone and can't be bypassed by
an individual.

Table L3.3.1 — Examples of action restrictions.

| Service | Allow | Block |
|---|---|---|
| Email | Search and summarize | Send messages |
| Drive | Read files | Create/edit |
| Linear | View issues | Create or change them |

These restrictions work **together** with the service's permissions: even where
Claude can write, you still need permission at the source. Restricting in Claude
never grants more than the source system allows — at most it restricts.

## Precautions (EVERGREEN)

- **Connect only what you trust and what you need.** Linking a service means
  giving Claude access to your data in it.
- **Review the requested access** during connection, and **disconnect** what you
  no longer use (Customize > Connectors).
- **Custom connector = not verified by Anthropic.** You can add custom
  connectors (remote MCP), but only connect servers from trusted organizations.
  We go into custom connectors in detail at Level 6 (ch. L6.2).
- **Team/Enterprise:** connectors only work in private Projects, and chats with
  synced content can't be shared.

## In practice: connect Google Drive

1. In chat, "+" (or "/") > "Connectors" > "Manage connectors" > "+".
2. Search for the connector in the directory and open it.
3. Read the capabilities, then "Connect" and authorize with your account
   (OAuth).
4. Go back to chat, "+", "Connectors", and toggle on the service.
5. Try it:

   ```text
   Search my Drive for the March quote
   and summarize the main line items for me.
   ```

## Common mistakes

- **"I connected it but it isn't using it."** Connecting isn't enough: toggle it
  on in the chat's "Connectors" menu.
- **Expecting access to everything.** Claude only sees what you see in the
  service.
- **(Team) "The connector isn't there."** An Owner must enable it for the org
  first; then you authenticate.
- **Custom connector that times out.** The MCP server is reached from
  Anthropic's cloud, not from your device: it must be on the public internet
  (see ch. L6.2). (VOLATILE)

## Summary

1. A connector gives Claude access to an app to read data and act, **with your
   own permissions** at the source.
2. Connectors live in the Connectors Directory; some are **Interactive**.
3. Connecting (OAuth, once) and activating (toggle, per conversation) are two
   distinct steps.
4. In Team/Enterprise an Owner enables the connector and can restrict its
   actions for the whole org.
5. Connect only what you trust, review the access, disconnect the useless.

## Next step

In **ch. L3.4 — Documents** we use Claude to generate professional files — Word,
PowerPoint, Excel, PDF — starting from the right content.

---

*Connector data (directory, OAuth, admin role, action restrictions) from the
ledger, verified on 24/06/2026 on support.claude.com/en/articles/11176164. The
operational steps were not executed here.*
