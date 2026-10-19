"""First project task: read the supplied claim submission guide."""

from pathlib import Path
from medibot.chunking import split_word_chunks, build_chunk_records

PROJECT_ROOT = Path(__file__).resolve().parents[1]
# Initial ingestion allowlist: exactly one document. No directory scanning.
INITIAL_DOCUMENTS = (
    PROJECT_ROOT / "data" / "mediassist_data" / "billing" / "claim_submission_guide.md",
)


def main():
    note = INITIAL_DOCUMENTS[0]
    if not note.is_file():
        raise SystemExit(
            "Dataset missing. See README.md and run tools/prepare_data.py first."
        )
    print(note)

    text = note.read_text(encoding="utf-8")
    print(len(text))
    print(text[:200])

    print("------------------------------------")
    chunks = split_word_chunks(text, 50)
    print(len(chunks))
    print(chunks[0])

    print("------------------------------------")
    chunk_records = build_chunk_records(chunks, note.name)
    print(len(chunk_records))
    print(chunk_records[0])
    print(chunk_records[-1]["chunk_index"])


if __name__ == "__main__":
    main()
