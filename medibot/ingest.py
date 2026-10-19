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

    # TODO (learner): read UTF-8 text, print its length, and print its first 200 characters.
    # See learning/first_lesson.md. Your two existing helpers are in medibot/chunking.py.
    print("Task 1 pending: add the three statements described in learning/first_lesson.md")


if __name__ == "__main__":
    main()
