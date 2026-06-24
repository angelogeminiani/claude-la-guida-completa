# Capitolo L3.2 — Projects

> Livello 3 — Lavoro quotidiano.
> Dati di prodotto verificati il 22/06/2026 su fonti ufficiali.

## Obiettivo

Al termine saprai cos'è un Project, quando conviene crearne uno, come dargli
istruzioni e file di riferimento che restano tra una conversazione e l'altra, e
cosa cambia quando lavori in team. Useremo come esempio il Project con cui è
stato scritto questo libro.

## Prerequisiti

- Saper conversare in chat (vedi cap. L1.2).
- Un'attività ricorrente: qualcosa su cui torni più volte, non una domanda
  secca.

## Cos'è un Project (VOLATILE)

Un Project è un **workspace** dedicato a un'attività: raccoglie in un posto solo
le istruzioni che valgono sempre, i file di riferimento (la "knowledge base") e
le conversazioni collegate. Ogni chat aperta dentro il Project parte già con
quel contesto, senza che tu lo ripeta.

Li avevi già incontrati di sfuggita tra le impostazioni (cap. L1.3): qui li
mettiamo al lavoro. I Project sono disponibili su tutti i piani; nel **Free**
sono limitati a **5**. La condivisione in team è riservata a **Team ed
Enterprise** (vedi il ledger). (VOLATILE)

## Quando crearne uno (EVERGREEN)

Non tutto merita un Project. La singola domanda sta bene in una chat normale.
Conviene creare un Project quando ricorrono questi segnali:

- **Torni più volte** sullo stesso lavoro nel tempo.
- **Ripeti lo stesso contesto** a ogni chat ("ricordati che lo stile è...").
- **Hai file di riferimento** che servono in ogni conversazione.

Se ti ritrovi a incollare le stesse istruzioni o gli stessi documenti all'inizio
di ogni chat, è il momento del Project.

## Istruzioni e knowledge base (EVERGREEN)

Due cose rendono utile un Project:

- **Istruzioni:** valgono per ogni chat del Project. Tono, vincoli, formato,
  cose da fare e da non fare. È il "chi sei e come lavori" del progetto.
- **Knowledge base:** i file che Claude può consultare — documenti, esempi,
  materiale di riferimento. Diventano parte del contesto disponibile.

La differenza con `CLAUDE.md` (cap. L2.4) è il contesto d'uso: `CLAUDE.md`
governa Claude Code sui file del progetto; le istruzioni del Project governano
le **conversazioni** dentro quel Project. Stessa idea — scrivi una volta il
contesto stabile — applicata a strumenti diversi.

> **Nota:** i file della knowledge base hanno un limite per file (intorno ai
> 30 MB) ma numero non vincolato, purché il contenuto stia nel contesto di
> Claude. È un limite diverso da quello degli allegati in chat (cap. L1.1): la
> knowledge base è pensata per molti file di riferimento, non per pochi file
> enormi. (VOLATILE)

## Memoria e scope (EVERGREEN)

Il Project dà ai tuoi lavori un confine. Le istruzioni e i file restano
**circoscritti** a quel Project: non si mescolano con le altre chat. Questo è un
vantaggio doppio — il contesto giusto è sempre lì, e quello sbagliato resta
fuori. Quando cambi attività, cambi Project, e il modello non trascina dietro
materiale che non c'entra.

## Esempio: il Project di questo libro (EVERGREEN)

Questo manuale è stato scritto dentro un Project. La sua forma mostra bene il
pattern:

- **Istruzioni:** regole di progetto — dove salvare i capitoli, niente note
  prudenziali nei testi pubblicati, voce e vincoli di impaginazione.
- **Knowledge base:** il piano editoriale, il ledger dei fatti, i file di
  contesto su voce e pubblico.
- **Conversazioni:** una per blocco di capitoli, tutte già allineate alle stesse
  regole senza ripeterle.

Risultato: ogni sessione di scrittura parte sapendo com'è fatto il libro. È la
differenza tra spiegare il progetto da capo ogni volta e averlo scritto una
volta sola.

## In pratica: crea il tuo Project

1. In Claude, apri la sezione **Projects** e creane uno nuovo.
2. Dagli un nome che dice di cosa si tratta.
3. Scrivi le **istruzioni**: il contesto stabile, i vincoli, il formato che
   vuoi.
4. Carica nella **knowledge base** i file di riferimento ricorrenti.
5. Apri una chat dentro il Project e lavora: il contesto è già attivo.
6. Quando una regola si ripete in più chat, spostala nelle istruzioni del
   Project.

## Errori comuni

- **Un Project per ogni chat.** Sono per il lavoro ricorrente, non per la
  domanda singola. Troppi Project diventano disordine.
- **Istruzioni-fiume.** Vale come per `CLAUDE.md`: poco e mirato. L'eccesso si
  diluisce.
- **Knowledge base obsoleta.** I file di riferimento invecchiano. Aggiornali, o
  Claude lavora su materiale vecchio.
- **Aspettarsi la condivisione nel Free/Pro.** Condividere un Project in team è
  da Team/Enterprise. (VOLATILE)

## Riepilogo

1. Un Project è un workspace con istruzioni, file di riferimento e chat
   collegate, tutto in un posto.
2. Crealo quando torni più volte su un lavoro e ripeti lo stesso contesto.
3. Le istruzioni valgono per ogni chat del Project; la knowledge base è il
   materiale che Claude consulta.
4. Lo scope tiene dentro il contesto giusto e fuori quello che non c'entra.
5. Free fino a 5 Project; condivisione in team su Team/Enterprise. (VOLATILE)

## Prossimo passo

Nel **cap. L3.3 — Connettori** colleghiamo Claude alle app che già usi — Drive,
Slack, gestori di task — così può leggere i tuoi dati e agire al loro interno.

---

*Dati sui Project (limiti Free, condivisione team) dal ledger, verificati il
22/06/2026 su support.claude.com. L'esempio del Project di questo libro è reale;
i passaggi operativi non sono stati eseguiti in questa sede.*
