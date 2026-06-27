# Chapter L6.5 — Claude at work, safely

> Level 6 — Advanced.
> Product details verified on 24/06/2026 against official sources.

## Goal

By the end you'll know what changes when Claude enters an organization: who governs
the capabilities, how roles and data are managed, and why a personal account isn't
the right choice for business work. This is the chapter that separates individual
use from team use.

## Prerequisites

- Knowing the plans (ch. F.3) and connectors (ch. L3.3).

## Personal or company account (EVERGREEN)

The first decision is also the most important: for the organization's work you use
an account **managed by the organization** (Team or Enterprise), not a personal
one. The reason isn't a formality. On a company account the data, the access, and
the rules are controlled by whoever administers it; on a personal one they stay in
the hands of the individual, outside the company's policies. Putting work material
on a personal account means taking it outside the perimeter the organization can
protect and manage.

## Who governs the capabilities (VOLATILE)

In Team and Enterprise not everything is on for everyone. An **Owner** or **Primary
Owner** decides what's available, from **Admin > Capabilities**: Web search,
connectors, and other functions are enabled at the organization level. So if you
don't see a function, it's often not an error: it's a choice by whoever administers
the account (we already saw this for Web search in ch. L1.3 and for connectors in
ch. L3.3).

The same goes for **connector actions**: an admin can allow read-only and block
writes, for the entire organization (ch. L3.3).

## Roles, identity, and data (VOLATILE)

Organizations need controls that a single account doesn't have. The table sums up
what the business plans add.

Table L6.5.1 — Controls for organizations.

Each column is additive: Enterprise includes what Team has, and adds to it.

| Area | Team | Enterprise (extra) |
|---|---|---|
| Access | admin, SSO | RBAC, SCIM |
| Data | no training* | retention, audit log |
| Network | — | IP allowlisting |

*On both Team and Enterprise, by default data isn't used for training; Enterprise
adds retention and audit log. (VOLATILE)

In short: **Team** brings administration, SSO (single sign-on), and controlled
deployment; **Enterprise** adds granular roles (RBAC), automatic user provisioning
(SCIM), audit log, data retention management, IP allowlisting, and dedicated
security features. These are the tools that make use compliant with company
policies, not left to the individual.

## The permission model, again (EVERGREEN)

One principle runs through the whole book: Claude **inherits your permissions**. It
holds for connectors (it sees only what you see at the source, ch. L3.3) and for
file work (it touches only the connected folders, ch. L3.1). In a company this is a
guarantee: the controls of the source system stay in force, and Claude doesn't
override them. Restricting in Claude never grants more access than the source
allows.

## In practice: introducing Claude into a company

1. Use an account **managed by the organization**, not a personal one.
2. Have an Owner define the available **capabilities** (Admin > Capabilities).
3. Set up **access**: SSO and, in Enterprise, roles (RBAC) and provisioning (SCIM).
4. Configure **connector restrictions** based on what the team can read or modify
   (ch. L3.3).
5. Agree on the rules for **data** and retention before putting in sensitive
   material.

## Common mistakes

- **Business work on a personal account.** It takes data outside the
  organization's control: use the managed account.
- **Thinking it's a bug when a function is missing.** Often an admin has disabled
  it (ch. L1.3, L3.3).
- **Connectors without restrictions.** In a team, define what's read-only and what
  isn't (ch. L3.3).
- **Postponing the data rules.** Agree on them first, not after uploading sensitive
  material.

## Summary

1. For business work use an account **managed by the organization**, not a personal
   one.
2. An **Owner** governs the capabilities from **Admin > Capabilities**.
3. **Team** adds admin and SSO; **Enterprise** adds RBAC, SCIM, audit log,
   retention, IP allowlisting.
4. Claude **inherits permissions**: the source's controls stay in force.
5. Define access, connector restrictions, and data rules before you start.

## Next step

In **ch. L6.6 — Integrating via API** we close the technical level: how to move
from interfaces to code, with the messages endpoint and a first example.

---

*Data on Team/Enterprise controls (RBAC, SCIM, SSO, audit, retention) verified on
24/06/2026 against claude.com/pricing and support.claude.com. Independent
publication, not affiliated with Anthropic.*
