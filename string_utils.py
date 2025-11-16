def split_before_each_uppercases(formula):
    end = 1
    start = 0
    split_formula = []
    if formula != "":
        for i in range(1,len(formula)):
            if formula[i].isupper():
                end = i
                split_formula.append(formula[start:end])
                start = i
        split_formula.append(formula[start:len(formula)])
        return split_formula
    else:
        return []

def split_at_first_digit(formula):
    digit_location = 1
    for i in range(1, len(formula)):
      if formula[i].isdigit() == True:
        break
      else:
        digit_location += 1
    if digit_location == len(formula):
      return formula, 1
    else:
      prefix = formula[:digit_location]
      numeric = int(formula[digit_location::])
      return prefix,numeric
