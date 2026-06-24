# Capitolo L6.1 — Claude Code avanzato

> Livello 6 — Avanzato.
> Dati di prodotto verificati il 24/06/2026 su fonti ufficiali.

## Obiettivo

Al termine conoscerai tre leve avanzate di Claude Code: gli **hooks** per
agganciare i tuoi comandi agli eventi, i **sub-agent** per delegare compiti a
contesti separati, e i **permessi** granulari. Sono gli strumenti che trasformano
Claude Code da assistente a parte integrata del tuo flusso.

## Prerequisiti

- Claude Code installato e un progetto configurato (cap. L2.2, L2.4).
- A tuo agio con `settings.json` e i permessi base (cap. L2.4).

## Hooks: agganciare comandi agli eventi (VOLATILE)

Un **hook** è un comando shell che Claude Code esegue automaticamente in
corrispondenza di un **evento** del suo ciclo di vita: prima di usare un tool,
dopo, all'invio di un prompt, e così via. Servono a imporre regole che non vuoi
affidare alla buona volontà: lanciare il linter dopo ogni modifica, bloccare la
scrittura su certi file, registrare cosa è successo.

Si configurano in `settings.json`, organizzati per **matcher** (il nome del tool,
una regex, o vuoto per tutti). Gli eventi principali sono `PreToolUse` (prima
della chiamata a un tool) e `PostToolUse` (dopo).

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

### La trappola dell'exit code (VOLATILE)

Il punto che fa inciampare tutti è il **codice di uscita** dell'hook. Non è un
dettaglio: cambia il comportamento di Claude.

- **exit 0:** tutto ok, si prosegue.
- **exit 2:** errore **bloccante**. Lo stdout viene ignorato; lo **stderr** torna
  a Claude come messaggio d'errore. Su `PreToolUse`, la chiamata al tool è
  bloccata.
- **altri codici != 0:** errore **non** bloccante, mostrato a te.

Quindi, se vuoi che un hook **fermi** un'azione e spieghi a Claude perché, devi
uscire con **exit 2** e scrivere il motivo su **stderr**. Sbagliare codice è la
causa più comune di hook che "non bloccano".

## Sub-agent: delegare a un contesto separato (VOLATILE)

Un **sub-agent** è un assistente specializzato che Claude Code interpella per un
compito, con un **proprio context window**, un proprio system prompt e propri
permessi sui tool. Serve a isolare un lavoro (per esempio una revisione del
codice) senza ingombrare la conversazione principale.

Si definisce come file Markdown con frontmatter in `.claude/agents/` (di progetto)
o `~/.claude/agents/` (personale). Claude decide a quale sub-agent delegare
leggendo la `description`, come per le Skills.

```markdown
---
name: code-reviewer
description: Rivede le modifiche per qualità
  e correttezza. Usalo prima del commit.
tools: Read, Grep, Glob
---

Sei un revisore attento. Cerca errori di
logica, casi limite e problemi di leggibilità.
```

> **Tip:** il comando `/agents` ti guida nella creazione di un sub-agent e può
> generarne una prima bozza da una descrizione.

## Permessi granulari (EVERGREEN)

I permessi base (`allow`/`deny`, cap. L2.4) decidono cosa Claude può fare senza
chiedere. Gli hooks alzano il controllo: un `PreToolUse` può **valutare** la
singola azione e decidere a runtime se permetterla, negarla o chiedere conferma.
Così passi da regole statiche ("mai `rm -rf`") a regole dinamiche ("blocca la
scrittura fuori da `src/`"). Il principio resta quello del cap. L2.4: concedi il
ripetitivo e sicuro, presidia il distruttivo.

## In pratica: un hook che blocca

1. Apri `.claude/settings.json`.
2. Aggiungi un hook `PreToolUse` con il matcher del tool da sorvegliare.
3. Nel comando, controlla la condizione; se va bloccata, scrivi il motivo su
   stderr ed esci con **exit 2**.
4. Avvia Claude Code e prova un'azione che deve essere bloccata.
5. Verifica che Claude riceva il messaggio e si fermi.

## Errori comuni

- **Hook che non blocca.** Manca l'**exit 2**: con altri codici l'azione prosegue.
  (VOLATILE)
- **Messaggio dove non serve.** Su un blocco, scrivi su **stderr**, non stdout:
  lo stdout viene ignorato. (VOLATILE)
- **Sub-agent senza description chiara.** Claude non sa quando delegargli il
  compito: cura la `description`.
- **Permessi troppo larghi.** Aprire tutto annulla la rete di sicurezza (cap.
  L2.4).

## Riepilogo

1. Gli **hooks** eseguono tuoi comandi sugli eventi di Claude Code, da
   `settings.json` per matcher.
2. La **trappola dell'exit code**: solo **exit 2** blocca, e il motivo va su
   **stderr**.
3. I **sub-agent** delegano un compito a un contesto separato; Claude sceglie in
   base alla `description`.
4. I permessi granulari: gli hooks valutano a runtime cosa permettere.
5. Filosofia invariata: concedi il sicuro, presidia il distruttivo.

## Prossimo passo

Nel **cap. L6.2 — MCP custom** vediamo come collegare a Claude ciò che non ha già
un connettore pronto, e il pattern che unisce una skill a un server MCP.

---

*Dati su hooks, sub-agent e permessi verificati il 24/06/2026 su
code.claude.com/docs (hooks, sub-agents). Gli esempi di configurazione non sono
stati eseguiti in questa sede.*
