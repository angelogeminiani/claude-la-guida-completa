# Capitolo L6.4 — Gestire i limiti d'uso

> Livello 6 — Avanzato.
> Dati di prodotto verificati il 27/06/2026 su fonti ufficiali.

## Obiettivo

Al termine capirai la differenza tra **usage limit** e **length limit**, da cosa
dipende il consumo, e come lavorare a lungo senza sbattere contro i limiti. Sono le
nozioni che ti fanno usare Claude in modo sostenibile, soprattutto su task pesanti.

## Prerequisiti

- Conoscere i piani (cap. F.3) e i Project (cap. L3.2).

## Due limiti diversi (VOLATILE)

Claude ha due tipi di limite, che funzionano in modo distinto:

- **Usage limit:** *quanto* puoi usare Claude in un periodo. È il tuo "budget di
  conversazione". Al suo esaurirsi, aspetti il reset.
- **Length limit:** *quanto* può diventare lunga una singola chat, cioè il
  **context window** (la memoria di lavoro di Claude in quella conversazione).

Il primo riguarda la quantità nel tempo; il secondo la profondità di una singola
chat. Confonderli porta alle scelte sbagliate quando qualcosa si "blocca".

## Da cosa dipende il consumo (VOLATILE)

L'usage non si consuma a colpi fissi. Pesano più fattori: la **lunghezza e
complessità** della conversazione, le **feature** attive, il **modello** scelto e
l'**effort level** (quanto a fondo ragiona). Un dettaglio che sorprende: tutte le
superfici — claude.ai, Claude Code, Claude Desktop — attingono allo **stesso**
usage. Non sono budget separati.

> **Nota:** con la Code execution attiva, le chat lunghe innescano la **gestione
> automatica del contesto**: Claude riassume i messaggi più vecchi per proseguire.
> Comodo, ma le conversazioni lunghe consumano **più** usage. (VOLATILE)

## Il context window (VOLATILE)

Nella chat, sui piani a pagamento, il context window è di **500K token** per i
modelli di punta (Opus 4.6/4.7/4.8 e Sonnet 4.6) e di **200K** per gli altri. In
**Claude Code** i modelli di punta arrivano fino a **1M token**: su Pro, per il
milione, vanno abilitati gli usage credits. Non puoi ingrandirlo a piacere, ma puoi
usarlo meglio: è lì che si gioca la differenza tra una chat che regge e una che si
satura.

## Task economici: ridurre il consumo (EVERGREEN)

Alcune mosse abbassano il consumo a parità di risultato:

- **Usa i Project.** Sfruttano il RAG (recupero mirato): caricano in contesto solo
  ciò che serve, invece di tutto.
- **Istruzioni brevi.** Project e prompt concisi pesano meno e rendono di più.
- **Togli ciò che non serve.** File inutili nei Project, e **tool/connettori** non
  necessari: sono token-intensive, spegnili quando non servono.
- **Abbassa l'effort** e disattiva l'**extended thinking** sui task di routine.
- **Scegli il modello giusto.** Non usare il più potente "per sicurezza" (cap.
  F.3): spesso paghi di più senza vantaggi.

## Cosa fare al limite (EVERGREEN)

Quando sbatti contro un limite, la mossa dipende da quale:

- **Usage limit raggiunto:** aspetti il **reset**, fai **upgrade** di piano, o
  compri **usage credits** (sui piani a pagamento) per continuare subito.
- **Length limit (chat troppo lunga):** apri una **nuova conversazione**, o sposta
  il materiale in un **Project** per lavorarci in modo più efficiente.

> **Tip:** se sei in una chat lunga e vicino al limite d'uso, conviene spesso
> ricominciare in una chat nuova: riparti con il contesto essenziale invece di
> trascinarti dietro tutto lo storico.

## In pratica: lavora a lungo senza bloccarti

1. Per un lavoro ricorrente, mettilo in un **Project** invece di chat infinite.
2. Tieni istruzioni brevi e rimuovi i file che non usi più.
3. Disattiva tool e connettori non necessari per quella sessione.
4. Sui task semplici, abbassa l'effort e spegni l'extended thinking.
5. Se ti avvicini al limite in una chat lunga, **aprine una nuova**.

## Errori comuni

- **Confondere i due limiti.** Se è la chat a essere piena, non serve aspettare il
  reset: apri una chat nuova.
- **Tenere tutto acceso.** Tool e connettori inutili consumano contesto e usage:
  spegnili. (VOLATILE)
- **Modello sovradimensionato.** Più potenza del necessario costa di più senza
  resa migliore.
- **Chat infinite.** Trascinare uno storico enorme consuma usage: spezza in chat o
  usa i Project.

## Riepilogo

1. **Usage limit** = quanto usi nel tempo; **length limit** = quanto è lunga una
   chat (context window).
2. Il consumo dipende da lunghezza, feature, **modello** ed **effort**; tutte le
   superfici contano sullo **stesso** usage.
3. Context window in chat: **500K** per i modelli di punta, **200K** per gli
   altri; in Claude Code fino a **1M** (con usage credits su Pro).
4. Riduci il consumo con Project, istruzioni brevi, meno tool attivi, effort più
   basso.
5. Al limite: reset/upgrade/**credits** per l'usage; **nuova chat**/Project per la
   lunghezza.

## Prossimo passo

Nel **cap. L6.5 — Claude al lavoro, sicuro** vediamo come introdurre Claude in
un'organizzazione: governance, ruoli, dati e quando non usare l'account personale.

---

*Dati su usage/length limit e context window verificati il 27/06/2026 su
support.claude.com/en/articles/11647753 e /articles/8606394. Valori soggetti a
modifica: vedi il ledger e le fonti ufficiali per gli aggiornamenti.*
