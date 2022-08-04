def truncate(text, length):
    return f"{text[:length]}..."

text = "01234567"
print(truncate(text, 4))
