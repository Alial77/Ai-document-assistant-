import re

def clean_text(text):
    cleaned = re.sub(r"\t+", " ", text)
    cleaned = re.sub(r" {2,}", " ", cleaned )
    cleaned = cleaned.replace("\r\n","\n")
    cleaned = cleaned.replace("\r","\n")
    cleaned = re.sub(r" +$", "",cleaned , flags=re.MULTILINE)
    cleaned = re.sub(r"^ +", "", cleaned, flags=re.MULTILINE)
    cleaned = re.sub(r"\n{3,}","\n\n",cleaned).strip()

    return cleaned

