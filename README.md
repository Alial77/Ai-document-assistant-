# AI Document Assistant

A Python command-line application that loads text documents, cleans them, and will grow into a tool that searches them and answers questions grounded in their contents.

## Current status

Days 1 and 2 are complete. The program can load a `.txt` file, clean its text, and print a summary with the file name, character count, and word count.

## Features

- Loads UTF-8 `.txt` files from the command line
- Reports clear errors for a missing file, a folder instead of a file, an unsupported extension, or a file that isn't valid UTF-8
- Cleans messy whitespace before counting (see below)
- Counts characters (excluding spaces) and words on the cleaned text
- Returns each document as a dictionary with its path, name, and text, so later stages can cite where a passage came from

## Usage

```
python project.py documents/sample.txt
```

Example output (replace with your own real output):

```
File: sample.txt
Characters: 1200
Words: 210
```

## Text cleaning

`clean_text` applies these rules, in order:

1. Runs of tabs become a single space
2. Runs of two or more spaces become a single space
3. Windows (`\r\n`) and old Mac (`\r`) line endings become `\n`
4. Trailing spaces at the end of each line are removed
5. Leading spaces (indentation) at the start of each line are removed
6. Three or more newlines in a row become one blank line, so paragraph breaks survive
7. Whitespace at the start and end of the whole text is removed

Capitalization, punctuation, and word order are never changed, so passages can be quoted back accurately later.

## Project structure

- `project.py`: command-line entry point with `main`, `count_characters`, `count_words`, and `format_summary`
- `test_project.py`: tests for the functions in `project.py`
- `document_assistant/document_loader.py`: file validation and loading
- `document_assistant/text_processor.py`: text cleaning
- `tests/`: tests for the loader and the text cleaner
- `documents/`: sample documents

## Design decisions

- The loader raises exceptions instead of printing errors, so it is easy to test. `main()` catches them and shows a friendly message.
- Counting functions return numbers, and `format_summary` builds the output string, so each can be tested with a plain assertion.
- Characters are counted without regular spaces. Newlines are included.
- Cleaning is a separate function that takes text and returns text. It knows nothing about files or the command line.
- Every cleaning rule has a test that fails if the rule is removed.

## Running the tests

```
pip install -r requirements.txt
pytest
```

## Roadmap

- Most common words (Day 3)
- PDF extraction with PyMuPDF, including odd whitespace such as non-breaking spaces (Day 5)
- Text chunking
- Keyword search
- Embeddings and retrieval-augmented answers with citations