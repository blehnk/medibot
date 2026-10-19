"""First project task: read the supplied claim submission guide."""

from pathlib import Path
from medibot.chunking import split_word_chunks, build_chunk_records
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient, models

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

    print("------------------------------------")
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    embeddings = model.encode(chunks)
    print(embeddings.shape)
    print(embeddings[0].shape)

    print("------------------------------------")
    client = QdrantClient(":memory:")
    collection_name = "medibot_baseline"

    client.create_collection(
        collection_name=collection_name,
        vectors_config=models.VectorParams(
            size=embeddings.shape[1],  # Get the vector dimension from embeddings.shape
            distance=models.Distance.COSINE,  # Use models.Distance.COSINE
        ),
    )

    print(client.collection_exists(collection_name))

    print("------------------------------------")
    points = []

    for index, record in enumerate(chunk_records):
        point = models.PointStruct(
            id=index,
            vector=embeddings[index].tolist(),
            payload=record,
        )
        points.append(point)

    print(len(points))
    print(len(points[0].vector))
    print(points[0].payload["source_document"])

    print("------------------------------------")
    client.upsert(
        collection_name=collection_name,
        points=points,
        wait=True,
    )

    result = client.count(
        collection_name=collection_name,
        exact=True,
    )
    print(result.count)


if __name__ == "__main__":
    main()
