from document_assistant.text_processor import clean_text

def test_collapse_spaces():
    assert clean_text("hello   world") == "hello world"
    assert clean_text("hello world") == "hello world"
    
    
def test_extra_lines():    
    assert clean_text("a\r\nb") == "a\nb"
    assert clean_text("a\rb") == "a\nb"
    assert clean_text("a\tb") == "a b"
    assert clean_text("a\t\tb") == "a b"
    assert clean_text("a\t\t\tb") == "a b"
    assert clean_text("a \nb") == "a\nb"
    assert clean_text("a   \nb   \nc") == "a\nb\nc"
    assert clean_text("a \r\nb") == "a\nb"
    assert clean_text("a\n\n\nb") == "a\n\nb"
    assert clean_text("a\n\n\n\n\nb") == "a\n\nb"
    assert clean_text("a\n\nb") == "a\n\nb"
    assert clean_text("a\nb") == "a\nb"
    assert clean_text("a\n\n\nb\n\n\nc") == "a\n\nb\n\nc"
    assert clean_text("a\r\n\r\n\r\nb") == "a\n\nb"
    assert clean_text("a\n  b") == "a\nb"
    assert clean_text("\n\nhi\n\n") == "hi"