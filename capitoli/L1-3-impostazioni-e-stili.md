# Capitolo L1.3 — Impostazioni e stili

> Livello 1 — Fondamenti.
> Dati di prodotto verificati il 22/06/2026 su fonti ufficiali.

## Obiettivo

Al termine saprai configurare Claude perché risponda nel tuo tono e con le
capacità giuste, senza ripetere le stesse istruzioni a ogni chat. Vedremo le
preferenze d'account, gli Styles (stili) e le capacità Web search (ricerca web),
Code execution (esecuzione del codice) e Memory (memoria).

## Prerequisiti

- Saper avviare una conversazione (cap. L1.1).

## Istruzioni a livello di account (VOLATILE)

In **Settings → Instructions for Claude** imposti preferenze che valgono per
tutte le conversazioni: come ti chiami, in che lingua scrivere, il tono che
preferisci, termini ricorrenti del tuo lavoro. È il posto giusto per le cose
che diresti a ogni chat: scriverle una volta sola ti fa risparmiare tempo.

È diverso da un'istruzione data nella singola chat, che vale solo lì: queste
valgono ovunque. Esempi utili da mettere qui: «scrivi sempre in italiano»,
«preferisco risposte concise con esempi», «sono uno sviluppatore», «non usare
emoji». Tienile brevi e aggiornale quando le tue esigenze cambiano: è il livello
più comodo per le preferenze stabili.

## Stili di risposta (VOLATILE)

Gli **Styles** controllano *come* Claude comunica. Sono disponibili alcuni
preset — Normal, Concise (conciso), Formal (formale), Explanatory (esplicativo)
— e puoi crearne di personalizzati, anche caricando esempi della tua scrittura.
Li trovi nel menu "Search and tools" accanto alla casella di testo.

Quando usarli? **Concise** per risposte rapide e dense; **Explanatory** quando
stai imparando e vuoi più contesto; **Formal** per testi professionali. Lo stile
**custom** è il più potente: carichi alcuni tuoi testi e Claude ne imita registro
e ritmo. È il primo passo verso il «far suonare Claude come te», che approfondiamo
con le Skills nel Livello 5.

> **Attenzione:** gli Styles stanno evolvendo verso le Skills (vedi Livello 5).
> Funzioni e nomi potrebbero cambiare: è un'area volatile, verifica lo stato
> attuale nelle impostazioni.

## Le capacità da conoscere (VOLATILE)

Oltre al tono, puoi attivare capacità che ampliano ciò che Claude può fare. La
tabella le riassume; sotto, il dettaglio.

Tabella L1.3.1 — Capacità principali e disponibilità.

| Funzione | A cosa serve | Disponibilità |
|---|---|---|
| Web search | dati aggiornati | tutti i piani |
| Code execution | creare file | tutti i piani |
| Memory | ricorda lo storico | tutti i piani |
| Chat search | cerca chat passate | a pagamento |

**Web search.** Attiva la ricerca live sul web, con citazioni delle fonti. È
indispensabile per informazioni recenti, dove la conoscenza "a memoria" del
modello non basta. Si attiva dal pulsante "+" o dal menu strumenti. Consuma i
tuoi limiti d'uso. Su Team ed Enterprise va abilitata da un amministratore.
In pratica: chiedi «cerca le ultime notizie su X» e Claude porta risultati con i
link, così risali alla fonte. Senza, risponde con ciò che «sa» e su fatti recenti
può sbagliare.

**Code execution e creazione file.** Dà a Claude un ambiente sandbox per
eseguire codice e produrre file veri: Excel, PowerPoint, Word, PDF, grafici.
Serve anche per caricare file XLSX. È disponibile su tutti i piani, con un
limite indicativo di ~30 MB per file. È ciò che permette richieste come «crea un
Excel con queste spese e un grafico a torta»: Claude scrive il file e te lo
restituisce pronto da scaricare.

**Memory e ricerca nelle chat.** La **Memory** crea una sintesi del tuo storico,
così Claude costruisce sul contesto passato; è disponibile su tutti i piani.
La **ricerca nelle chat passate** è invece riservata ai piani a pagamento. Le
conversazioni in incognito (icona fantasma) restano escluse da entrambe.

