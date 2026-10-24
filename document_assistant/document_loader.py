from pathlib import Path


def validate(path):
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if not path.is_file():
        raise ValueError(f"Expected a file: {path}")

    if path.suffix.lower() != ".txt":
        raise ValueError(f"Unsupported file extension: {path.suffix}")


def load_text_file(filename):
    path = Path(filename)
    validate(path)

    text = path.read_text(encoding="utf-8")

    return {
        "path": str(path),
        "name": path.name,
        "text": text
    }