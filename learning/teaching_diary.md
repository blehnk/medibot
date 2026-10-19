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

## Learner feedback - commit practice - 2026-10-19

- Learner wants to perform commits and pushes personally, with tutor nudges when a
  coherent reviewed change is ready. This overrides earlier automatic commit/push guidance.
- Initially explain status, diff, explicit staging, staged diff review, commit messages,
  and push commands. Gradually move from exact commands to learner-proposed file selection,
  messages, and independent execution. Discuss branches and pull requests when useful.
- Commit scope: one clear purpose, runnable/reviewed behavior or a coherent documentation
  change; not every edit and not only at the end of a large stage. Avoid mixing unrelated work.
- First expected code checkpoint: claim-guide reading, character count, and preview work
  and are reviewed. Possible message: Read claim guide and preview its contents.
- The tutor updated AGENTS.md and this diary to preserve this preference. These changes
  are uncommitted for the learner to review; no commit or push performed for this update.
- GPT-6.1 Sol at medium reasoning is the learner's current setup; retain it as the default.
- First ingestion task remains pending; wait for learner code/output.

## Reviewed ingestion Task 1 - 2026-10-19

- Saved ingest.py and learner-provided output reviewed: correct UTF-8 read_text,
  len(text), and text[:200], indented inside main(). Reported 12,833 characters
  and the expected claim-guide heading. Task 1 complete.
- Before committing, learner should remove completed TODO comments and the commented
  pending-task print block; keep the working read/length/preview statements.
- First guided commit: inspect status/diff, stage only medibot/ingest.py, review the
  staged diff, commit with 'Read claim guide and preview its contents', then push.
- AGENTS.md and diary changes describe tutoring preferences/progress and should be
  reviewed and committed separately from application code. Learner runs Git commands.
- Next code task after commit review: import and call split_word_chunks(text, 50),
  store document_chunks, inspect count and first chunk; then build metadata records.
  Do not implement it before the learner's attempt.

## First learner commit reviewed - 2026-10-19

- Learner ran commit and push personally. Shared output shows cc1dea3 pushed to
  origin/main; local log confirms that commit. Saved ingestion file has the completed
  TODO and pending-task block removed and retains the correct three statements.
- Completed one guided application-code commit. Do not assume independent command
  selection yet; progressively ask learner to choose scope/message on later commits.
- Next bounded task: explain the import from medibot.chunking, then learner calls
  split_word_chunks with text and size 50, stores document_chunks, and prints its
  length and first item. Expected 40 chunks and document-title opening. Wait for attempt.
- Metadata construction follows after chunk output review; no immediate commit is
  required for every substep. Target next coherent commit at chunking plus metadata.

## Reviewed document chunking - 2026-10-19

- Saved ingest.py and learner-provided output reviewed: correct import and call to
  split_word_chunks(text, 50), list length, and first-item lookup. Output is 40 and
  expected title-opening chunk. Learner uses chunks, a valid equivalent variable name;
  no renaming is required. Split/join normalizes whitespace, visible in the output.
- Next task: import the existing build_chunk_records, call with chunks and note.name,
  store document_records, and inspect record count, first record, and last chunk_index.
  Expected 40, first record with source_document and chunk_index 0, final index 39.
- Explain content versus source metadata and the role of source_document in future
  citations. Do not assign section titles to fixed-word chunks. Wait for learner attempt.
- Once reviewed, prompt learner to propose the next commit message and guide explicit
  staging of application changes. Keep tutoring-document changes a separate commit.

## Reviewed chunk metadata - 2026-10-19

- Saved ingest.py correctly imports and calls build_chunk_records(chunks, note.name),
  stores chunk_records, and prints len(chunk_records), the first record, and last
  chunk_index. Learner output shows 40, expected source/content/index 0, and 39.
- Pasted snippet had print(chunk_records), inconsistent with numeric output, but
  saved file correctly uses len(chunk_records). No code correction needed.
- File-to-text-to-chunks-to-metadata pipeline is now connected in the project.
- Ready for learner's second application commit. Ask learner to propose a descriptive
  message; review status/diff, explicitly stage medibot/ingest.py, inspect staged diff,
  commit, and push. Tutor does not perform the commit. Keep docs changes separate.
- Next teaching step after commit review: encode actual chunk contents, preserving
  positional alignment with metadata. Explain batch input/output before learner attempt.

