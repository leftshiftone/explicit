def is_numeric(text: str):
    text = text.replace(".", "")
    text = text[0:-2] if text.endswith(",-") else text
    return text.isdigit()


def to_number(text: str):
    text = text.replace(".", "")
    text = text[0:-2] if text.endswith(",-") else text
    return float(text)