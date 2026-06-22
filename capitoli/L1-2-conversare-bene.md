# Capitolo L1.2 — Conversare bene

> Livello 1 — Fondamenti.
> Dati di prodotto verificati il 22/06/2026 su fonti ufficiali.

## Obiettivo

Al termine saprai scrivere richieste (prompt) che ottengono risposte utili al
primo colpo: chiare, con il contesto giusto e nel formato che ti serve. È
l'abilità che fa la differenza tra usare Claude e usarlo bene.

## Prerequisiti

- Aver mandato il primo messaggio (cap. L1.1).

## La regola d'oro (EVERGREEN)

Pensa a Claude come a un nuovo collaboratore: bravo, ma senza contesto sulle tue
abitudini. Se la tua richiesta confonderebbe una persona competente che non
conosce il tuo lavoro, confonderà anche Claude. Da qui derivano cinque principi
pratici.

Nessuno di questi principi richiede tecnicismi: sono lo stesso buon senso che
useresti delegando un compito a una persona. La differenza è che con Claude il
costo di riprovare è quasi nullo, quindi puoi permetterti di essere esplicito
senza timore di «chiedere troppo».

## 1. Sii chiaro e specifico (EVERGREEN)

Di' esplicitamente cosa vuoi, per chi e con quali vincoli. Indica lunghezza,
tono e formato dell'output. Quando l'ordine conta, usa passi numerati. "Scrivi
qualcosa sul prodotto" lascia troppo spazio; "Scrivi tre righe di descrizione
per il prodotto X, tono professionale, per un pubblico tecnico" guida la
risposta.

## 2. Dai contesto e motivazione (EVERGREEN)

Spiegare il perché di una richiesta aiuta Claude a centrarla. "Riassumi questo
report **per un dirigente che ha due minuti**" porta a un risultato diverso da
un riassunto generico. Il contesto non è un di più: è ciò che orienta le scelte.
Anche un vincolo, se posto in positivo, aiuta: invece di «non essere tecnico»,
scrivi «usa parole che capirebbe un cliente non del settore».

## 3. Usa esempi (EVERGREEN)

Mostrare uno o due esempi del risultato che vuoi è uno dei modi più affidabili
per guidare formato e tono. Se ti serve una scheda prodotto con una certa
struttura, incolla una scheda già fatta come modello. Tre-cinque esempi ben
scelti valgono più di mille spiegazioni.

## 4. Controlla il formato (EVERGREEN)

Di' cosa vuoi, non cosa non vuoi. "Rispondi con un elenco puntato di massimo
cinque voci" è meglio di "non essere prolisso". Se vuoi una tabella, chiedila;
se vuoi JSON o Markdown, specificalo. Dichiarare il formato fa risparmiare giri:
se ti serve una tabella a tre colonne o un elenco numerato, dillo subito invece
di riformattare dopo.

## 5. Itera (EVERGREEN)

La prima risposta è una bozza. Invece di ricominciare, correggi il tiro: "Più
breve", "Tono più informale", "Aggiungi un esempio concreto". Affinare in due o
tre passaggi è più rapido che cercare il prompt perfetto al primo tentativo.

## Dare ruolo, struttura e vincoli (EVERGREEN)

Oltre ai cinque principi, due mosse alzano la qualità sulle richieste complesse.

**Assegna un ruolo.** Indicare il punto di vista da cui rispondere orienta tono e
profondità: «Rispondi come un revisore di bilancio» o «Spiega come faresti a un
collega non tecnico». Non è un trucco scenico: restringe il campo delle risposte
plausibili a quelle che ti servono davvero.

**Struttura le richieste lunghe.** Quando una richiesta ha molte parti, separale:
un blocco per il contesto, uno per il compito, uno per il formato voluto. Anche
solo usare trattini o titoletti aiuta Claude a non perdere pezzi. Una richiesta
ordinata produce una risposta ordinata.

## Prima e dopo (EVERGREEN)

La tabella mostra come passare da una richiesta debole a una efficace. Il
principio è sempre lo stesso: aggiungere scopo, destinatario e formato.

Tabella L1.2.1 — Stesso intento, prompt debole e prompt migliore.

