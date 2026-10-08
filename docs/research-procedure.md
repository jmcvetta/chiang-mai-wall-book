# Operational research procedure

This document makes the research process in [PLANNING.md](../PLANNING.md) executable by a worker who has not seen the planning conversation. It adds handoff detail only. Editorial policy, the section-definition rules, the endnote standard, the adversarial review protocol and the rights rules stay in PLANNING.md, and PLANNING.md wins on any conflict. Section references below use the headings of that file.

Everything under `research/` and `book/` named here is a **proposed destination**. None of it exists yet. Create a file only when a stage produces its content. Do not create empty section trees.

## Rules every worker follows

1. Work from the assignment brief alone. If the brief lacks an input listed for your stage, stop and report the gap. Do not invent the input.
2. Never claim to have visited, measured or photographed a site. Remote evidence keeps its own observation date, which is not the retrieval date.
3. A search snippet, AI output or uninspected reference is a **lead**, not evidence.
4. Write only to your own output files. Shared records have one integration owner (see "Roles").
5. Never invent metadata, locators or calendar conversions. Write `unknown`.
6. Keep failed runs, rejected claims and declined escalations. Do not replace them with a cleaner story.
7. Record the actual model that did the work, not the model requested.
8. Do not add paid access, commissioned specialist work or owner fieldwork. Record inaccessible sources as leads.

## Roles

| Role | Owns | Does not |
| --- | --- | --- |
| Editorial owner (human) | Section register, names, route order, the three gates, final acceptance | Act as historian or archaeologist |
| Integration owner | `research/shared/*`, section boundaries, handoff commits | Settle an ambiguous date or identity alone |
| Section coordinator | Assignment brief, run record, next-recipient decisions | Edit shared records directly |
| Discovery / extraction worker | One search stream or source batch, in its own files | Judge phase, date or identity |
| Section researcher | Claim ledger and research history | Cite an agent-written history as a source |
| Writer / editor | Chapter text | Add prose first and search for citations afterwards |
| Reviewer | Claim-by-claim findings | Review a chapter they drafted |
| Section-level reviewer | Whole-section reconciliation | Rely on batch summaries |
| Competent human reviewer | Consequential translation and archaeological interpretation | — |

The owner's nonexpert approval is a workflow decision. It is not specialist review and it is not historical evidence. Never cite it for a claim.

## Handoff header

Every stage output begins with this header. A handoff without it is incomplete.

```text
section:        <descriptive section name, or "shared">
stage:          <stage name from the table below>
status:         draft | reviewed | owner-accepted
input revision: <commit SHA of every input artifact>
outputs:        <paths written>
sources used:   <source keys with locators, or "none">
missing inputs: <list, or "none">
next recipient: <role>
next action:    <one concrete step>
```

`status` describes the artifact. It does not describe any claim in it.

## Stages

Parallel work inside one section is allowed from the first pilot. Parallel work across sections is allowed only after the third human gate (see "Human gates").

| Stage | Inputs | Owner | Outputs | Evidence status produced | Stop when | Escalate to |
| --- | --- | --- | --- | --- | --- | --- |
| 1. Assign | Reviewed inventory entry using the existing inventory fields: name, mapped extent, name variants, identity uncertainties | Section coordinator | `research/sections/<name>/brief.md` stating questions, known sources, search scope, stopping point and output paths | none | The brief names scope and stopping point | Integration owner, if identity is ambiguous |
| 2. Discover | Brief | Cheaper workers, one coherent stream each (Thai literature, non-Thai literature, images and maps/archives) | `discovery-thai.md`, `discovery-other-languages.md`, `discovery-images-and-maps.md` | Source access status only | Search scope exhausted or the stopping point reached; searched and inaccessible items listed | Coordinator, for a source needing paid or restricted access |
| 3. Extract | One accessible source batch | Cheaper workers | `evidence.md` entries (one worker per file or source bundle) | Inspected passages | The batch is extracted, or an item is found inaccessible | Section researcher, for difficult handwriting or consequential translation ambiguity |
| 4. Synthesize | Evidence batches and the list of missing sources | Section researcher | `claims.md`, `research-history.md` | Claim support status | Every candidate claim is classified; conflicts and unknowns are listed | Integration owner for identity or boundary changes; competent human for interpretation |
| 5. Edit | History, claim ledger, standard chapter template | Writer / editor | `book/chapters/<name>.md` (meaning only, no visual styling) | none new | Each retained claim keeps its evidence link | Section researcher, if wording needs support the ledger lacks |
| 6. Check | A chapter at a fixed revision | Mechanical checks, then independent reviewers on claim batches | `review.md` findings | Review disposition | Every factual statement has been reviewed, captions, tables, map labels and footnotes included | Capable reviewer or competent human |
| 7. Reconcile | All review outputs and the full chapter | Independent section-level reviewer | Reconciliation entry in `review.md`; accept or revise decision | Whole-section consistency | No unresolved support objection is attached to a retained claim | Competent human; editorial owner |
| 8. Correct and accept | Reconciliation decision | Coordinator, then editorial owner | Revised chapter; updated `runs.md` | `owner-accepted` artifact status | Review reopened for every changed wording or evidence item | Editorial owner |

