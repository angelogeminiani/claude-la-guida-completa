# Claude: la guida completa (repo companion)

Materiali di supporto al libro **"Claude: la guida completa"**, manuale in
italiano in formato A5 dedicato all'ecosistema Claude: dai fondamenti
all'installazione locale, fino a Skills, integrazioni e automazioni.

Questo repository è il **companion repo** del libro: raccoglie ciò che cambia
nel tempo o serve in formato digitale, così che il testo a stampa non
"nasca vecchio". Contiene i sorgenti dei capitoli, le risorse e gli strumenti
di build; nel tempo ospiterà anche aggiornamenti dei dati volatili ed errata.

> Pubblicazione **indipendente: non affiliata, non sponsorizzata e non
> approvata da Anthropic**. "Claude" e "Anthropic" sono marchi dei rispettivi titolari,
> citati a solo scopo identificativo e descrittivo. Vedi le
> [Note legali e disclaimer](#note-legali-e-disclaimer).

## Struttura del libro

Bozza completa: **33 capitoli** su sei livelli di complessità crescente, più
front matter e chiusura.

- **Front matter (F.1–F.4):** prefazione, ecosistema, modelli e piani, percorsi
  di lettura.
- **Livello 1 — Fondamenti (L1.1–L1.3):** primo contatto, conversare bene,
  impostazioni e stili.
- **Livello 2 — Installazione locale (L2.1–L2.4):** Desktop, Code,
  autenticazione, configurare il progetto.
- **Livello 3 — Lavoro quotidiano (L3.1–L3.5):** Cowork, Projects, connettori,
  documenti, slide ed Excel.
- **Livello 4 — Design (L4.1–L4.5):** canvas, design system import,
  `/design-sync`, Design dentro Cowork, export e Canva.
- **Livello 5 — Skills e identità (L5.1–L5.4):** anatomia, prima skill, skill in
  Cowork, voce.
- **Livello 6 — Avanzato (L6.1–L6.6):** Code avanzato, MCP custom, automazioni,
  limiti d'uso, sicurezza, API.
- **Chiusura (C.1–C.2):** progetto end-to-end, appendici.

## Cosa contiene

```
SOMMARIO.md Indice dei capitoli nell'ordine di lettura
capitoli/   Capitoli del libro in Markdown (sorgente del testo)
risorse/    Immagini, diagrammi e copertina (copertina.svg/.png)
scripts/    Strumenti di build e QA per il formato A5
docs/       Landing di presentazione (GitHub Pages) + PDF scaricabile
LICENSE     Licenza MIT
```

L'elenco completo dei capitoli con i link è in [SOMMARIO.md](SOMMARIO.md).

## Strumenti di build

Gli script in `scripts/` aiutano a produrre e verificare i capitoli in
formato A5. Esistono **due pipeline** di build:

- `build-elegant.py` — genera il PDF A5 nello **stile grafico Claude.ai**
  (sfondo crema, accento corallo, titoli Lora, copertina, tabelle raffinate,
  citazioni con barra, diagrammi vettoriali SVG) via HTML/CSS → **WeasyPrint**.
  Richiede `pandoc`, Python con `weasyprint`, e il font Lora. I diagrammi Mermaid
  sono resi in SVG da `mermaid2svg.py` (nessun Chromium necessario). Stile in
  `scripts/style-claude.css`. È la pipeline consigliata per la stampa.
- `build-a5.sh` — variante con **Pandoc + XeLaTeX** (`manuale.pdf`): layout da
  libro più sobrio. Richiede `pandoc` e XeLaTeX; per i diagrammi usa
  `mermaid-filter` se presente (`npm install -g mermaid-filter`), altrimenti
  restano come codice. Header glifi in `scripts/a5-header.tex`, copertina in
  `scripts/a5-cover.tex`.
- `check-a5.sh` — segnala le righe **dentro i blocchi di codice** più lunghe
  di 56 caratteri (limite di larghezza A5); Mermaid e prosa sono ignorati.

Esempio:

```bash
python3 scripts/build-elegant.py manuale_produzione.pdf
```

Oppure la variante LaTeX (la cartella predefinita è `capitoli/`):

```bash
bash scripts/check-a5.sh capitoli/
bash scripts/build-a5.sh
```

## Sito di presentazione

La landing del libro è in `docs/` (HTML statico, un solo `index.html`, palette
Claude.ai) e si pubblica su **GitHub Pages**:
`https://angelogeminiani.github.io/claude-la-guida-completa/`.

- **Attivazione (una volta):** repo *Settings → Pages → Build and deployment →
  Source: Deploy from a branch → Branch: `main` / `/docs`*. Da lì ogni push che
  modifica `docs/` aggiorna il sito (nessun workflow, nessuno scope token).
- **Contenuti:** hero con download del PDF, valore del libro, i sei livelli, per
  chi è, CTA finale; meta tag Open Graph/Twitter e immagine social `og-image.png`.
- **Download:** `docs/manuale_produzione.pdf` è committato per il download diretto.
- **Aggiornare gli asset del sito:** `bash scripts/build-site.sh` rigenera PDF,
  immagine social e copertina dentro `docs/`.

## Errata e aggiornamenti

I dati di prodotto (versioni, comandi, prezzi) sono **volatili**: nel libro
sono marcati come tali e rimandano a questo repo per la versione aggiornata.
Segnalazioni ed errata sono benvenute tramite le *issue* di GitHub.

## Note legali e disclaimer

### Indipendenza e assenza di affiliazione

Questo è un progetto **editoriale indipendente e non ufficiale**. Non è
prodotto, autorizzato, sponsorizzato, approvato, certificato né altrimenti
collegato ad Anthropic PBC o alle sue affiliate. Le opinioni e le
interpretazioni contenute nel libro e in questo repository sono dell'autore.

### Marchi di terze parti

"Claude", "Anthropic", "Claude Code", "Cowork" e gli altri nomi di prodotto,
servizio, logo e marchio citati appartengono ai rispettivi titolari. Tali
nomi sono usati esclusivamente in funzione **identificativa e descrittiva**
(uso nominativo / fair use) per riferirsi ai prodotti oggetto del manuale, e
**non** implicano alcun rapporto di sponsorizzazione o approvazione. Nessun
logo, icona o marchio figurativo di terze parti è riprodotto in questo
repository.

### Contenuti, copyright e licenza

Il testo, i diagrammi originali e gli script presenti in questo repository
sono **opera originale dell'autore**, © 2026 Gian Angelo Geminiani.

Salvo dove diversamente indicato, il materiale di questo repository è rilasciato
con licenza **MIT** (vedi [LICENSE](LICENSE)). La licenza MIT si applica **solo**
all'opera originale dell'autore; **non** concede alcun diritto su marchi, nomi,
loghi, software, documentazione o altri contenuti di proprietà di terze parti,
che restano soggetti ai termini dei rispettivi titolari.

Eventuali brevi citazioni di documentazione ufficiale di terze parti sono
riportate, ove presenti, a fini di commento, cronaca, critica o didattica, con
indicazione della fonte, nei limiti del diritto di citazione.

### Accuratezza, aggiornamento e nessuna garanzia

I contenuti sono forniti **"così come sono" ("as is"), senza garanzie** di
alcun tipo, esplicite o implicite, comprese quelle di accuratezza, completezza,
idoneità a uno scopo specifico o aggiornamento. Le informazioni su versioni,
comandi, prezzi, menu e funzionalità si riferiscono a prodotti di terze parti
in rapida evoluzione: sono **verificate alla data indicata e soggette a
modifica** senza preavviso. Verifica sempre i dati sensibili sulle fonti
ufficiali prima di agire.

Nei limiti consentiti dalla legge, l'autore **declina ogni responsabilità**
per danni diretti o indiretti derivanti dall'uso di questi materiali, dei
comandi o degli script qui forniti. L'esecuzione di comandi e script avviene
a rischio dell'utente.

### Uso dei prodotti di terze parti

L'uso di Claude e degli altri prodotti citati è regolato dai rispettivi
**termini di servizio e condizioni di licenza**, che prevalgono in caso di
conflitto. Consulta sempre la documentazione ufficiale aggiornata su
docs.claude.com, code.claude.com, support.claude.com e anthropic.com.

### Segnalazioni

Per errata, imprecisioni o richieste di rimozione di contenuti, apri una
*issue* su GitHub o contatta l'autore.
