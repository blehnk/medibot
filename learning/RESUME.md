# Resume MediBot learning - 2026-10-20

## Teaching agreement

Read AGENTS.md, this note, learning/teaching_diary.md, and learning/roadmap.md.
Learning is project-first. The learner writes core logic and runs commits/pushes.
Give purpose and unfamiliar syntax, one bounded task, expected behavior, then wait
for code/output. Give hints before full solutions. Small exercises only for observed
gaps. Tutor may handle environment setup, installation, documentation, and verification.
Never read actual .env files. Nudge commits at coherent reviewed checkpoints; gradually
reduce command scaffolding. Do not perform commits for the learner unless asked.

## Current position

- Baseline in medibot/ingest.py works: one claim guide -> 50-word chunks -> metadata
  -> all-MiniLM-L6-v2 embeddings -> in-memory Qdrant -> dense retrieval -> cited context
  -> Groq completion. Expected 40 chunks, embedding shape (40, 384).
- Groq model is openai/gpt-oss-20b using the Groq SDK and GROQ_API_KEY. Earlier
  llama-3.3-70b-versatile returned model_not_found; do not switch back without checking.
- Retrieval and generation work, but answer grounding is not fully validated.
  Original question ranks reimbursement checklist chunks 15/16 at 7/9; explicit
  reimbursement question ranks them 3/1. Generation invents a bank-proof alternative
  and changes 'cancelled cheque OR passbook copy' into separate requirements.
  Stronger prompts did not fix it. A revenue question produced an expected refusal
  in one run. Preserve these examples for later comparisons; details are in the diary.
- Starting Stage 3. Docling 2.140.0 import and synthetic Markdown conversion passed
  on Windows Python 3.13.5. Dependency versions are locked in uv.lock.
- medibot/structured_ingest.py is still a TODO starter. Real document conversion
  has not been completed/reviewed. Do not advance to chunking on assumed success.
- Stages remaining: structured PDF/Markdown ingestion and metadata; hybrid dense/BM25
  fusion in Qdrant and cross-encoder reranking; explicit read-only SQL RAG; role-based
  access/authentication/FastAPI; Next.js and submission evidence. No deployment yet.
- LangChain is not installed or used yet. Learner asked about it; agreed it can be
  introduced after the structured retrieval flow is understood, using Session 4-5
  examples where useful. Specific integration is not decided. It is not mandatory
  for every component; preserve explicit SQL steps and retrieval-level access filters.

## Exact next learner task

See learning/structured_ingestion.md. Inside structured_ingest.main(): construct a
DocumentConverter, call convert(note), access result.document, print its class name,
and preview the first 400 characters of document.export_to_markdown(). Expected
DoclingDocument and claim-guide opening. Learner writes statements and shares output.
Then inspect parsed headings/list/table elements before hierarchical/token-aware chunking.
Run: uv run --locked python -m medibot.structured_ingest
No API key needed for this task. Preserve the existing baseline module for comparison.

## On the other machine

1. Clone https://github.com/blehnk/medibot or pull --ff-only an existing clone. Open
   the medibot repository itself as the workspace. Check git status before changes.
2. Install Git, uv, and Python 3.13; run uv sync --locked from the repository root.
   Recreate .venv; do not copy the Windows environment onto another machine/OS.
3. Transfer the supplied mediassist_data.zip separately using your normal private
   file-transfer method. Run:
   uv run --locked python tools/prepare_data.py "PATH/TO/mediassist_data.zip"
   Do not publish supplied PDFs/SQLite data. Keep source cohort resources unchanged.
4. Make the assignment brief and Session 3-5 resources available locally as references
   if the tutor needs to consult them; these are not included in this public repository.
5. Only for Groq answer generation, configure your own project-local .env using
   .env.example. Do not paste keys into chat or commit them. The learner runs:
   uv run --locked --env-file .env python -m medibot.ingest
6. First model imports/downloads may take time. Verify dependencies on the new OS;
   successful Windows checks do not establish another machine's compatibility.
7. Follow the same explicit document allowlist. Do not scan learning/reference files
   for ingestion. Pull before switching machines, and commit/push before switching back.

## Prompt to paste into the new chat

Read AGENTS.md, learning/RESUME.md, learning/teaching_diary.md, and learning/roadmap.md.
Inspect medibot/ingest.py and medibot/structured_ingest.py without reading any .env
files. Help verify this machine's environment and local dataset, then resume the
first Docling task in learning/structured_ingestion.md. Teach one step at a time:
I write core logic, you review attempts and give hints before solutions. I also run
my own commits and pushes; nudge me at coherent checkpoints and gradually reduce
Git command scaffolding. Do not assume the structured starter or answer grounding
is complete. Use the diary to preserve known failures and update progress after review.
