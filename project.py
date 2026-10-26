import sys
from document_assistant.document_loader import load_text_file
from document_assistant.text_processor import clean_text


def count_characters(text):
    characters = len(text.replace(" ", ""))
    return characters


def count_words(text):
    words = len(text.split())
    return words


def format_summary(name, characters , words):
    return(f"File: {name}\nCharacters: {characters}\nWords: {words}")
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python project.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        document = load_text_file(filename)


    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    except UnicodeDecodeError:
        print("Error: The file could not be decoded as UTF-8.")
        sys.exit(1)

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    text = document["text"]
    name = document["name"]
    clean_text(text)
    words = count_words(text)
    characters = count_characters(text)

    print(format_summary(name,characters,words))
    print("-" * 40)
    print(text)
    print("-" * 40)


if __name__ == "__main__":
    main()