## Second learner commit reviewed - 2026-10-19

- Learner chose 'Create chunks with metadata' and personally committed/pushed e3c400a.
  Shared push output confirms origin/main advancement; local log also checked.
- Message appropriately describes the coherent application change. Learner has now
  executed two guided commits and selected the second message independently.
- Next bounded task: import SentenceTransformer, construct the previously used
  sentence-transformers/all-MiniLM-L6-v2 model, batch-encode chunks into embeddings,
  and inspect embeddings.shape and embeddings[0].shape. Expected (40, 384) and (384,).
- Explain that encode accepts list[str], not the metadata dictionaries; output row i
  corresponds to chunks[i] and chunk_records[i]. Keep metadata separately.
- Model weights may download on first construction here. First import was slow on
  this Windows machine during setup. No project embedding inference yet reviewed.
- Wait for learner code/output before point construction or Qdrant indexing.

## Reviewed real-document embeddings - 2026-10-19

- Saved code and learner output reviewed: constructs all-MiniLM-L6-v2, batch-encodes
  chunks, prints shapes (40, 384) and (384,). Correct real-document embeddings;
  inference now confirmed by learner on this machine. Records remain separately aligned.
- Next task: introduce Qdrant collection, vector size versus number of points, and
  cosine metric. Use QdrantClient(":memory:") first, explicitly temporary each run.
  Learner fills collection configuration size from embeddings.shape[1] and cosine
  distance, creates medibot_baseline, and prints collection_exists result (True).
- Installed Qdrant create_collection and VectorParams signatures checked read-only.
- No points inserted yet; point construction/upsert follows after collection review.
  Persisted storage and repeatable ingestion follow later. No commit performed.

## Reviewed Qdrant collection creation - 2026-10-19

- Saved code and learner output reviewed: correct in-memory client, collection name,
  VectorParams size=embeddings.shape[1], cosine metric, and collection_exists=True.
- Next task: build points with enumerate(chunk_records). Introduce PointStruct fields:
  id=index, vector=matching embeddings row converted with .tolist(), payload=record.
  Give loop/constructor scaffold, let learner fill fields and append.
- Inspect len(points)=40, len(points[0].vector)=384, and first payload filename before
  inserting. Emphasize index alignment; constructing points does not store them yet.
- Upsert and count follow after review. Target next commit at working baseline indexing;
  no commit or push performed by tutor.

## Reviewed Qdrant point construction - 2026-10-19

- Saved code and learner output reviewed: correct enumerate(chunk_records),
  PointStruct id=index, embeddings[index].tolist(), payload=record, and append.
  Output: 40 points, first vector length 384, expected source filename.
- Next task: explain upsert (insert absent IDs, replace existing IDs) and wait=True.
  Learner calls client.upsert with collection_name and points; then client.count
  with exact=True, inspecting returned CountResult.count. Expected stored count 40.
- Installed upsert/count signatures inspected. In-memory collection remains temporary.
- After successful insertion review, prompt learner to propose commit scope/message
  for real-document embeddings plus baseline Qdrant indexing before query retrieval.
- No application code edited and no commit/push performed by tutor.

## Reviewed baseline Qdrant indexing - 2026-10-19

- Saved upsert/count code and learner output reviewed: correct collection_name,
  points, wait=True, exact=True, and CountResult.count=40. Indexing checkpoint complete.
- This verifies stored count in the temporary in-memory collection; no retrieval query
  or disk persistence implemented yet. Stage 1 retrieval is not complete.
- Ready for learner-run commit of embeddings and baseline indexing in medibot/ingest.py.
  Ask learner to choose message and recall review/stage/commit/push commands, offering
  help as needed. AGENTS.md and diary remain a separate documentation change.
- Next task after commit review: encode a real claim-related question with the same
  model, query Qdrant for top 3 points, and inspect scores and source/content payloads.
- No application edits, commit, or push performed by tutor.

## Third learner commit reviewed - 2026-10-19

- Learner committed/pushed 0ed92a7 with message 'Create embeddings and store
  chunk_records with it in a Qdrant collection'. Shared push output confirms main
  advancement; local log matches. Message is accurate; offered a shorter future
  alternative without requesting a rewrite of published history.
- Learner performed the commit after a workflow reminder without exact commands
  being supplied in the preceding response; intermediate review/staging steps were
  not shown, so do not assume they were independently completed.
