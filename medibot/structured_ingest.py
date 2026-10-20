"""Stage 3: inspect structural document parsing before adding chunking."""

from pathlib import Path

from docling.document_converter import DocumentConverter

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INITIAL_DOCUMENTS = (
    PROJECT_ROOT / "data" / "mediassist_data" / "billing" / "claim_submission_guide.md",
)


def main():
    note = INITIAL_DOCUMENTS[0]
    if not note.is_file():
        raise SystemExit("Dataset missing. See README.md to prepare the local data.")
    print(note)

    # TODO (learner): construct DocumentConverter as converter.
    # Call converter.convert(note), storing the result as result.
    # Get result.document and store it as document.
    # Print type(document).__name__ and a 400-character Markdown export preview.
    print("Structured parsing task pending. See learning/structured_ingestion.md")


if __name__ == "__main__":
    main()
