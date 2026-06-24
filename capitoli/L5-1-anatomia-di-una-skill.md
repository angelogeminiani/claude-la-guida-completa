# Capitolo L5.1 — Anatomia di una skill

> Livello 5 — Skills e identità.
> Dati di prodotto verificati il 24/06/2026 su fonti ufficiali.

## Obiettivo

Al termine saprai cos'è una skill, in cosa differisce da un prompt, come è fatto
un file `SKILL.md` e perché la sua `description` è la parte più importante. È la
base concettuale per costruirne una tua nel prossimo capitolo.

## Prerequisiti

- Saper scrivere richieste efficaci (cap. L1.2).
- Avere **code execution** attiva (cap. L1.3): è richiesta per le Skills.
  (VOLATILE)

## Skill o prompt? (EVERGREEN)

Un prompt vale per una conversazione: lo scrivi, ottieni la risposta, finisce lì.
Una **skill** è conoscenza riutilizzabile che Claude carica **da solo** quando il
contesto lo richiede, senza che tu la incolli ogni volta. Scrivi una regola una
volta, e Claude la applica ogni volta che serve.

La differenza pratica: il prompt è un'istruzione usa-e-getta; la skill è una
competenza permanente. Se ti accorgi di reincollare le stesse istruzioni in chat
dopo chat, quel testo è un candidato a diventare una skill.

## Una cartella e un file (VOLATILE)

Una skill, nella sua forma minima, è una **cartella** che contiene un file
`SKILL.md`. Solo quel file è obbligatorio: basta lui a fare una skill funzionante.
Il file ha due parti:

- un **frontmatter** in cima (metadati tra due righe `---`);
- un **corpo** in Markdown con le istruzioni vere e proprie.

> **Nota:** il file si chiama per convenzione `SKILL.md`. La documentazione lo
> cita anche come `skill.md`: è lo stesso file. In Claude Code le skill di
> progetto stanno sotto `.claude/skills/` (cap. L2.4). (VOLATILE)

## Il frontmatter: due campi obbligatori (VOLATILE)

Il frontmatter dichiara chi è la skill. Due campi sono obbligatori:

- **name** — il nome leggibile, massimo **64 caratteri**.
- **description** — cosa fa la skill e **quando usarla**, massimo **200
  caratteri**.

Esistono campi opzionali (per esempio `dependencies` per i pacchetti software),
ma name e description bastano per partire.

Ecco una skill minima completa:

```markdown
---
name: verbale-riunione
description: Da note grezze crea un verbale
  con decisioni e action item.
---

# Verbale riunione

Trasforma note disordinate in un verbale:
1. Elenca le decisioni prese.
2. Estrai gli action item con responsabile.
3. Chiudi con i punti rimasti aperti.
```

## La description è tutto (EVERGREEN)

Tra i due campi, la `description` è quello che conta davvero. Claude la legge per
decidere **se** attivare la skill: con decine o centinaia di skill disponibili, è
la description a far scattare quella giusta al momento giusto. Una description
vaga ("aiuta con i documenti") non scatta mai con precisione; una specifica ("da
note grezze crea un verbale con decisioni e action item") sì.

Qui entra il meccanismo della **progressive disclosure** (rivelazione
progressiva): Claude legge prima solo i metadati — name e description — per capire
se la skill serve, e carica il corpo completo **solo se** decide di usarla. È
efficiente: poche righe gli bastano per scegliere, senza leggere tutto. Per questo
la description va scritta pensando a quando vuoi che la skill si attivi, non solo a
cosa fa.

## Il corpo: istruzioni ed esempi (EVERGREEN)

Sotto il frontmatter, il corpo Markdown contiene le istruzioni che Claude segue
quando la skill è attiva: cosa fare, in che ordine, con quali vincoli. Gli esempi
aiutano molto — mostrare un input e l'output atteso vale più di una spiegazione
astratta. Se le istruzioni crescono troppo, puoi spostarne una parte in file di
risorse separati (per esempio un `REFERENCE.md`) e richiamarli dal `SKILL.md`.

## Errori comuni

- **Confondere skill e prompt.** Il prompt è per una chat; la skill è
  riutilizzabile e si attiva da sola.
- **Description vaga.** È il campo che fa scattare la skill: sii specifico sul
  "quando".
- **Sforare i limiti.** name oltre 64 o description oltre 200 caratteri non sono
  validi. (VOLATILE)
- **Mettere tutto nel corpo.** Se è troppo, usa file di risorse separati.

## Riepilogo

1. Una skill è conoscenza **riutilizzabile** che Claude carica da solo; un prompt
   vale per una sola chat.
2. Nella forma minima è una **cartella** con un file **`SKILL.md`**.
3. Il frontmatter ha due campi obbligatori: **name** (≤64) e **description**
   (≤200). (VOLATILE)
4. La **description** decide quando la skill scatta: scrivila pensando al "quando".
5. Il corpo Markdown contiene istruzioni ed esempi; le risorse extra vanno in file
   separati.

## Prossimo passo

Nel **cap. L5.2 — La tua prima skill** costruiamo una skill da zero, a mano e con
l'aiuto di skill-creator, e impariamo a testare che si attivi quando deve.

---

*Dati su SKILL.md, frontmatter e limiti verificati il 24/06/2026 su
support.claude.com/en/articles/12512198 e code.claude.com/docs/en/skills.
L'esempio di SKILL.md non è stato eseguito in questa sede.*
