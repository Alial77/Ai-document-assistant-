import re
import pytest
from document_assistant.document_loader import validate, load_text_file


def test_validate_valid_file(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("Hello world", encoding="utf-8")

    assert validate(file) is None


def test_validate_missing_file(tmp_path):
    file = tmp_path / "missing.txt"

    with pytest.raises(FileNotFoundError):
        validate(file)


def test_validate_directory(tmp_path):
    with pytest.raises(ValueError, match="Expected a file"):
        validate(tmp_path)


def test_validate_wrong_extension(tmp_path):
    file = tmp_path / "test.pdf"
    file.write_text("content", encoding="utf-8")

    with pytest.raises(ValueError, match="Unsupported file extension"):
        validate(file)


def test_validate_uppercase_extension(tmp_path):
    file = tmp_path / "test.TXT"
    file.write_text("Hello", encoding="utf-8")

    assert validate(file) is None


def test_load_text_file(tmp_path):
    file = tmp_path / "test.txt"
    file.write_text("Hello world", encoding="utf-8")

    document = load_text_file(file)

    assert document["path"] == str(file)
    assert document["name"] == "test.txt"
    assert document["text"] == "Hello world"


def test_load_empty_file(tmp_path):
    file = tmp_path / "empty.txt"
    file.write_text("", encoding="utf-8")

    document = load_text_file(file)

    assert document["text"] == ""


def test_load_invalid_utf8(tmp_path):
    file = tmp_path / "invalid.txt"
    file.write_bytes(b"\xff\xfe\xfa")

    with pytest.raises(UnicodeDecodeError):
        load_text_file(file)


def test_load_missing_file(tmp_path):
    file = tmp_path / "missing.txt"

    with pytest.raises(FileNotFoundError):
        load_text_file(file)


def test_load_wrong_extension(tmp_path):
    file = tmp_path / "document.pdf"
    file.write_text("PDF content", encoding="utf-8")

    with pytest.raises(ValueError, match="Unsupported file extension"):
        load_text_file(file)


def test_missing_file_error_message_contains_path(tmp_path):
    file = tmp_path / "missing.txt"

    with pytest.raises(
        FileNotFoundError,
        match=re.escape(str(file))
    ):
        validate(file)


def test_missing_pdf_raises_file_not_found_first(tmp_path):
    file = tmp_path / "missing.pdf"

    with pytest.raises(
        FileNotFoundError,
        match=re.escape(str(file))
    ):
        validate(file)


def test_load_non_ascii_text(tmp_path):
    file = tmp_path / "arabic.txt"
    content = "Hello, café! مرحبًا بالعالم"

    file.write_text(content, encoding="utf-8")

    document = load_text_file(file)

    assert document["text"] == content
