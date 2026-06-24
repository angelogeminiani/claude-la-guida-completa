# Capitolo C.2 — Appendici

> Chiusura — materiale di consultazione.
> Dati di prodotto verificati il 24/06/2026 su fonti ufficiali.

## Come usare queste appendici

Non si leggono in sequenza: si consultano. Trovi un glossario dei termini
ricorrenti, una tabella di troubleshooting per i problemi più comuni, e i link
ufficiali da cui verificare i dati volatili.

## Glossario (EVERGREEN)

- **Agentico:** modo di lavorare in cui Claude porta avanti un compito in più
  passi, non solo una risposta singola.
- **API:** accesso programmatico ai modelli, per integrare Claude nei propri
  software (cap. L6.6).
- **Canvas:** la tela di Claude Design dove appaiono le interfacce generate (cap.
  L4.1).
- **Connettore (Connector):** collegamento che dà a Claude accesso a un'app, con i
  tuoi permessi (cap. L3.3).
- **Context window:** la memoria di lavoro di una singola chat, misurata in token
  (cap. L6.4).
- **Cowork:** lavoro agentico non di codice nell'app desktop, in VM isolata (cap.
  L3.1).
- **Design / `/design-sync`:** il canvas e il comando che sincronizza design e
  codice nei due versi (cap. L4.3).
- **Dispatch:** avviare da telefono un task che Claude esegue sul tuo computer
  (cap. L6.3).
- **Effort level:** quanto a fondo Claude ragiona; più alto consuma più usage
  (cap. L6.4).
- **Handoff:** passaggio di un design a Claude Code perché diventi software (cap.
  L4.3).
- **Hook:** comando agganciato a un evento di Claude Code (cap. L6.1).
- **MCP:** standard aperto che collega Claude a strumenti e dati esterni (cap.
  L6.2).
- **Native installer:** metodo consigliato per installare Claude Code, senza Node
  (cap. L2.2).
- **OAuth:** accesso delegato via browser, senza digitare la password nel terminale
  (cap. L2.3).
- **Prompt:** la richiesta che scrivi a Claude (cap. L1.2).
- **Project:** workspace con istruzioni e knowledge base condivise tra le chat
  (cap. L3.2).
- **Routine:** automazione di Claude Code che gira sul cloud (cap. L6.3).
- **Scheduled Task:** task ricorrente di Cowork, gira a computer acceso (cap.
  L6.3).
- **Skill / `SKILL.md`:** conoscenza riutilizzabile che Claude carica da solo (cap.
  L5.1).
- **Sub-agent:** assistente con contesto e permessi propri, a cui Code delega (cap.
  L6.1).
- **Tool use:** uso, via API, di strumenti che fornisci tu (cap. L6.6).
- **Usage limit:** quanto puoi usare Claude in un periodo (cap. L6.4).
- **VM isolata:** macchina virtuale in cui gira Cowork; vede solo le cartelle
  collegate (cap. L3.1).

## Troubleshooting (VOLATILE)

Tabella C.2.1 — Problemi comuni e prima soluzione.

| Problema | Causa | Soluzione |
|---|---|---|
| `command not found` | PATH | nuovo terminale (L2.2) |
| Login fallito | API key di troppo | `unset` la key (L2.3) |
| Funzione assente | admin | Admin > Capabilities (L1.3) |
| Hook non blocca | exit code | usa exit 2 (L6.1) |
| Connettore inerte | non attivato | toggle in chat (L3.3) |
| Task saltato | PC spento | riapri l'app (L6.3) |
| Chat satura | length limit | nuova chat (L6.4) |

## Link ufficiali (VOLATILE)

Da qui verifichi i dati che cambiano nel tempo. Sono le uniche fonti su cui questo
libro si basa per i dettagli di prodotto.

- **claude.ai** — accesso a Claude (web).
- **claude.com** e **claude.com/pricing** — prodotti e piani.
- **support.claude.com** — guide e troubleshooting ufficiali.
- **code.claude.com/docs** — documentazione di Claude Code.
- **platform.claude.com/docs** — documentazione API e Console.
- **agentskills.io** — standard aperto delle Skills.
- **github.com/anthropics/skills** — skill di esempio.

## Note legali (EVERGREEN)

Pubblicazione **indipendente, non affiliata né approvata da Anthropic**. Claude e
Anthropic sono marchi dei rispettivi titolari. I dati di prodotto (versioni,
comandi, prezzi, menu, piani) sono **verificati alla data indicata** in ciascun
capitolo e nel ledger, e sono **soggetti a modifica**: per i valori correnti fai
riferimento alle fonti ufficiali sopra e al repo companion.

## Riepilogo

1. Il **glossario** raccoglie i termini ricorrenti, con il rimando al capitolo.
2. La tabella di **troubleshooting** dà la prima mossa per i problemi comuni.
3. I **link ufficiali** sono le sole fonti per i dati volatili.
4. La pubblicazione è **indipendente** e non affiliata ad Anthropic.
5. I dati sono verificati alla data indicata e vanno ricontrollati alle fonti.

## Fine

Hai attraversato tutto il percorso: dai primi messaggi in chat fino alle API e
all'automazione. Il prodotto continuerà a cambiare — per questo i dati volatili
sono datati e raccolti nel repo companion. Le idee di fondo, invece, restano:
descrivi il risultato, dai contesto, itera, e fai collaborare i pezzi
dell'ecosistema.

---

*Materiale di consultazione. Glossario e rimandi sono evergreen; troubleshooting,
link e dati di prodotto verificati il 24/06/2026 sulle fonti ufficiali elencate.*
