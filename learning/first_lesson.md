# First lesson: read a real project document

We are starting the project, not another isolated exercise. The first flow is:
claim guide -> text -> chunks -> embeddings -> Qdrant -> matching passages.
Today, take just the first step and inspect the actual text.

## Task 1

Open medibot/ingest.py. Inside main(), below the TODO comment:

1. Read note as UTF-8 and store the returned string as text.
2. Print the number of characters in text.
3. Print the first 200 characters of text.

You have used read_text(encoding="utf-8"), len(), and slicing before. The encoding
keyword tells Python how to decode file bytes. len(text) counts characters; text[:200]
returns a preview. Use those ideas to write the three statements yourself.

Run from the project root:

```powershell
uv run --locked python -m medibot.ingest
```

Expected: the document path, a positive character count, then the claim-guide title
and opening text. Character count can differ from the earlier machine if line endings
or resource versions differ. Share your code and output for review before continuing.

## How the starter finds the file

PROJECT_ROOT comes from this module's __file__, so it does not depend on the terminal's
current directory. The / operator joins Path components. The if __name__ == "__main__"
guard runs main() when you launch the module; importing it does not run the lesson.
We will unpack these details as needed rather than assume they are already familiar.

## After review

Call your existing split_word_chunks(text, 50), then build_chunk_records using the
filename. Inspect first/last records before introducing embeddings and Qdrant.
Do not implement these follow-up steps until Task 1 has been reviewed.
