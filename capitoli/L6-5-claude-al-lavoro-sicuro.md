# Capitolo L6.5 — Claude al lavoro, sicuro

> Livello 6 — Avanzato.
> Dati di prodotto verificati il 24/06/2026 su fonti ufficiali.

## Obiettivo

Al termine saprai cosa cambia quando Claude entra in un'organizzazione: chi governa
le capacità, come si gestiscono ruoli e dati, e perché per il lavoro aziendale
l'account personale non è la scelta giusta. È il capitolo che separa l'uso
individuale da quello di squadra.

## Prerequisiti

- Conoscere i piani (cap. F.3) e i connettori (cap. L3.3).

## Account personale o aziendale (EVERGREEN)

La prima decisione è anche la più importante: per il lavoro dell'organizzazione si
usa un account **gestito dall'organizzazione** (Team o Enterprise), non quello
personale. La ragione non è formale. Su un account aziendale i dati, gli accessi e
le regole li controlla chi amministra; su quello personale restano in mano al
singolo, fuori dalle policy dell'azienda. Mettere materiale di lavoro su un account
personale significa portarlo fuori dal perimetro che l'organizzazione può
proteggere e gestire.

## Chi governa le capacità (VOLATILE)

In Team ed Enterprise non tutto è acceso per tutti. Un **Owner** o **Primary
Owner** decide cosa è disponibile, da **Admin > Capabilities**: Web search,
connettori, e altre funzioni si abilitano a livello di organizzazione. Per questo,
se non vedi una funzione, spesso non è un errore: è una scelta di chi amministra
(lo abbiamo già visto per Web search nel cap. L1.3 e per i connettori nel cap.
L3.3).

Lo stesso vale per le **azioni dei connettori**: un admin può permettere la sola
lettura e bloccare la scrittura, per tutta l'organizzazione (cap. L3.3).

## Ruoli, identità e dati (VOLATILE)

Le organizzazioni hanno bisogno di controlli che un account singolo non ha. La
tabella riassume cosa aggiungono i piani per le aziende.

Tabella L6.5.1 — Controlli per le organizzazioni.

Ogni colonna è additiva: Enterprise include quel che ha Team, e aggiunge.

| Area | Team | Enterprise (in più) |
|---|---|---|
| Accessi | admin, SSO | RBAC, SCIM |
| Dati | no training* | retention, audit log |
| Rete | — | IP allowlisting |

*Sia su Team sia su Enterprise, di default i dati non sono usati per il training;
Enterprise aggiunge retention e audit log. (VOLATILE)

In sintesi: **Team** porta amministrazione, SSO (accesso unico) e deployment
controllato; **Enterprise** aggiunge ruoli granulari (RBAC), provisioning
automatico degli utenti (SCIM), audit log, gestione della retention dei dati,
allowlisting degli IP e funzioni di sicurezza dedicate. Sono gli strumenti che
rendono l'uso conforme alle policy aziendali, non lasciato al singolo.

## Il modello dei permessi, ancora (EVERGREEN)

Un principio attraversa tutto il libro: Claude **eredita i tuoi permessi**. Vale per
i connettori (vede solo ciò che vedi tu alla fonte, cap. L3.3) e per il lavoro sui
file (tocca solo le cartelle collegate, cap. L3.1). In azienda questo è una
garanzia: i controlli del sistema d'origine restano in vigore, e Claude non li
scavalca. Restringere in Claude non concede mai più accesso di quanto la fonte
permetta.

## In pratica: introdurre Claude in azienda

1. Usa un account **gestito dall'organizzazione**, non quello personale.
2. Fai definire a un Owner le **capacità** disponibili (Admin > Capabilities).
3. Imposta gli **accessi**: SSO e, in Enterprise, ruoli (RBAC) e provisioning
   (SCIM).
4. Configura le **restrizioni dei connettori** secondo cosa il team può leggere o
   modificare (cap. L3.3).
5. Concorda le regole su **dati** e retention prima di mettere materiale sensibile.

## Errori comuni

- **Lavoro aziendale su account personale.** Porta i dati fuori dal controllo
  dell'organizzazione: usa l'account gestito.
- **Pensare a un bug quando manca una funzione.** Spesso l'ha disattivata un admin
  (cap. L1.3, L3.3).
- **Connettori senza restrizioni.** In team, definisci cosa è in sola lettura e
  cosa no (cap. L3.3).
- **Rinviare le regole sui dati.** Concordale prima, non dopo aver caricato
  materiale sensibile.

## Riepilogo

1. Per il lavoro aziendale usa un account **gestito dall'organizzazione**, non
   personale.
2. Un **Owner** governa le capacità da **Admin > Capabilities**.
3. **Team** aggiunge admin e SSO; **Enterprise** RBAC, SCIM, audit log, retention,
   IP allowlisting.
4. Claude **eredita i permessi**: i controlli della fonte restano in vigore.
5. Definisci accessi, restrizioni dei connettori e regole sui dati prima di
   partire.

## Prossimo passo

Nel **cap. L6.6 — Integrare via API** chiudiamo il livello tecnico: come passare
dalle interfacce al codice, con l'endpoint dei messaggi e un primo esempio.

---

*Dati su controlli Team/Enterprise (RBAC, SCIM, SSO, audit, retention) verificati
il 24/06/2026 su claude.com/pricing e support.claude.com. Pubblicazione
indipendente, non affiliata ad Anthropic.*
