# Structured ingestion: first task

The existing ingest.py is a working baseline with recorded answer-quality failures.
Its fixed 50-word chunks can cut list items and separate content from headings.
Docling converts source files into a structured document model. Parsing and chunking
are separate steps: first inspect the parsed document, then add hierarchical,
token-aware chunking and compare results on the same questions.

## Parse the claim guide

Complete the TODOs inside main() in medibot/structured_ingest.py:

1. Construct DocumentConverter() and assign it to converter.
2. Call converter.convert(note), storing its returned conversion result as result.
3. Assign result.document to document.
4. Print type(document).__name__.
5. Call document.export_to_markdown() and print its first 400 characters.

DocumentConverter is the class; converter is the object you construct. convert()
returns a conversion result, and .document accesses its parsed document. The
Markdown export is a human-readable preview; the document object retains structure
for subsequent chunking. type(document).__name__ prints the class name.

Run from the project root:

```powershell
uv run --locked python -m medibot.structured_ingest
```

Expected: DoclingDocument, then an export beginning with the claim-guide title.
Export formatting may differ from the original Markdown. No Groq call or API key is
needed here. Share your code/output before inspecting heading/list/table objects.
Keep original supplied files unchanged. This starter processes exactly one file.

References: https://docling-project.github.io/docling/getting_started/quickstart/
and https://docling-project.github.io/docling/usage/supported_formats/.
