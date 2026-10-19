# MediBot teaching diary

## Goal and teaching agreement

Learn Python and AI engineering through the MediBot assignment covering Sessions
3, 4, and 5. Start building the project now. Use separate small exercises only
when a specific gap makes one useful. Learning takes priority over submission speed.

The learner writes core application logic. Explain purpose and relevant syntax,
give a small starter and expected behavior, then wait for an attempt. Review code
and output, give hints before solutions, and adapt scaffolding to demonstrated
independence. Tutor may handle environment setup, dependency installation, Git,
and documentation. Update this diary after reviewed attempts or explicit feedback.
Never read actual .env files.

## Carried-forward observations

Reviewed the earlier teaching diary and both saved exercise files in coho-spelmani.
Demonstrated in those exercises: Path and working-directory behavior; UTF-8 reading;
strings, lists, dictionaries, loops, enumerate, functions and return values;
word chunking and chunk metadata; single and batch embeddings; similarity-score
mapping; max and index; a named key function passed to sorted.

The earlier claim-guide pipeline reported 40 chunks at 50 words, with indexes 0-39.
The learner wrote split_word_chunks and build_chunk_records; these functions are
copied unchanged into medibot/chunking.py. They are a baseline, not final structured
ingestion. Their invalid-size handling has not been implemented or assessed.

Previously observed gaps to revisit in context: exclusive range/slice stops;
absolute slice end versus chunk length; list versus NumPy array; class versus
instance; dictionary key consistency. Observations are provisional, not mastery ratings.
The final sorting prediction check was not answered. Revisit when ranking real
project chunks, rather than requiring a detached exercise before starting.

## Assignment policy

Preserve supplied resources. Ingest only explicitly selected assignment files.
Follow the data-source access matrix: doctor=clinical+nursing+general;
nurse=nursing+general; billing_executive=billing+general;
technician=equipment+general; admin=all. This resolves a contradiction in the brief.
SQL is restricted to billing_executive/admin. The final project needs FastAPI and
Next.js; no intermediate UI or deployment is required.

## Checkpoint - 2026-10-19

- User approved project-first learning and a separate public blehnk/medibot repository.
- Original study repository and its history remain separate.
- Project scaffold created; only the learner's existing two helpers are implemented.
- Supplied ZIP is prepared locally through tools/prepare_data.py; data stays ignored.
- Python/uv setup and GitHub verification results are recorded after checks below.
- Next task: learning/first_lesson.md, Task 1. Learner adds UTF-8 reading and two
  diagnostic print statements in medibot/ingest.py, then shares code/output.
- Wait for that attempt. Do not implement embeddings/retrieval on the learner's behalf.

## Setup verification - 2026-10-19

- Windows CPython 3.13.5; project-local .venv created by uv, with uv.lock checked.
- Installed/imported sentence-transformers 6.1.0, qdrant-client 1.19.1, and
  torch 2.14.1+cpu. The first Sentence Transformers import took several minutes
  while Transformers scanned its modules. A separate 30-second diagnostic timed
  out during that scan; the original full import completed successfully.
- In-memory Qdrant collection creation, upsert, and query passed using a synthetic
  three-number vector. This is environment verification, not completed retrieval.
- Syntax checks, copied learner helpers, and real claim-guide chunking passed:
  12,833 characters; 40 chunks at 50 words; chunk indexes 0 through 39.
- Dataset preparation was run twice and is repeatable; originals were not changed.
- Starter command runs and explicitly reports Task 1 pending. No embedding model
  has been downloaded or encoded on this machine. No core project task reviewed yet.
- Public repository created at https://github.com/blehnk/medibot. Publish only the
  staged project files; datasets, environment files, and old study history excluded.
- First commit covers project scaffolding, setup, reusable learner code, roadmap,
  teaching agreement, and first task. Verify origin/main after pushing.
