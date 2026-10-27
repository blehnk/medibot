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

    converter = DocumentConverter()

    result = converter.convert(note)
    document = result.document

    print(type(document).__name__)
    print(document.export_to_markdown()[:400])


    print("-------------------------------")
    for index, (item, level) in enumerate(document.iterate_items()):
        if index >= 15:
            break

        print(type(item).__name__, item.label, level)
        print(getattr(item, "text", ""))


    print("-------------------------------")
    print(len(document.tables))
    table = document.tables[0]
    print(table.data.num_rows)
    print(table.data.num_cols)
    print(table.export_to_markdown(doc=document))

if __name__ == "__main__":
    main()
