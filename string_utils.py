def split_before_each_uppercases(formula):
    start = 0
    split_formula = []
    for i in range (len(formula)):
        if formula[i].isupper() and i != start:
            split_formula.append(formula[start:i])
            start = i
    split_formula.append(formula[start:])
    return split_formula

def split_at_first_digit(formula):
    digit_location = 1
    for l in range(1, len(formula)):
      if formula[l].isdigit() == True:
        break
      else:
        digit_location += 1
    if digit_location == len(formula):
      return formula, 1
    else:
      prefix = formula[:l]
      numeric = formula[l:]
      return prefix,numeric
