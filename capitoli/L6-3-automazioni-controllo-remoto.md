# Capitolo L6.3 — Automazioni e controllo remoto

> Livello 6 — Avanzato.
> Dati di prodotto verificati il 24/06/2026 su fonti ufficiali.

## Obiettivo

Al termine saprai far lavorare Claude nel tempo senza starci davanti: i **Scheduled
Tasks** in Cowork, le **Routines** cloud di Claude Code, e il **Dispatch** che
trasforma il telefono in telecomando. Capirai soprattutto quale scegliere, perché
girano in posti diversi.

## Prerequisiti

- Cowork (cap. L3.1) per i task pianificati; Claude Code (cap. L2.2) per le
  routine.
- Un piano a pagamento. (VOLATILE)

## Tre strumenti, tre posti (EVERGREEN)

La differenza che conta non è cosa fanno, ma **dove girano**: dipende da questo se
funzionano a computer spento, e quanto sono adatti al lavoro non tecnico.

Tabella L6.3.1 — Dove gira ciascuno strumento.

| Strumento | Dove gira | A computer spento |
|---|---|---|
| Scheduled Task | Cowork, Desktop | no |
| Routine | cloud Anthropic | sì |
| Dispatch | il tuo computer | no |

## Scheduled Tasks (VOLATILE)

I **Scheduled Tasks** fanno girare un task di Cowork in automatico, su pianificazione
o su richiesta: «ogni mattina controlla la posta», «ogni venerdì prepara il
report». Vivono in **Cowork su Desktop**, sui piani a pagamento.

Il limite da conoscere: girano **solo a computer acceso e app Desktop aperta**. Se
il computer è spento o l'app è chiusa all'ora prevista, il task viene **saltato** e
parte da solo appena riaccendi o riapri l'app. Sono perfetti per chi lascia il
computer acceso, meno per chi vuole garanzia di esecuzione a ogni costo.

## Routines (VOLATILE)

Le **Routines** di Claude Code sono configurazioni salvate — un prompt, uno o più
repository e i tuoi connettori — che girano sul **cloud di Anthropic**, non sul tuo
computer. Per questo funzionano anche a macchina spenta.

Il loro punto di forza sono i **trigger** combinabili: la stessa routine può
partire su pianificazione, in risposta a una chiamata API e a un evento GitHub,
tutto insieme. Sono lo strumento per le automazioni di sviluppo che devono essere
affidabili e indipendenti dalla tua macchina.

## Dispatch (VOLATILE)

Il **Dispatch** trasforma il telefono in un telecomando per Claude sul tuo
computer. Mandi un messaggio dall'app mobile e Claude esegue il task **sulla tua
macchina**: legge i file locali, tira dati dai connettori, cerca sul web e ti
riporta il risultato. Tra l'app mobile e il Desktop si apre un **thread unico e
persistente**, come un walkie-talkie: tu assegni da remoto, Claude lavora in
locale.

È la risposta al «vorrei far partire quel lavoro mentre sono fuori»: il computer
deve essere acceso, ma tu no.

## Quale scegliere (EVERGREEN)

- Lavoro **non tecnico, ricorrente**, e tieni il computer acceso → **Scheduled
  Task**.
- Automazione di **sviluppo** che deve girare **sempre**, anche a macchina spenta,
  con trigger vari → **Routine** cloud.
- Vuoi **avviare da remoto** un lavoro che usa i tuoi file locali → **Dispatch**.

## In pratica: pianifica un task ricorrente

1. In Cowork, descrivi il task come faresti per un lavoro normale (cap. L3.1).
2. Imposta la ricorrenza (per esempio «ogni mattina alle 8»).
3. Lascia il computer acceso e l'app Desktop aperta all'orario previsto.
4. Per le automazioni di sviluppo indipendenti, valuta invece una **Routine** in
   Claude Code.
5. Per avviare da fuori, usa il **Dispatch** dall'app mobile.

## Errori comuni

- **Scheduled Task a computer spento.** Viene saltato e parte alla riapertura: per
  l'esecuzione garantita usa una Routine cloud. (VOLATILE)
- **Confondere Routine e Scheduled Task.** Le Routine girano sul cloud (Code), i
  task in Cowork sul tuo Desktop.
- **Aspettarsi il Dispatch a macchina spenta.** Esegue in locale: il computer deve
  essere acceso. (VOLATILE)

## Riepilogo

1. La differenza chiave è **dove gira** lo strumento.
2. **Scheduled Tasks**: Cowork su Desktop; solo a computer acceso e app aperta.
3. **Routines**: cloud di Anthropic (Code); girano sempre, trigger combinabili.
4. **Dispatch**: avvii dal telefono, Claude esegue sul tuo computer acceso.
5. Scegli in base ad affidabilità richiesta e tipo di lavoro.

## Prossimo passo

Nel **cap. L6.4 — Gestire i limiti d'uso** vediamo da cosa dipende il consumo e
come lavorare a lungo senza sbattere contro i limiti.

---

*Dati su Scheduled Tasks, Routines e Dispatch verificati il 24/06/2026 su
support.claude.com (scheduled tasks, dispatch) e code.claude.com/docs
(scheduled-tasks/routines). Le funzioni richiedono un account a pagamento, quindi
non sono state eseguite in questa sede.*
