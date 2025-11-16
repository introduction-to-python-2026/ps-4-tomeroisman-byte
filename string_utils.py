def split_at_digit(formula):
    prefix = ""
    num = ""
    for i in formula:
        if i.isdigit:            
            num += i
        else:
            if number:
                break
            break
            prefix += i
        if num:
            return prefix, int(num)
        else:
            return formula, 1
            
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
