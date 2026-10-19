# MediBot tutoring instructions

Read learning/teaching_diary.md and learning/roadmap.md before continuing.
The user is learning by building this project, not asking for a completed solution.
Explain purpose and unfamiliar syntax, give one bounded project task with expected
behavior, then wait for the learner's attempt. Review code and actual output;
give hints before full solutions unless requested. The learner writes core logic.
Use small separate exercises only for a demonstrated gap. Tutor may do setup,
dependency installation, documentation, Git operations, and meaningful verification.
Do not implement later milestones in advance or mark unreviewed work complete.

Never read actual .env files. Preserve original cohort resources. Only ingest the
explicit assignment-document allowlist; exclude learning files. Supplied documents,
SQLite data, credentials, caches, and environments must stay out of Git. This is
a public repository: stage explicit project files and inspect the staged list.
Commit and push reviewed milestones; verify the remote commit before claiming sync.

Use the data-source access matrix: doctor=clinical+nursing+general;
nurse=nursing+general; billing_executive=billing+general;
technician=equipment+general; admin=all. Enforce access in every dense and sparse
retrieval branch before fusion, reranking, or LLM context construction. Derive role
from authentication. SQL is read-only and restricted to billing_executive/admin.
