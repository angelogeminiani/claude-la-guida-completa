# Capitolo L4.2 — Design system import

> Livello 4 — Design.
> Dati di prodotto verificati il 24/06/2026 su fonti ufficiali.

## Obiettivo

Al termine saprai perché far partire Claude Design dal tuo brand invece che da
zero, da quali fonti importare un design system, cosa Claude ne estrae, e come
evitare l'output anonimo e generico — il cosiddetto "AI slop".

## Prerequisiti

- Aver usato il canvas (cap. L4.1).
- Avere almeno una fonte del tuo brand: un codebase, un deck, o asset grafici.

## Perché importare il brand (EVERGREEN)

Senza un design system, Claude genera con uno stile predefinito: corretto ma
neutro, riconoscibile come "fatto dall'IA". È il problema dell'**AI slop**:
risultati plausibili ma senza identità, che sembrano tutti uguali. La cura è dare
a Claude il tuo brand come fondamenta, così ogni schermata nasce con i tuoi
colori, font e componenti invece che con quelli di default.

Importare un design system è il passo che trasforma Design da generatore di bozze
generiche a strumento che produce materiale già "tuo".

## Cosa Claude estrae e da dove (VOLATILE)

Claude analizza le fonti che gli dai ed estrae un **design system riutilizzabile**:

- **Color palette:** colori primari, secondari e d'accento.
- **Tipografia:** famiglie di font, dimensioni, pesi.
- **Componenti:** bottoni, card, elementi di navigazione e altri pattern.
- **Layout:** spaziature, griglie, strutture di pagina.

Le fonti possibili sono più di una, e basta partire da una sola:

Tabella L4.2.1 — Fonti da cui importare e cosa danno.

| Fonte | Cosa contiene | Resa |
|---|---|---|
| Codebase | componenti reali | la più fedele |
| Deck / PDF | colori, layout | buona per il look |
| Asset di brand | logo, palette | base minima |

Un **codebase** (per esempio una libreria di componenti React) è la fonte più
ricca: Claude legge i componenti veri e li riusa. Un **deck** o un PDF ben fatti
bastano a estrarre colori e impaginazione. Anche solo logo e palette danno un
punto di partenza. Più fonti dai, più Claude ha da cui lavorare.

## Come si imposta (VOLATILE)

Configurare il design system è un'operazione da **brand owner o designer**, da
fare **una volta**: dopo, i progetti del team lo ereditano in automatico
(Team/Enterprise). I passaggi, in breve:

1. In Claude Design, seleziona o crea la tua **organizzazione**.
2. Carica gli **asset** del brand (codebase, deck, asset grafici).
3. Claude genera una **UI kit**: la rivedi creando un progetto di prova.
4. Quando ti soddisfa, attiva il **toggle "Published"**: da lì i nuovi progetti
   dell'org usano il tuo design system.

> **Nota:** in team, il ruolo **Claude Design Admin** permette di approvare un
> design system standard e bloccare le modifiche, così l'output resta sempre
> dentro le linee guida aziendali. (VOLATILE)

## Importare da Claude Code (VOLATILE)

Se il tuo design system vive nel codice, puoi importarlo **dal terminale** con il
comando `/design-sync` di Claude Code: porta il design system del codebase locale
dentro Design, così ogni schermata parte dai tuoi componenti reali. È il ponte
tra codice e canvas, che approfondiamo nel cap. L4.3.

## Ridurre l'AI slop (EVERGREEN)

L'import vale quanto la sua fonte: una codebase disordinata o un file incompleto
si vedono nell'output. Alcune mosse alzano la qualità:

- **Dai esempi reali, non solo specifiche.** Una landing page finita dice più di
  una palette di colori isolata: mostra il "sentire" del brand.
- **Itera sull'estrazione.** Se la prima resa non coglie il brand, carica asset
  diversi o aggiuntivi.
- **Nomina i componenti nel prompt.** «Usa il componente Primary Button» o
  «Applica il pattern Card» guida Claude verso il tuo sistema invece che verso
  un default.

## In pratica: porta il tuo brand

1. Raccogli la fonte migliore che hai: idealmente il codebase, altrimenti un deck
   curato.
2. Crea/seleziona l'organizzazione in Claude Design e carica gli asset.
3. Rivedi la UI kit generata con un progetto di test ("Crea una landing page per
   il nostro prodotto").
4. Se non coglie il brand, aggiungi asset e itera.
5. Attiva **Published** e verifica che i nuovi progetti usino il tuo stile.

## Errori comuni

- **Partire senza design system.** Ottieni l'AI slop: stile anonimo. Importa il
  brand prima.
- **Fonte disordinata.** Codebase confusa o file incompleto si riflettono
  nell'output: pulisci la fonte o scegline una migliore.
- **Solo specifiche, niente esempi.** Una palette da sola dice poco: aggiungi una
  pagina reale.
- **Non nominare i componenti.** Se sai che un componente esiste, chiamalo per
  nome nel prompt.

## Riepilogo

1. Senza design system l'output è anonimo (**AI slop**); importare il brand è la
   cura.
2. Claude estrae **colori, tipografia, componenti e layout** dalle fonti.
3. La fonte più fedele è un **codebase**; deck e asset danno una base.
4. Il setup è da brand owner, **una volta**: il team eredita il sistema.
5. L'import vale quanto la fonte: dai esempi reali e itera per ridurre l'AI slop.

## Prossimo passo

Nel **cap. L4.3 — Da Design a codice** percorriamo il ponte completo: il comando
`/design-sync` nei due versi e l'handoff a Claude Code che costruisce software
vero a partire dal canvas.

---

*Dati sull'import del design system (fonti, estrazione, setup, ruolo admin)
verificati il 24/06/2026 su support.claude.com/en/articles/14604397. Il setup
richiede un account a pagamento e non è stato eseguito in questa sede.*