## Privacy e controllo dei dati (EVERGREEN)

Tre cose da tenere a mente. Le chat in **incognito** non finiscono nello storico
né nella Memory: usale quando non vuoi lasciare traccia. La **Memory** è una
sintesi, non una copia fedele: se un dato è importante, ripetilo nella chat invece
di confidare che sia stato ricordato. Infine, su **Team** ed **Enterprise** alcune
capacità le abilita un amministratore da *Admin → Capabilities*: se non le vedi,
non è un errore tuo, chiedi a chi gestisce l'organizzazione.

> **Tip:** non devi attivare tutto subito. Parti da Web search e Code execution:
> coprono la gran parte dei casi quotidiani; il resto lo aggiungi quando serve.

## Projects, in due parole (VOLATILE)

Un **Project** è uno spazio di lavoro con una sua knowledge base e istruzioni
dedicate, condivise tra le chat di quel progetto. È utile quando lavori a lungo
sullo stesso tema. Gli utenti Free possono crearne fino a cinque; la
condivisione è riservata a Team ed Enterprise. Li approfondiamo nel cap. L3.2.

## Preferenze, Styles o Projects? (EVERGREEN)

Si sovrappongono, ma servono a scopi diversi. Le **Instructions for Claude** sono
preferenze personali valide ovunque. Gli **Styles** cambiano il modo di comunicare
e li attivi all'occorrenza. Un **Project** isola contesto e istruzioni per un tema
o un cliente specifico, senza inquinare le altre chat. Regola pratica: preferenze
stabili → Instructions; come scrivere → Styles; un lavoro a sé → Project.

Esempio concreto: per scrivere questo libro potresti tenere un Project con le
regole di stile e i capitoli già pronti, così ogni nuova chat parte già «sul
pezzo» senza ripetere il contesto.

> **Nota:** le impostazioni viste qui sono personali. In un'organizzazione,
> alcune scelte (sicurezza, uso dei dati per il training) le definisce
> l'amministratore: il tuo account eredita quelle regole.

## In pratica: configura il tuo Claude

1. Apri **Settings → Instructions for Claude** e scrivi nome, lingua e tono.
2. Scegli uno **stile** dal menu "Search and tools" (prova Concise).
3. Attiva **Web search** e fai una domanda su un fatto recente.
4. In **Settings → Capabilities**, verifica che **Code execution** sia attiva.
5. Controlla le impostazioni di **Memory** e decidi se tenerla attiva.
6. Se sei in un'organizzazione, verifica in **Admin → Capabilities** cosa è
   abilitato sul tuo account.

## Errori comuni

- **Ripetere le stesse istruzioni a ogni chat.** Mettile una volta in
  "Instructions for Claude".
- **Dimenticare Web search sui fatti recenti.** Senza, Claude risponde "a
  memoria" e può sbagliare date o numeri.
- **Aspettarsi un file Excel senza Code execution.** Va attivata, altrimenti
  niente generazione di file.
- **Confidare nella Memory per tutto.** È una sintesi, non un archivio preciso:
  per dati importanti, riportali nella chat.
- **Pensare a un bug quando manca una funzione.** Su Team/Enterprise può averla
  disattivata l'amministratore: controlla in Admin → Capabilities.
- **Creare un Project per ogni domanda.** I Project servono ai lavori continui;
  per una richiesta isolata basta una chat normale.

## Riepilogo

1. **Instructions for Claude** applica le tue preferenze a ogni conversazione.
2. Gli **Styles** regolano il tono; stanno evolvendo verso le Skills.
3. **Web search** serve per i dati aggiornati e consuma usage.
4. **Code execution** abilita la creazione di file; **Memory** ricorda lo storico.
5. La **ricerca nelle chat** è solo a pagamento; l'incognito resta escluso.

## Prossimo passo

Hai completato i fondamenti. Nel **Livello 2** passiamo all'installazione locale:
si parte dal **cap. L2.1 — Installare Claude Desktop**.
