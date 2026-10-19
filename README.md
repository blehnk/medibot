# MediBot

A learning implementation of the Codebasics MediBot assignment. We build the
application in small reviewed steps, starting with a single claims document.
**Status: project setup and first ingestion lesson; no working RAG application yet.**

The final target is structured ingestion, role-filtered hybrid retrieval,
cross-encoder reranking, cited cloud-LLM answers, SQL RAG, FastAPI, and Next.js.
See [the roadmap](learning/roadmap.md) and [teaching diary](learning/teaching_diary.md).

## Set up

Install Git, Python 3.13, and [uv](https://docs.astral.sh/uv/getting-started/installation/).
Clone this repository, open its root in a terminal, then run:

```powershell
git clone git@github.com:blehnk/medibot.git
cd medibot
uv sync --locked
```

The project uses CPU PyTorch and a project-local .venv. uv.lock captures resolved
dependencies. Embedding models download separately on their first actual use.
No API key is needed for the first lesson. LLM configuration comes later.
The first Sentence Transformers import can take several minutes on this Windows machine;
setup verified that it completes, along with an in-memory Qdrant query.

Obtain the supplied mediassist_data.zip separately from your cohort resources:

```powershell
uv run --locked python tools/prepare_data.py "PATH/TO/mediassist_data.zip"
uv run --locked python -m medibot.ingest
```

The preparation tool copies only the 12 assignment documents and supplied SQLite
database into ignored data/mediassist_data. Original resources stay unchanged.
It will not overwrite a differing local file. Do not add these resources to Git.
The ingestion command initially prints the document path and the pending task;
you will implement text reading in the first lesson.

## Learning and syncing

Read learning/first_lesson.md. You write the core application logic; the tutor
explains, reviews, and handles setup. The old exercises remain in the separate
study repository; this project includes only the two reusable functions you wrote.

On another computer: clone, run uv sync --locked, and transfer the dataset separately.
Pull with git pull --ff-only before editing; commit and push reviewed milestones
before changing machines. Do not edit the same files simultaneously on two machines.
Git syncs files and teaching checkpoints, not the original chat.

## Final assignment contract

- Docling structural parsing with token-aware hierarchical chunks and heading context.
- Dense and BM25 vectors indexed together; Qdrant-side fusion, then cross-encoder reranking.
- Access filters on both retrieval branches, before any result reaches the application.
- Cloud-LLM answers supported by citations; explicit handling of insufficient evidence.
- Plain sql_rag_chain(question: str) -> str: generate SQL, extract SQL, execute read-only,
  then generate an answer from results. Restricted to billing_executive and admin.
- FastAPI: POST /login, POST /chat, GET /collections/{role}, GET /health.
- Chat response: answer, sources, retrieval_type (hybrid_rag or sql_rag), authenticated role.
- Next.js: five demo roles, login, sources, permitted collections, retrieval type, refusals.

The brief contradicts itself about doctors accessing nursing documents. We follow
its data-source table: doctors get clinical, nursing, and general; nurses get nursing
and general. No login, API, UI, or role enforcement has been implemented yet.

## Verification and submission

Before calling the assignment complete, document dense/hybrid/reranked comparisons,
four independently checked SQL answers, and at least three adversarial access attempts
with screenshots. Verify citations, insufficient evidence, ingestion repeatability,
and all five roles. Setup commands above are not evidence of assignment completion.

Dependency setup follows [uv's CPU PyTorch guide](https://docs.astral.sh/uv/guides/integration/pytorch/).
