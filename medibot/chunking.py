"""Baseline helpers written by the learner in the earlier study exercises.

Copied unchanged. Word splitting normalizes whitespace and is not the final
structure-aware chunker. Validate chunk_size when that task is introduced.
"""

def split_word_chunks(text, chunk_size):
    # Split the supplied text into words.
    # Create an empty chunks list.
    # Use your loop to build the chunks.
    # Return the list after the loop.
    words = text.split()
    chunks = []

    for start in range(0, len(words), chunk_size):
        chunk = " ".join(words[start:start+chunk_size])
        chunks.append(chunk)
    return chunks


def build_chunk_records(chunks, source_document):
    # Create an empty records list.
    # Loop over the supplied chunks with enumerate().
    # Build and append each dictionary.
    # Return the records after the loop.
    chunk_records = []

    for index, content in enumerate(chunks):
        record = {
            "content": content,
            "source_document": source_document,
            "chunk_index": index,
        }
        chunk_records.append(record)

    return chunk_records
