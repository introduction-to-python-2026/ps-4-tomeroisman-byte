def split_at_digit(formula):
    prefix = ""
    num_str = ""
    digit_started = False

    for ch in formula:
        if ch.isdigit():
            if not digit_started:
                digit_started = True
            num_str += ch
        else:
            if digit_started:
                break
            prefix += ch

    if not digit_started:
        return formula, 1

    return prefix, int(num_str)
