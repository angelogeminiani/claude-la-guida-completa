# Capitolo L3.3 — Connettori

> Livello 3 — Lavoro quotidiano.
> Dati di prodotto verificati il 24/06/2026 su fonti ufficiali.

## Obiettivo

Al termine saprai cosa sono i Connectors (connettori), come collegarne uno dalla
directory, come attivarli in una conversazione, e quali cautele tenere — sia da
utente sia, in azienda, da amministratore.

## Prerequisiti

- Saper aprire una chat (vedi cap. L1.1) e usare il menu strumenti (vedi cap.
  L1.3).
- Un account su un servizio che vuoi collegare (Drive, Slack, un gestore di
  task...).

## Cosa sono i connettori (VOLATILE)

Un connettore dà a Claude accesso a un'app o un servizio: leggere i tuoi dati e
**compiere azioni** al loro interno. Collega Claude a Linear per aprire issue, a
Slack per inviare messaggi, a Google Drive per cercare nei tuoi file.

Il punto da capire bene è il modello dei permessi: **Claude eredita i tuoi
permessi** nel servizio collegato. Se tu non puoi vedere un certo file, canale o
record alla fonte, il connettore non lo raggiunge da Claude. Un connettore non
ti dà più accesso di quanto già hai — lo porta solo dentro la conversazione.

I web connectors sono disponibili per **tutti gli utenti** su Claude, Cowork,
Desktop e Mobile; funzionano anche con Claude Code e via API. (VOLATILE)

## La directory dei connettori (VOLATILE)

I connettori disponibili stanno nella **Connectors Directory** (claude.ai/
connectors). Ogni connettore ha una scheda con i casi d'uso, le capacità di
lettura/scrittura e la disponibilità. Alcuni hanno il badge **Interactive**:
rendono interfacce live — dashboard, board, strumenti — dentro la conversazione.

Apri la directory in due modi:

- **Da una chat:** pulsante **"+"** (o "/") > "Connectors" > "Manage connectors"
  > "+".
- **Dalle impostazioni:** **Customize > Connectors** > "+".

## Collegare e attivare un servizio (VOLATILE)

Collegare un servizio e usarlo sono due passaggi distinti.

**Collegare** (una volta): dalla directory, clic sul connettore, rivedi le sue
capacità, "Connect"/"Install", segui i prompt di autenticazione (di solito
OAuth, cioè autorizzi Claude dal sito del servizio), configura i permessi.

**Attivare** (per conversazione): "+" (o "/") > "Connectors", poi accendi con il
toggle i servizi che vuoi per quella chat. Da lì Claude li usa quando sono
pertinenti — e può proporli da solo, senza che tu li nomini ogni volta.

> **Tip:** se hai molti connettori, da "Connectors" > "Tool access" scegli come
> si caricano. Il default **Auto** va bene per quasi tutti; con 10 o più
> connettori attivi, **On demand** lascia più spazio alla conversazione.

## In azienda: il ruolo dell'admin (VOLATILE)

Su **Team ed Enterprise** un connettore non è usabile finché un **Owner** o
**Primary Owner** non lo abilita per l'organizzazione (Organization settings >
Connectors > "Browse connectors" > "Add to your team"). Abilitare **non** dà
accesso a nessuno: ognuno si autentica comunque per conto suo.

L'admin può anche **restringere le azioni** di un connettore per tutta l'org. Da
Customize > Connectors, sul connettore, le **Tool permissions** sono divise per
tipo (sola lettura, scrittura/cancellazione) e per ciascuna scegli *Always
allow*, *Needs approval* o *Blocked*. Vale per tutti e non è aggirabile dal
singolo.

Tabella L3.3.1 — Esempi di restrizione delle azioni.

| Servizio | Permetti | Blocca |
|---|---|---|
| Email | Cercare e riassumere | Inviare messaggi |
| Drive | Leggere i file | Creare/modificare |
| Linear | Vedere le issue | Crearne o cambiarle |

Queste restrizioni lavorano **insieme** ai permessi del servizio: anche dove
Claude può scrivere, serve comunque il permesso alla fonte. Restringere in
Claude non concede mai più di quanto il sistema d'origine consente — al massimo
restringe.

## Cautele (EVERGREEN)

- **Connetti solo ciò di cui ti fidi e che ti serve.** Collegare un servizio
  significa dare a Claude accesso ai tuoi dati lì dentro.
- **Rivedi gli accessi richiesti** durante la connessione, e **disconnetti** ciò
  che non usi più (Customize > Connectors).
- **Custom connector = non verificato da Anthropic.** Puoi aggiungere connettori
  personalizzati (remote MCP), ma collega solo server di organizzazioni fidate.
  Sui custom connector entriamo nel dettaglio al Livello 6 (cap. L6.2).
- **Team/Enterprise:** i connettori funzionano solo in Project privati, e le chat
  con contenuti sincronizzati non sono condivisibili.

## In pratica: collega Google Drive

1. In chat, "+" (o "/") > "Connectors" > "Manage connectors" > "+".
2. Cerca il connettore nella directory e aprilo.
3. Leggi le capacità, poi "Connect" e autorizza con il tuo account (OAuth).
4. Torna in chat, "+", "Connectors", e attiva il toggle del servizio.
5. Prova:

   ```text
   Cerca nel mio Drive il preventivo di marzo
   e riassumimi le voci principali.
   ```

## Errori comuni

- **"Ho collegato ma non lo usa."** Collegare non basta: attiva il toggle nel
  menu "Connectors" della chat.
- **Aspettarsi accesso a tutto.** Claude vede solo ciò che vedi tu nel servizio.
- **(Team) "Il connettore non c'è."** Deve prima abilitarlo un Owner per l'org;
  poi ti autentichi tu.
- **Custom connector che va in timeout.** Il server MCP è raggiunto dal cloud di
  Anthropic, non dal tuo device: deve stare su internet pubblico (vedi cap.
  L6.2). (VOLATILE)

## Riepilogo

1. Un connettore dà a Claude accesso a un'app per leggere dati e agire, **con i
   tuoi stessi permessi** alla fonte.
2. I connettori stanno nella Connectors Directory; alcuni sono **Interactive**.
3. Collegare (OAuth, una volta) e attivare (toggle, per conversazione) sono due
   passi distinti.
4. In Team/Enterprise un Owner abilita il connettore e può restringerne le azioni
   per tutta l'org.
5. Connetti solo ciò di cui ti fidi, rivedi gli accessi, disconnetti l'inutile.

## Prossimo passo

Nel **cap. L3.4 — Documenti** usiamo Claude per generare file professionali —
Word, PowerPoint, Excel, PDF — partendo dal contenuto giusto.

---

*Dati sui connettori (directory, OAuth, ruolo admin, restrizioni azioni) dal
ledger, verificati il 24/06/2026 su support.claude.com/en/articles/11176164. I
passaggi operativi non sono stati eseguiti in questa sede.*
