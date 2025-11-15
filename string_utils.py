def split_at_digit(formula):
    prefix = ""
    num_part = ""
    for i in formula:
        if i.isdigit():
            num_part = formula[len(prefix):]
            break
        prefix += i
    if num_part == "":
        num_part = 1
    return prefix, int(num_part)

def split_before_each_uppercase(formula):
    parts = []
    current = ""
    for ch in formula:
        if ch.isupper():
            if current:
                parts.append(current)
            current = ch
        else:
            current += ch
    if current:
        parts.append(current)
    return parts