A mechanical check can find a dangling note or an empty locator. It cannot show that a citation supports a claim.

Discovery batches related items. Never assign one worker per query or per passage. Bound the number of active workers.

## Record specifications

These are Markdown files. Use the table or list form shown. No database, no schema tool.

### Source register: `research/shared/sources/`

One file per source, named by a bibliographic key. A key is not a section identity.

```text
key:               <short key>
citation:          <bibliographic details, original language and transliteration or translation if any>
language:          <language>
found:             <date> via <route>      # a reference was seen
obtained:          <date> via <route> | no # the source itself was retrieved
inspected:         <passages or figures inspected> | none
access conditions: <open | library | paywalled | restricted | unknown>
redistribution:    <confirmed permitted, with basis and credit | not permitted | unknown>
translation:       original | human translation | machine translation | none
derived from:      <keys of upstream sources, or "original">
cited by:          <keys it cites that matter for lineage>
used by sections:  <section names, with the scope each use covers>
```

Access status has three levels: **found**, **obtained**, **inspected**. A lead stays a lead until a passage is inspected. Open access is not permission to commit the file.

### Discovery record: `discovery-*.md`

One entry per candidate source: key or provisional title, authors, language, publication details, DOI or catalog reference, access link, why it may be relevant, upstream citations, and the access level reached. The file ends with the **search log**: streams searched, terms, dates, what was not searched, and what stayed inaccessible. A search log does not claim exhaustiveness.

### Evidence record: `evidence.md`

One entry per inspected passage, figure or dated image.

```text
id:               <evidence id within the section>
source:           <key> locator: <page, figure, passage, plate, or URL with date>
original wording: <quoted where lawful, else "not shareable">
translation:      <status and who translated>
subject:          <exact physical component and phase this applies to>
scope:            <what place and date the source actually covers>
observation date: <date or "unknown"> retrieval date: <date>
limits:           <what the source does not establish>
lineage:          <independent | derived from <key>>
```

A summary by an agent is not evidence. Copy or point to the underlying passage.

### Claim ledger: `claims.md`

```text
id:           <claim id within the section>
statement:    <the proposed assertion>
type:         observation | source assertion | interpretation | unresolved
evidence:     <evidence ids with locators>
independence: <how many independent lineages support it, naming them>
applies to:   <component and phase, with the reasoning that connects source to visible fabric>
status:       candidate | supported | narrowed | rejected | unresolved
notes:        <conflicts, contrary evidence sought and where, limits>
```

Rejected and unresolved claims stay in the ledger. A claim whose only support is a copy or translation of another source has one lineage.

### Research history: `research-history.md`

A long source-linked narrative that may include predecessors. Label it as unreviewed research at the top. Mark candidate claims, disagreements, rejected claims and unresolved questions explicitly. It is never a source for another agent to cite.

### Review finding: `review.md`

Each finding has all of these fields.

