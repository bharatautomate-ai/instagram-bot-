def normalize_text(text):

    text = text.lower()

    replacements = {
        "kya": "",
        "hai": "",
        "ka": "",
        "ki": "",
        "price": "price",
        "rate": "price",
        "kitna": "price",
        "pp": "price",
        "prc": "price",
        "bhai": "",
        "plz": "",
        "cod":"online",
        "price Drop": "cost rate" "kitne ka hai",
        "قیمت": "قیمت کیا ہے"
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    return text.strip()


def humanize_reply(text):
    return f"😊 {text}"