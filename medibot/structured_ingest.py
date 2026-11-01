"""Stage 3: inspect structural document parsing before adding chunking."""

from pathlib import Path

from docling.document_converter import DocumentConverter
from docling_core.transforms.chunker.hierarchical_chunker import HierarchicalChunker
from sentence_transformers import SentenceTransformer
from docling.chunking import HybridChunker
from docling_core.transforms.chunker.tokenizer.huggingface import HuggingFaceTokenizer

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

    print("-------------------------------")
    chunker = HierarchicalChunker()
    structured_chunks = list(chunker.chunk(dl_doc=document))
    print(len(structured_chunks))
    print(structured_chunks[0].text)
    print(structured_chunks[0].meta.headings)

    print("-------------------------------")
    embedder = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    print(embedder.max_seq_length)

    print("-------------------------------")
    for index, chunk in enumerate(structured_chunks):
        if "Cancelled cheque" in chunk.text:
            print(index)
            print(chunk.text)
            print(chunk.meta.headings)
            embedding_text = chunker.contextualize(chunk)
            print(embedding_text)
            token_ids = embedder.tokenizer.encode(
                embedding_text,
                add_special_tokens=True,
            )
            print(len(token_ids))

    print("-------------------------------")
    token_counts = []
    exceeded_count = 0
    for index, chunk in enumerate(structured_chunks):
        embedding_text = chunker.contextualize(chunk)
        token_ids = embedder.tokenizer.encode(
            embedding_text,
            add_special_tokens=True,
        )
        token_counts.append(len(token_ids))
        if len(token_ids) > embedder.max_seq_length:
            print(index)
            print(len(token_ids))
            print(chunk.meta.headings)
            exceeded_count += 1

    print("-------------------------------")
    print(
        f"Number of counts: {len(token_counts)}\nLargest count: {max(token_counts)}\nCounts exceeding model limit: {exceeded_count}"
    )

    print("-------------------------------")
    special_tokens = embedder.tokenizer.num_special_tokens_to_add(pair=False)

    tokenizer = HuggingFaceTokenizer(
        tokenizer=embedder.tokenizer,
        max_tokens=embedder.max_seq_length - special_tokens,
    )

    hybrid_chunker = HybridChunker(
        tokenizer=tokenizer,
        merge_peers=True,
    )

    hybrid_chunks = list(hybrid_chunker.chunk(dl_doc=document))
    print(len(hybrid_chunks))

    token_counts = []
    exceeded_count = 0
    for index, chunk in enumerate(hybrid_chunks):
        embedding_text = hybrid_chunker.contextualize(chunk)
        token_ids = embedder.tokenizer.encode(
            embedding_text,
            add_special_tokens=True,
            truncation=False,
        )
        token_counts.append(len(token_ids))
        if len(token_ids) > embedder.max_seq_length:
            print(index)
            print(len(token_ids))
            print(chunk.meta.headings)
            exceeded_count += 1

    print("-------------------------------")
    print(
        f"Number of counts: {len(token_counts)}\nLargest count: {max(token_counts)}\nCounts exceeding model limit: {exceeded_count}"
    )

    print("-------------------------------")
    for index, chunk in enumerate(hybrid_chunks):
        if "Cancelled cheque" in chunk.text:
            print(index)
            print(chunk.text)
            print(chunk.meta.headings)
            embedding_text = hybrid_chunker.contextualize(chunk)
            print(embedding_text)

    if exceeded_count > 0:
        raise ValueError(
            f"{exceeded_count} chunks exceed the model's {embedder.max_seq_length}-token input limit."
        )
    print("All hybrid chunks fit the embedding model's input limit.")


if __name__ == "__main__":
    main()