```text
finding id:          <id>
manuscript location: <chapter path and anchor, caption, table, map label or footnote>
claim id:            <ledger id>
source locator:      <source key and exact locator reopened>
objection:           <how the statement could mislead or be wrong>
required resolution: narrower wording | additional evidence | corrected attribution | removal
response:            <drafter's evidence, not confidence>
recheck:             <reviewer's result>
final disposition:   supported as written | supported only with narrower wording | omit | unresolved - do not publish as fact
reviewer:            <role and actual model or person>
```

A reviewer who suspects an error but cannot show it records the finding as `unresolved`. Findings for batches run in parallel. One reviewer then records a whole-section reconciliation covering contradictions, misapplied dates and false corroboration across batches. A changed claim, boundary, date or interpretation reopens the findings it touches.

### Run record: `runs.md`

One entry per attempt, never overwritten.

```text
run id:             <sequential within the section>
process version:    <commit SHA of this document and PLANNING.md>
input commits:      <SHAs>
output paths:       <paths>
roles and models:   <role: actual model or person, per stage>
outstanding work:   <list>
defects found:      <process defects, failed handoffs>
changes since last: <procedure changes and claims invalidated>
usage:              <tokens, time or cost where measured, else "not measured">
frontier:           <investigation record link, or "none">
```

## Shared records and invalidation

- Shared files are `research/shared/sources/`, `research/shared/chronology.md`, `research/shared/names.md` and `research/materials/`. Only the integration owner edits them. Workers propose additions in their own files. The owner deduplicates and commits.
- `research/shared/names.md` distinguishes official names, historical variants, transliterations and editorial names. A name is never reassigned to different masonry. A split or merger is documented and references are updated.
- `research/shared/chronology.md` states, for each event, the geographic extent actually established. A gate date is not a date for adjacent wall or moatwork.
- Reusing a source record in another section keeps its locators, scope and lineage. The section's own evidence record states why the source applies to that exact fabric.
- Invalidation: a changed claim reopens its evidence dependencies and its review findings. A changed identification, boundary, date, source interpretation or shared name reopens every claim in the section that depends on it, and requires a whole-section reconciliation. It also reopens other sections that cite the changed shared record. Unrelated acquisition work is not re-run.
- Concurrent workers get separate files or source bundles. Commits are made by the integration owner after checking scope and public release suitability. Name the files in each commit. The next assignment records the commit and paths.
- Material in `research/materials/` needs a recorded rights basis and credit. Restricted copies, credentials and private correspondence never enter Git.

## Human gates

1. **Inventory acceptance** permits the first pilot.
2. **First-pilot acceptance** permits the second pilot.
3. **Second-pilot acceptance** permits scaling to later sections.

Owner feedback causes agent corrections and repeated review. It is never silent acceptance, and it does not trigger an automatic third pilot. Record each approval as a workflow decision with its date. All failed attempts are preserved. The inventory uses only the existing inventory fields in PLANNING.md, so inventory work does not depend on anything here.

## Optional bounded frontier investigation

