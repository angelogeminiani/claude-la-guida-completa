# Capitolo L3.1 — Cowork: primi passi

> Livello 3 — Lavoro quotidiano.
> Dati di prodotto verificati il 22/06/2026 su fonti ufficiali.

## Obiettivo

Al termine saprai cos'è Cowork e in cosa differisce da Chat e da Claude Code,
avviare un task su una cartella del tuo computer, descrivere un risultato invece
di una sequenza di passi, e approvare le azioni che Claude propone mentre lavora.

## Prerequisiti

- Claude Desktop installato (vedi cap. L2.1).
- Un piano a pagamento: **Pro, Max, Team o Enterprise**. Cowork non è incluso
  nel Free (vedi cap. F.3 e il ledger). (VOLATILE)
- Una cartella con file su cui ha senso lavorare.

## Cos'è Cowork (VOLATILE)

Cowork è il tab dell'app desktop per il **lavoro agentico non di codice**: gli
affidi un compito su una cartella e lui lo porta avanti da solo — legge i file,
ragiona, crea o modifica documenti, esegue passaggi in sequenza — fermandosi a
chiederti conferma quando serve. (VOLATILE: research preview)

Gira in una **VM isolata** (una macchina virtuale, un computer dentro il
computer) sul tuo dispositivo. Questo è il punto chiave per la fiducia: Cowork
legge e scrive **solo nelle cartelle che gli colleghi**, e la rete segue le
impostazioni di egress (cosa può raggiungere su internet). Non vede il resto del
tuo disco se non glielo dai.

## Cowork, Chat e Code: chi fa cosa (EVERGREEN)

I tre tab dell'app rispondono a bisogni diversi. Sceglierli bene è metà del
lavoro.

Tabella L3.1.1 — Quando usare quale tab.

| Tab | Per cosa | Forma |
|---|---|---|
| Chat | Domande, bozze, idee | Botta e risposta |
| Code | Sviluppo software | Sui file di codice |
| Cowork | Compiti su file, multi-passo | Agentico, lungo |

In breve: se vuoi una risposta, Chat. Se programmi, Code. Se vuoi che qualcuno
**faccia** una cosa articolata sui tuoi file — riorganizza una cartella,
produca un report da più documenti, prepari una serie di file — Cowork.

## End-state, non i passi (EVERGREEN)

L'errore più comune al primo uso è guidare Cowork passo per passo, come si fa in
chat. Funziona meglio il contrario: descrivi il **risultato che vuoi** (lo
"end-state") e lascia che sia lui a trovare la sequenza.

- **Debole (passi):** "Apri il file. Ora leggi la colonna B. Adesso copia..."
- **Meglio (end-state):** "Da questi tre Excel di vendita, crea un riepilogo
  per regione con i totali trimestrali, salvato come `riepilogo.xlsx`."

Descrivere il risultato sfrutta ciò per cui Cowork è fatto: pianificare il
percorso. Tu definisci il "dove arrivare" e i vincoli; lui trova il "come".

## Approvare le azioni (EVERGREEN)

Mentre lavora, Cowork si ferma prima delle azioni che contano e ti mostra cosa
sta per fare: creare un file, modificarne uno, eseguire un comando. Tu approvi o
correggi. È lo stesso principio dei permessi di Claude Code (vedi cap. L2.4): la
parte ripetitiva scorre, le decisioni restano tue.

Non approvare a scatola chiusa. Leggi cosa propone, soprattutto le prime volte:
è così che impari a fidarti — o a capire dove serve essere più precisi nella
richiesta.

## In pratica: il tuo primo task

1. Apri Claude Desktop e vai sul tab **Cowork**.
2. **Collega una cartella**: scegline una con dei file veri, ma di cui hai una
   copia. Cowork agirà solo dentro questa cartella.
3. Scrivi il compito come **end-state**, con i vincoli:

   ```text
   In questa cartella ci sono appunti .txt sparsi.
   Raggruppali per argomento in sottocartelle e
   crea un INDICE.md che elenca cosa c'è dove.
   ```

4. Lascia che pianifichi. Quando si ferma per un'azione, **leggi e approva**.
5. A fine task, controlla il risultato nella cartella. Se non è quello che
   volevi, raffina la richiesta e rilancia.

## Errori comuni

- **Guidarlo passo per passo.** Spreca il suo punto di forza. Descrivi il
  risultato, non la procedura.
- **Collegare l'intero disco o cartelle critiche.** Collega solo ciò che serve,
  e lavora su copie finché non ti fidi.
- **Aspettarsi Cowork nel Free.** Serve un piano a pagamento. (VOLATILE)
- **Approvare senza leggere.** Le prime volte controlla cosa propone: è lì che
  impari a dargli istruzioni migliori.

## Riepilogo

1. Cowork è il tab desktop per il lavoro agentico non di codice, in una **VM
   isolata** che vede solo le cartelle collegate.
2. Chat per le risposte, Code per il software, Cowork per i compiti multi-passo
   sui tuoi file.
3. Descrivi il **risultato** (end-state) e i vincoli, non la sequenza di passi.
4. Approva le azioni che Cowork propone: il controllo resta tuo.
5. Collega solo le cartelle necessarie e parti da copie.

## Prossimo passo

Nel **cap. L3.2 — Projects** vediamo come dare a un lavoro ricorrente una casa
stabile: istruzioni, file di riferimento e memoria che restano tra una sessione
e l'altra.

---

*Dati su Cowork (VM isolata, piani, cartelle collegate) dal ledger, verificati
il 22/06/2026 su support.claude.com e code.claude.com/docs. Il task di esempio
non è stato eseguito qui: richiede l'app desktop con un account a pagamento.*
