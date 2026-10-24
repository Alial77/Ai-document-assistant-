# AI Document Assistant

A Python command-line application that loads text documents, and will grow into a tool that searches them and answers questions grounded in their contents.

## Current status: Day 1

The project can currently load a `.txt` file, validate it, and print a summary with its name, character count, and word count.

### Features

- Loads UTF-8 `.txt` files from the command line
- Validates input and reports clear errors for a missing file, a folder instead of a file, an unsupported extension, or a file that isn't valid UTF-8
- Counts characters (excluding spaces) and words
- Returns each document as a dictionary containing its path, name, and text, so later stages can cite where a passage came from

### Usage

```
python project.py documents/sample.txt
```

Example output:

```
File: sample.txt
Characters: 1200
Words: 210
```

### Project structure

- `project.py`: command-line entry point with `main`, `count_characters`, `count_words`, and `format_summary`
- `test_project.py`: tests for the functions in `project.py`
- `document_assistant/document_loader.py`: file validation and loading
- `tests/test_document_loader.py`: tests for the loader
- `documents/`: sample documents

### Design decisions

- The loader raises exceptions instead of printing errors, so it can be tested. `main()` catches them and shows a friendly message.
- Counting functions return numbers, and `format_summary` builds the output text, so each can be tested with a plain assertion.
- Characters are counted without regular spaces. Newlines are included.

### Running the tests

```
pip install -r requirements.txt
pytest
```

## Roadmap

PDF extraction, text cleaning, chunking, keyword search, embeddings, and retrieval-augmented answers with citations.