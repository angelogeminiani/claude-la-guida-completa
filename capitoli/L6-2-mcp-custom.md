# Capitolo L6.2 — MCP custom

> Livello 6 — Avanzato.
> Dati di prodotto verificati il 24/06/2026 su fonti ufficiali.

## Obiettivo

Al termine capirai cos'è MCP in parole semplici, quando serve un server MCP custom
invece di un connettore pronto, come aggiungerne uno a Claude Code, e il pattern
che combina una skill con un MCP. È il modo per collegare Claude a ciò che non ha
già un'integrazione.

## Prerequisiti

- Aver usato i connettori (cap. L3.3).
- Claude Code installato (cap. L2.2), per la parte pratica.

## Cos'è MCP, in parole semplici (EVERGREEN)

**MCP** (Model Context Protocol) è uno **standard aperto** per collegare Claude a
strumenti e dati esterni. Pensa a una presa elettrica universale: invece di
un'integrazione su misura per ogni app, MCP definisce un modo comune perché Claude
parli con un servizio. Un **server MCP** è il componente che espone a Claude le
azioni di quel servizio.

I connettori del cap. L3.3 sono già MCP sotto il cofano: un **custom connector** è
un **remote MCP** (un server raggiungibile via rete). MCP è dunque il livello
tecnico che sta sotto ai connettori.

## Quando serve un MCP custom (EVERGREEN)

La directory dei connettori copre le app più diffuse. Un MCP custom serve quando:

- l'app che ti serve **non ha un connettore** pronto;
- vuoi collegare un tuo **strumento interno** o un database aziendale;
- ti serve un'azione specifica che nessun connettore esistente offre.

In breve: prima cerchi nella directory; se non c'è, costruisci o colleghi un MCP.

## Locale o remoto (VOLATILE)

Un server MCP può girare in due modi, e Claude Code li gestisce entrambi.

Tabella L6.2.1 — MCP locale e remoto a confronto.

| Tipo | Dove gira | Come |
|---|---|---|
| Locale (stdio) | sul tuo computer | child process |
| Remoto (HTTP) | su un server | via rete |

Il **locale** (transport `stdio`) viene avviato da Claude Code come processo
figlio, che comunica su standard input/output: utile per strumenti che vivono
sulla tua macchina. Il **remoto** (transport `http`) è un server raggiungibile via
rete: è la forma dei custom connector, raggiunti dal cloud di Anthropic (cap.
L3.3).

## Aggiungere un MCP a Claude Code (VOLATILE)

Dal terminale, il comando base è `claude mcp add`. Per un server locale:

```bash
claude mcp add --transport stdio \
  mio-tool -- npx -y mio-mcp-server
```

I flag (`--transport`, `--env`, `--scope`) vanno **prima** del nome; il `--`
separa il nome dal comando che avvia il server. Le variabili d'ambiente si passano
con `--env` (per esempio una API key del servizio).

> **Attenzione:** un MCP custom dà a Claude accesso a un servizio esterno. Collega
> solo server di cui ti fidi e non mettere segreti in chiaro: usa le variabili
> d'ambiente. (EVERGREEN)

## Il pattern skill + MCP (EVERGREEN)

MCP e Skills risolvono problemi diversi e si completano. Un **MCP** dà a Claude la
**capacità** di accedere a un servizio (i dati, le azioni). Una **skill** (Livello
5) dà a Claude il **metodo**: quando usare quella capacità, in che ordine, con
quali regole.

Esempio: un MCP espone il tuo gestionale; una skill descrive il workflow «come
preparare il report mensile dai dati del gestionale». L'MCP è il braccio, la skill
è la procedura. Insieme rendono un'integrazione non solo possibile, ma
**ripetibile**.

## In pratica: collega uno strumento

1. Verifica prima nella directory dei connettori (cap. L3.3): se c'è, usa quello.
2. Se non c'è, procurati o scrivi un server MCP per il tuo strumento.
3. Aggiungilo con `claude mcp add`, scegliendo `stdio` (locale) o `http` (remoto).
4. Passa le credenziali con `--env`, mai in chiaro.
5. Se l'uso è ricorrente, scrivi una **skill** che ne descrive il workflow.

## Errori comuni

- **Costruire un MCP che esiste già.** Controlla prima la directory dei
  connettori.
- **Flag dopo il nome.** Vanno prima; il `--` separa dal comando del server.
  (VOLATILE)
- **Segreti in chiaro.** Usa `--env`/variabili d'ambiente, non scriverli nel
  comando. (EVERGREEN)
- **MCP senza skill per l'uso ripetuto.** L'MCP dà la capacità; la skill dà il
  metodo.

## Riepilogo

1. **MCP** è lo standard aperto che collega Claude a strumenti e dati; un server
   MCP espone le azioni di un servizio.
2. I **custom connector** (cap. L3.3) sono **remote MCP**.
3. Serve un MCP custom quando non esiste un connettore pronto o per strumenti
   interni.
4. In Code: `claude mcp add` con transport `stdio` (locale) o `http` (remoto).
5. **Skill + MCP**: l'MCP dà la capacità, la skill il metodo ripetibile.

## Prossimo passo

Nel **cap. L6.3 — Automazioni e controllo remoto** vediamo come far lavorare
Claude da solo nel tempo: task pianificati, routine cloud e comando dal telefono.

---

*Dati su MCP e `claude mcp add` verificati il 24/06/2026 su
code.claude.com/docs/en/mcp e support.claude.com (custom connector). I comandi
richiedono Claude Code e un server MCP, quindi non sono stati eseguiti in questa
sede.*
