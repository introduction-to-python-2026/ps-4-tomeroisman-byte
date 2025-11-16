def split_before_each_uppercases(formula):
    start = 0
    split_formula = []
    for i in range (len(formula)):
        if formula[i].isupper() and i != start:
            split_formula.append(formula[start:i])
            start = i
    split_formula.append(formula[start:])
    return split_formula

def split_at_digit(formula):
    num_found = 1
    digit_location = 1
    for l in range(len(formula[1:])):
        if l.isdigit():
            digit_location.append(l)
            break
        else:
            num_found = 0
        if digit_location == len(formula):
            if num_found = 0:
                return formula, 1
            elif num_found != 0:
                prefix = formula[:i]
                numeric = formula[i:]
                return prefix,numeric
