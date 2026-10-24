
from project import count_characters, count_words, format_summary


def test_count_characters():
    assert count_characters("Hello") == 5
    assert count_characters("Hello World") == 10
    assert count_characters("") == 0
    assert count_characters("a\nb") == 3


def test_count_words():
    assert count_words("Hello World") == 2
    assert count_words("  Hello   World  ") == 2
    assert count_words("") == 0
    assert count_words("hello\nworld") == 2
    assert count_words("   ") == 0


def test_format_summary():
    assert format_summary("test.txt", 10, 2) == (
        "File: test.txt\n"
        "Characters: 10\n"
        "Words: 2"
    )

    assert format_summary("empty.txt", 0, 0) == (
        "File: empty.txt\n"
        "Characters: 0\n"
        "Words: 0"
    )

