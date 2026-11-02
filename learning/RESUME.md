# Resume MediBot learning - 2026-11-02

This is the current checkpoint. Earlier diary tasks are historical; do not restart
parsing or chunking. Read AGENTS.md, this note, the diary, and the roadmap.

## Teaching agreement

The learner writes core logic and performs commits/pushes. Explain purpose and new
syntax, give one bounded task and expected behavior, then wait for code/output.
Give hints before full solutions unless asked. Small exercises only for observed
gaps. Tutor may handle setup, installation, documentation, and verification.
Nudge commits at coherent reviewed checkpoints and gradually reduce Git scaffolding.
Never read actual .env files. Preserve supplied resources and explicit ingestion
allowlists. Data, credentials, environments, and caches stay out of the public repo.

## Current checkpoint and evidence

Latest inspected commits: 5ab6ff8 (create structured record.) and 8633288 (update
learning doc). Worktree was clean before this handoff; main matched locally recorded
origin/main. No live remote fetch performed here. Learner must commit/push this
handoff before switching machines.

### Original baseline: medibot/ingest.py

- Claim guide -> 50-word chunks -> 40 records -> all-MiniLM-L6-v2 embeddings
  (40,384) -> in-memory Qdrant -> dense retrieval -> cited context -> Groq answer.
- Groq uses openai/gpt-oss-20b through Groq SDK and GROQ_API_KEY. Earlier
  llama-3.3-70b-versatile failed with model_not_found for this account.
- Broad question: "What documents are required to submit an insurance claim?"
  Checklist chunks 15/16 ranked 7/9 among top 10.
- Specific question: "Which documents are required for a reimbursement claim?"
  The same chunks ranked 3/1. Checklist text was split mid-item.
- Generated answers invented an alternative bank-proof document and changed
  "cancelled cheque OR passbook copy" into separate requirements. Stronger prompts
  did not fix those examples; citation bracket formatting also differed.
- Annual-revenue question produced expected insufficient-evidence response once.
  General answer grounding/refusal reliability is NOT established.
- Preserve the baseline and these questions for comparison.

### Structured pipeline: medibot/structured_ingest.py

- Real Markdown conversion and element/table inspection reviewed. Six tables detected;
  first inspected table was 3 rows x 2 columns. No PDF ingestion implemented.
- HierarchicalChunker: 42 chunks, contextualized token maximum 240, none over 256.
- HybridChunker wraps existing embedder.tokenizer using HuggingFaceTokenizer;
  max_tokens=embedder.max_seq_length minus special-token overhead; merge_peers=True.
- Final hybrid audit: 30 chunks, maximum 249 tokens including special tokens,
  zero over 256. Audit contextualizes each chunk and encodes with
  add_special_tokens=True, truncation=False. ValueError guard blocks oversized output.
- A warning reported 258 > 256 during chunking. Exact intermediate origin untraced;
  no oversized final chunk in this audit. Do not suppress instead of validating.
- Hybrid checklist chunk 11 contains all seven requirements and intact payout
  alternative with full heading hierarchy. Find by content, not hard-coded index.
- 30 structured_records have content, embedding_text, source_document, chunk_index,
  section_title, collection, access_roles, chunk_type. Last index 29.
- content is raw text; embedding_text is contextualize(chunk), a string including
  heading context. contextualize does not embed, call an LLM, or modify the chunk.
- All current records: collection=billing, access_roles=[billing_executive,admin].
  Access metadata exists; retrieval-level permission enforcement does NOT.
- Type policy: any table label -> table; otherwise all labels code -> code;
  otherwise text. Six table records, one code record, 23 text records.
  Mixed tables/prose are summarized as table; inline code in prose remains text.
  No heading-only chunk observed; handling that case is future work.
- Checklist diagnostic uses None plus a missing-match guard.
- Structured records have NOT been embedded/indexed/queried or used in generation.
  No structured retrieval/answer improvement has been demonstrated.

## Exact next learner task

1. Verify machine setup and guide, then learner collects record["embedding_text"]
   from structured_records into a list using a familiar loop/append, preserving order.
2. Batch-encode with the existing embedder. Inspect shape (30,384), first row (384,),
   and one vector per record. Explain why dictionaries/raw content are not the chosen
   embedding input. Wait for learner code/output before indexing.
3. Then teach points/upsert in a separate in-memory Qdrant collection named
   medibot_structured_baseline; verify 30 stored points and aligned payloads.
4. Retrieve using the SAME baseline questions/model/settings, compare expected-source
   ranks and text, then inspect Groq answers/citations if generation is added.
   Do not infer improvement from fewer chunks alone.

No Groq key needed for the next embedding/indexing task. Do not fill in core logic
or refactor the whole pipeline for the learner. Model limit 256 is input tokens;
384 is output vector dimensions. These were explained; reinforce in context.

## Remaining project

Structured retrieval comparison, allowlisted PDF ingestion, table/metadata/token
verification across documents, general document-to-policy mapping; dense+BM25 fusion
inside Qdrant and cross-encoder reranking; explicit read-only SQL RAG; authenticated
roles and retrieval filters; FastAPI; Next.js; evaluation evidence/submission docs.
Deployment deferred. LangChain is not yet used; possible Session 4-5 integrations
were discussed, but specific usage remains undecided.

Access matrix: doctor=clinical+nursing+general; nurse=nursing+general;
billing_executive=billing+general; technician=equipment+general; admin=all.
SQL only billing_executive/admin. Filter all dense/sparse retrieval branches before
results reach application/LLM; derive role from authentication.

## Other-machine setup

1. Clone https://github.com/blehnk/medibot or check status and pull --ff-only an
   existing clone. Open the MediBot repo itself as the workspace.
2. Install Git, uv, Python 3.13; run `uv sync --locked`. Recreate .venv rather than
   copying it. Verify imports on the actual OS.
3. Transfer supplied mediassist_data.zip privately and run:
   `uv run --locked python tools/prepare_data.py "PATH/TO/mediassist_data.zip"`.
   Tool prepares 13 allowlisted files. Data and SQLite stay local.
4. Keep assignment brief and Session 3-5 materials available locally for reference;
   those resources are not included in this public repo.
5. Run `uv run --locked python -m medibot.structured_ingest`; expect final audit
   30/249/0 and 30 records. Imports/model downloads can take time.
6. Only for Groq generation, configure a local .env from .env.example and run
   `uv run --locked --env-file .env python -m medibot.ingest`. Do not share keys.
7. CPU Torchvision is locked alongside CPU Torch after a Linux torchvision::nms/CUDA
   mismatch. Use current lockfile, not historical install instructions.
8. Commit/push before changing machines; pull before continuing elsewhere.

## Prompt for the new chat

Read AGENTS.md, learning/RESUME.md, learning/teaching_diary.md, and learning/roadmap.md.
Inspect current code without reading any .env files. Verify this machine's environment
and local dataset, then resume RESUME.md's exact next task: embedding the validated
structured records. Parsing, token-aware chunking, and metadata have already been
reviewed. Teach one step at a time; I write core logic and run commits/pushes. Review
attempts and give hints before solutions. Preserve the original baseline and known
grounding failures for comparison. Update the diary and resume checkpoint after reviews.