- Next bounded task: encode question 'What documents are required to submit an
  insurance claim?' with the same model; fill query_points scaffold using the
  collection, query vector converted to list, limit=3, with_payload=True.
- Inspect response.points length and each hit's score, source_document, chunk_index,
  and content. Explain response versus points list and hit attributes versus payload
  dictionary lookup. Cosine scores are similarity, not confidence probabilities.
- Installed query_points signature checked. Wait for attempt and relevance review
  before declaring Stage 1 retrieval complete or adding answer generation.

## Reviewed first retrieval and relevance - 2026-10-19

- Saved query code and learner output reviewed: same-model question embedding,
  query_points(limit=3, with_payload=True), response.points iteration, score and
  payload inspection all correct. Returned chunks 33, 17, 6 at approximately
  0.554, 0.483, 0.477; sources and chunk indexes present.
- query=query_embedding is valid: installed query_points accepts NumPy arrays as
  well as lists. Earlier .tolist guidance was optional; remove inaccurate comment
  claiming conversion when no conversion is performed. No forced conversion needed.
- Retrieval runs but answer evidence is incomplete: top passages give general
  compliance, a deadline/checklist handoff, and a truncated pre-authorisation list.
- Inspected supplied guide: reimbursement section 2.1 (lines 107-115) contains the
  relevant full checklist; question itself is broad across claim types. Do not call
  similarity scores confidence or infer precise cause of ranking from this run.
- Next bounded diagnostic: keep question/model/chunking unchanged, increase limit
  from 3 to 10, inspect whether reimbursement checklist passages enter candidates
  and report ranks/chunk indexes. Broadening candidates does not improve top-3 order.
- Wait for output before deciding next change. Preserve this mixed-result baseline
  for later structural chunking, hybrid search, and reranking comparisons.
- No application edits, commit, or push performed by tutor.

## Reviewed top-10 baseline retrieval - 2026-10-19

- Saved file confirms same question/model/chunking with only limit increased to 10.
- Learner's returned chunk indexes by rank: [33, 17, 6, 7, 1, 24, 15, 25, 16, 18].
  Reimbursement checklist chunk 15 appears at rank 7 (score ~0.42505); continuation
  chunk 16 at rank 9 (~0.40661). Top 3 unchanged. Evidence is present among broader
  candidates but poorly ranked for the reimbursement interpretation of this broad query.
- Visible boundary: chunk 15 ends 'Cancelled cheque or', chunk 16 begins 'passbook
  copy for payout'. Fixed-word splitting cuts an item and omits its section heading
  from the continuation. These observations motivate later structure-aware chunking
  and reranking; they do not establish how much each later method will improve results.
- Baseline document-to-query retrieval is implemented, with known relevance limits.
  Do not equate this with a complete answer pipeline or final-quality retrieval.
- Next controlled check: change only question to 'Which documents are required for a
  reimbursement claim?', keep limit=10/model/chunks unchanged, and report ranks of
  chunks 15 and 16. This checks query specificity, not an automated retrieval fix.
- Preserve broad-query results for comparison. After review, commit baseline retrieval
  before building cloud-LLM answers. Learner performs all commits/pushes.

## Reviewed query-specificity comparison - 2026-10-19

- Saved question is 'Which documents are required for a reimbursement claim?';
  original broad query remains as a comment. Limit remains 10.
- Learner output ranks [16, 33, 15, 18, 17, 24, 3, 25, 37, 1]. Chunk 16 moves
  from rank 9 to 1 (score ~0.54398); chunk 15 from rank 7 to 3 (~0.51373).
- Both reimbursement checklist chunks now occur in top 3. This single comparison
  supports sensitivity to query specificity, not general retrieval-quality improvement.
  Unrelated audit guidance still ranks second and the split checklist remains.
- Stage 1 baseline retrieval checkpoint complete: real question returns ranked
  passages and source/index metadata; no generated answer or final-quality guarantee.
- Ask learner to perform application commit independently for baseline retrieval in
  medibot/ingest.py, choose scope/message, inspect staged diff, and push. Then guide
  a separate documentation commit for AGENTS.md and diary, which have accumulated
  tutoring preferences and evaluation evidence and should be synced across machines.
- Stage 2 follows after commit review: build cited context from retrieved passages,
  then introduce a cloud LLM provider/configuration without reading .env contents.
- Tutor has not edited core code or performed commits/pushes.
