def split_before_each_uppercases(formula):
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


def split_at_digit(formula):
    prefix = ""
    num = ""
    digit_start = False
    for i in formula:
        if i.isdigit():
            digit_start = True
            num += i
        else:
            if num:
                break
            prefix += i
    if digit_start:
        return prefix, int(num)
    else:
            return formula, 1
