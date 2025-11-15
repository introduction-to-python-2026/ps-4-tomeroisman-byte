def split_before_each_uppercase(formula):
    parts = []
    current = ""
    for ch in formula:
        if ch.isupper():
            if current:
                parts.append(current)
            current = ch  # start new chunk
        else:
            current += ch
    if current:
        parts.append(current)
    return parts
def split_before_each_uppercase(formula):
    parts = []
    current = ""
    for ch in formula:
        if ch.isupper():
            if current:
                parts.append(current)
            current = ch  # start new chunk
        else:
            current += ch
    if current:
        parts.append(current)

    return parts
