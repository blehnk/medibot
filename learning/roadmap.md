# Project-first roadmap

Every stage is divided into small learner-written tasks. Explain purpose and new
syntax before each task; review actual code/output before advancing. Commit and
push coherent reviewed milestones. Keep unresolved questions and the next task in
the teaching diary. No stage below is complete merely because its files exist.

| Stage | Build | Acceptance |
| --- | --- | --- |
| 1 | Claim-guide reading, baseline chunks, embeddings, local Qdrant | A real question returns ranked passages with sources |
| 2 | Cloud-LLM answers with citations | Sources support claims; missing evidence is acknowledged |
| 3 | Docling and token-aware hierarchical chunks | Tables/headings survive; parent context and metadata are complete |
| 4 | Dense + BM25 indexed together, Qdrant fusion, cross-encoder reranking | Same-question dense/hybrid/reranked comparison; broad candidates narrow before prompting |
| 5 | Inspect SQLite, practise SQL, build explicit SQL RAG function | Four analytical answers match independently executed read-only SQL |
| 6 | Authentication, role filters, FastAPI | Five roles; filters in both retrieval branches; restricted SQL blocked |
| 7 | Next.js and submission evidence | Login, citations, collections, retrieval labels, refusal messages, documented adversarial tests |

## Stable interfaces

Baseline records: content, source_document, chunk_index. Structured ingestion adds
collection, access_roles, section_title, chunk_type (text/table/heading/code).
Do not infer section titles from a separate headings list for fixed word chunks;
a fixed chunk can cross section boundaries.

Final API: POST /login, POST /chat, GET /collections/{role}, GET /health. Chat uses
the role from the authenticated token and returns answer, sources (source_document,
section_title, collection), retrieval_type (hybrid_rag/sql_rag), and role.

SQL RAG is a plain sql_rag_chain(question: str) -> str function with explicit
question-to-SQL, SQL extraction/execution, and result-to-answer steps. Enforce
read-only database access; only billing_executive/admin may invoke the SQL route.

## Verification at the appropriate stage

Check chunk count/content/index mapping and source metadata, repeatable indexing,
retrieval relevance and ranking, cited support and unanswerable questions, structural
parsing of tables, and same-query retrieval comparisons. Verify all role boundaries,
at least three adversarial prompts (with submission screenshots), four SQL examples,
and token-derived identity. Never pass the full candidate set after reranking.

Defer deployment. Introduce and verify dependencies when their stage starts.