| Intento | Prompt debole | Prompt migliore |
|---|---|---|
| Email | "scrivi un'email" | "email breve, cliente, tono cortese" |
| Riassunto | "riassumi" | "5 punti per un dirigente di fretta" |
| Codice | "fai una funzione" | "funzione che valida un'email, con test" |

> **Tip:** se non sai da dove partire, scrivi prima l'obiettivo ("voglio
> ottenere…"), poi il contesto, infine il formato. Tre righe bastano.

## Un esempio completo (EVERGREEN)

Mettiamo insieme i principi su un caso reale. Parti da una richiesta d'istinto:

> Scrivimi un post per annunciare il nuovo prodotto.

È vaga: niente pubblico, niente canale, niente tono. Ecco la stessa richiesta
riscritta applicando scopo, destinatario e formato:

> Scrivi un post LinkedIn (max 120 parole) per annunciare il lancio del prodotto
> X a professionisti del settore. Tono competente ma caldo, senza superlativi.
> Chiudi con una domanda che inviti al commento.

La seconda versione dichiara scopo, pubblico, canale, lunghezza, tono e perfino
la chiusura. A Claude resta poco da indovinare, e la prima risposta è già vicina
a ciò che volevi: il tempo speso a scrivere bene la richiesta lo recuperi sulle
correzioni che non dovrai fare.

## Iterare o ripartire? (EVERGREEN)

Iterare nella stessa chat conserva il contesto: è la scelta giusta quando rifini
un risultato. Conviene invece aprire una **nuova chat** quando cambi argomento
del tutto, così il contesto vecchio non «sporca» le risposte nuove. Regola
pratica: stesso obiettivo, stessa chat; obiettivo diverso, chat nuova.

## Spezzare un compito grande (EVERGREEN)

Le richieste enormi («scrivimi il piano marketing completo») producono risposte
generiche, perché Claude deve indovinare troppo. Conviene procedere a tappe:
prima l'indice, poi una sezione alla volta, infine la revisione d'insieme. A ogni
passo dai un obiettivo chiaro e controlli il risultato prima di andare avanti.
Così mantieni il controllo e ottieni una qualità costante, invece di un muro di
testo da sistemare tutto in una volta. Vale per testi, analisi e codice allo
stesso modo: è la differenza tra delegare un progetto e delegare un passo.

## Lungo non vuol dire migliore (EVERGREEN)

Essere specifici non significa scrivere paragrafi. Spesso tre righe ben mirate —
obiettivo, contesto, formato — battono mezza pagina di istruzioni confuse. Punta
alla chiarezza, non alla quantità: ogni parola che non aggiunge un vincolo è
rumore. Se ti accorgi di ripeterti, togli invece di aggiungere. Un buon prompt si
riconosce così: nessuno dei suoi pezzi è eliminabile senza perdere qualcosa.

## Errori comuni

- **Richiesta generica.** Senza scopo e destinatario, la risposta è anonima.
- **Troppi obiettivi in un colpo.** Spezza i compiti complessi in passi.
- **Dire solo cosa non vuoi.** Indica il risultato desiderato, non i divieti.
- **Non dare esempi.** Quando il formato conta, un modello vale più di una
  descrizione.
- **Arrendersi alla prima risposta.** Itera: è parte del metodo, non un fallimento.

## In pratica: trasforma un prompt debole

1. Parti da una richiesta vaga che useresti d'istinto.
2. Aggiungi **scopo** ("serve per…") e **destinatario** ("per…").
3. Specifica il **formato** (lunghezza, struttura, tono).
4. Se hai un esempio del risultato voluto, incollalo.
5. Manda, valuta e **itera** con una correzione mirata.

## Riepilogo

1. Tratta Claude come un collega competente ma senza il tuo contesto.
2. Sii **chiaro e specifico**: scopo, destinatario, vincoli.
3. Dai **contesto** ed **esempi**; guidano più di mille parole.
4. Controlla il **formato** dicendo cosa vuoi, non cosa eviti.
5. **Itera**: la prima risposta è una bozza da affinare.

## Prossimo passo

Nel **cap. L1.3 — Impostazioni e stili** configuriamo tono, preferenze e capacità
(Web search, Code execution, Memory) per non doverle ripetere a ogni chat.
