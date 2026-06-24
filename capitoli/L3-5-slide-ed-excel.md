# Capitolo L3.5 — Slide ed Excel

> Livello 3 — Lavoro quotidiano.
> Dati di prodotto verificati il 22/06/2026 su fonti ufficiali.

## Obiettivo

Al termine saprai costruire una presentazione con un metodo a tre tempi
(struttura, contenuti, stile), impostare un foglio di calcolo passando da dati a
formule a grafici, e capire quando conviene l'add-in dentro Office invece della
generazione in chat.

## Prerequisiti

- Aver letto come si chiedono i documenti (cap. L3.4).
- Code execution / file creation attiva (vedi cap. L1.3). (VOLATILE)

## Slide: struttura, poi contenuti, poi stile (EVERGREEN)

Una presentazione fatta tutta in un colpo viene quasi sempre confusa. Il metodo
che funziona è in tre tempi, e segue lo stesso principio "prima il contenuto"
del capitolo precedente:

1. **Struttura.** Decidi prima la sequenza delle slide: quante, con quale
   titolo, in che ordine. È l'ossatura del discorso. Falla rivedere finché il
   filo regge.
2. **Contenuti.** Riempi ogni slide: pochi punti per slide, un'idea per slide.
   Qui conta cosa dici, non come appare.
3. **Stile.** Solo alla fine, l'aspetto: tema, colori, coerenza visiva.

Invertire l'ordine costa caro: rifinire lo stile di slide che poi riscrivi è
lavoro buttato. Esempio di prima mossa:

```text
Prepara la SCALETTA di una presentazione di 8
slide sul progetto X per la direzione: solo
titoli e una riga di contenuto per slide.
```

Quando la scaletta tiene, passi ai contenuti slide per slide, e per ultimo
chiedi il `.pptx` con il tema.

## Excel: dati, poi formule, poi grafici (EVERGREEN)

Per i fogli di calcolo l'ordine giusto è altrettanto netto:

1. **Dati.** Prima i dati puliti e ben strutturati: colonne con intestazioni
   chiare, una riga per record. Tutto il resto poggia qui.
2. **Formule.** Poi i calcoli: totali, percentuali, aggregazioni. Su dati ben
   strutturati le formule vengono semplici e corrette.
3. **Grafici.** Infine la visualizzazione, costruita sui dati e sui calcoli già
   a posto.

Se i dati sono disordinati, formule e grafici erediteranno il disordine. Vale la
pena spendere il primo tempo a sistemare le colonne.

> **Tip:** chiedi a Claude di **spiegare le formule** che inserisce. Un foglio
> che non capisci è un foglio di cui non puoi fidarti: fartele commentare ti fa
> da controllo.

Tabella L3.5.1 — L'ordine giusto, a colpo d'occhio.

| Output | Prima | Ultimo |
|---|---|---|
| Slide | Struttura | Stile |
| Excel | Dati | Grafici |

## L'add-in dentro Office (VOLATILE)

Oltre a generare file in chat, Claude vive **dentro** Office come add-in per
**Excel, Word e PowerPoint** (Claude per Microsoft 365). È in beta (research
preview) per i piani **Max, Team ed Enterprise**. (VOLATILE)

La differenza pratica è dove lavori:

- **In chat:** Claude **crea** il file da zero. Comodo quando parti dal nulla o
  produci molti documenti simili.
- **Nell'add-in:** Claude lavora **sul documento aperto** in Office. Comodo
  quando il file esiste già, è grande, o vuoi restare nello strumento dove poi lo
  rifinisci a mano.

Regola spiccia: se il documento nasce ora, la chat va benissimo; se stai
modificando qualcosa che è già in Excel o PowerPoint, l'add-in ti evita il
viavai tra app.

## In pratica: una presentazione in tre tempi

1. Chiedi la **scaletta** (solo titoli + una riga). Aggiustala.
2. Per ogni slide, chiedi i **contenuti**: pochi punti, uno per idea.
3. Chiedi il **.pptx** con un tema coerente:

   ```text
   Genera il .pptx dalla scaletta approvata, tema
   sobrio, un colore d'accento, titoli uniformi.
   ```

4. Apri il file. Per i ritocchi, modifiche puntuali (cap. L3.4) o, se ce l'hai,
   l'add-in di PowerPoint.

## Errori comuni

- **Partire dallo stile.** Tema e colori vengono per ultimi. Prima struttura e
  contenuti.
- **Troppo per slide.** Un'idea per slide. I muri di testo non si presentano.
- **Dati sporchi in Excel.** Formule e grafici ereditano il disordine: sistema
  prima le colonne.
- **Fidarsi di formule che non capisci.** Fattele spiegare: è il tuo controllo.
- **Cercare l'add-in nel piano sbagliato.** È beta su Max/Team/Enterprise.
  (VOLATILE)

## Riepilogo

1. Slide in tre tempi: **struttura → contenuti → stile**. Lo stile per ultimo.
2. Excel in tre tempi: **dati → formule → grafici**. Dati puliti prima di tutto.
3. Fatti spiegare le formule: un foglio che non capisci non è affidabile.
4. In chat Claude **crea** i file; nell'add-in lavora **sul documento aperto** in
   Office.
5. L'add-in M365 è beta su Max/Team/Enterprise. (VOLATILE)

## Prossimo passo

Chiuso il lavoro quotidiano, il **Livello 4 — Design** apre il canvas: generare
e iterare interfacce, partire dal proprio brand e portare il risultato in Claude
Code. Si comincia dal **cap. L4.1 — Design: il canvas**.

---

*Dati sull'add-in Microsoft 365 (prodotti, beta, piani) dal ledger, verificati
il 22/06/2026 su claude.com e support.claude.com. Gli esempi non sono stati
eseguiti in questa sede.*
