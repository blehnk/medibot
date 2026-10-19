"""First project task: read the supplied claim submission guide."""

from pathlib import Path

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


if __name__ == "__main__":
    main()