The owner approved this policy in chat. The owner did not approve any particular frontier assignment. This policy creates no standing task, no placeholder blocker and no automatic promotion. It follows the proposed approval contract in [daily-driver #577](https://github.com/jmcvetta/daily-driver/issues/577).

1. **Try ordinary routes first.** Consider frontier only for a specific consequential ambiguity about identity, boundaries, chronology or interpretation that remains after bounded ordinary research. Record the work done and why cheaper classes are insufficient for the remaining question. Difficulty, missing evidence, retry or model availability alone does not justify escalation.
2. **Propose a separate investigation.** The proposal states:
   - the exact question or decision;
   - the named sections or components;
   - inspected sources with exact locators, and the conflicting evidence;
   - any additional source search, with its limits;
   - the expected evidence-linked deliverable;
   - the proposed number of frontier sessions or passes.

   Separate known inputs from estimates and unknowns. Do not do frontier research to estimate its own scope. Give cost, time and token figures only with a measured basis. Otherwise write `unknown`.
3. **Ask the owner before the assignment is made ready or dispatched.** If the owner approves, record the approved envelope and decision in a separate research issue that links the requesting task. Link a source for the approval when one exists. If approval was given in chat only, say so and do not invent a URL. Apply the frontier class only where the active harness supports it.
4. **Approval covers only that investigation.** More passes than approved, a material scope expansion, ordinary implementation and continuing frontier supervision each need separate authorization. Do not bypass the gate through delegation, overrides, retries or fallback routing. Do not change operator model configuration.
5. **Return the findings** with exact evidence, alternatives, uncertainty and open questions to the original task's coordinator. The original class integrates them. Frontier output is not an independent historical source. It does not replace adversarial review or required competent human review. Record the investigation, findings and resulting rechecks in the research history and run record.
6. **If escalation is declined, unavailable or inconclusive,** continue unaffected work. Keep the ambiguity as an explicit supported research limit, or omit the unsupported claim. Do not force a resolution and do not weaken coverage or evidence requirements.

## Evaluation before chapter fanout

This section documents interfaces only. It does not build or run a benchmark, add a prerequisite to the initial inventory, authorize frontier use, or change operator routing. The controlled gates are defined by the [benchmark task #11](https://github.com/jmcvetta/chiang-mai-wall-book/issues/11), [first comparison #12](https://github.com/jmcvetta/chiang-mai-wall-book/issues/12) and [second-section confirmation #13](https://github.com/jmcvetta/chiang-mai-wall-book/issues/13). Those issues are authoritative for details.

### Sequence

1. The first comparison uses independently reviewed first-pilot evidence and feeds the first-pilot owner decision (gate 2).
2. The second pilot uses the accepted provisional role selections. Its independently reviewed evidence supports locked confirmation before the final owner decision (gate 3) and chapter fanout.

### Invariants

- Independently validated reference answers stay isolated from candidates.
- Scoring floors are fixed before trials. Trials are bounded by the existing trial budget.
- Each trial records the actual route identity (model, route, environment) and usage.
- Outcomes include explicit *neither qualified* and *coverage gap* results.
- Controlled evidence use is kept distinct from live-source discovery.
- The agreed procedure and the model configurations are recorded together.
- Human workflow approval cannot repair an invalid reference answer. It cannot waive a critical qualification failure.
- Results are model, route and environment comparisons. They are not isolated provider effects.

### Provider execution

- Fixture preparation and shared scoring are separate from provider execution.
- The first-round Anthropic arm ([#14](https://github.com/jmcvetta/chiang-mai-wall-book/issues/14)) and OpenAI arm ([#15](https://github.com/jmcvetta/chiang-mai-wall-book/issues/15)) each run in their designated environment.
- Shared second-section fixture preparation ([#16](https://github.com/jmcvetta/chiang-mai-wall-book/issues/16)) supplies the Anthropic confirmation arm ([#17](https://github.com/jmcvetta/chiang-mai-wall-book/issues/17)) and the OpenAI confirmation arm ([#18](https://github.com/jmcvetta/chiang-mai-wall-book/issues/18)).
- Each arm reads an **immutable common input bundle** identified by commit. Each arm writes to its own result location. Named offline checks run on the results. Adjudication is shared and provider-blind.
- Dispatch is environment-aware. An orchestrator that lacks the environment a provider arm requires reports the configuration gap on the arm's issue. It does not run both providers locally and does not change routes.

## Tracing a hypothetical handoff

This trace checks the specifications. It uses no historical content.

1. The coordinator writes `brief.md` for a section already in the reviewed inventory. The brief carries the handoff header, with `next recipient: discovery worker`.
2. A Thai-language discovery worker writes `discovery-thai.md` with entries at the *found* level and a search log. It names `next recipient: coordinator` and lists the items it could not obtain.
3. The integration owner adds a source file for one obtained source. An extraction worker inspects a passage and writes an `evidence.md` entry with locator, scope and lineage.
4. The section researcher writes ledger claims. Each cites evidence ids. A claim supported only by a copy of the same report is recorded with one lineage.
5. The editor writes the chapter. A reviewer reopens each cited locator and writes findings with all required fields. A section-level reviewer reconciles across batches.
6. The coordinator records the run in `runs.md` and the owner decides. If the decision is acceptance of the first pilot, gate 2 is recorded. A correction request starts run 2, and the earlier run stays on file.

Each recipient finds its inputs, output path, next recipient and escalation route in this document and the previous handoff header. No step needs the original planning conversation.
