import fileinput

operators = ["+", "-", "*", "/"]


def determine_operator(m, d, a, s):
    # If there is multiplication and division
    if m != -1 and d != -1:
        if m < d:
            return "*", m
        else:
            return "/", d

    # If there is only multiplication
    if m != -1 and d == -1:
        return "*", m

    # If there is only division
    if m == -1 and d != -1:
        return "/", d

    # If there is neither multiplication nor division
    if m == -1 and d == -1:

        # If there is addition and subtraction
        if a != -1 and s != -1:
            if a < s:
                return "+", a
            else:
                return "-", s

        # If there is only addition
        if a != -1 and s == -1:
            return "+", a

        # If there is only subtraction
        if a == -1 and s != -1:
            return "-", s

    return "Done", -1


def convert_negatives(exp):
    new_expression = ""
    skip = 0

    for index in range(len(exp)):
        if index + skip < len(exp):
            if exp[index + skip] == "-":
                if index + skip + 1 < len(exp):
                    if exp[index + skip + 1] == "-":
                        new_expression += "+"
                        skip += 1
                    else:
                        new_expression += exp[index + skip]
            else:
                new_expression += exp[index + skip]

    return new_expression


def evaluate_operations(cur_exp):
    # Gets the index for the operator
    multiply_index = cur_exp.find("*")
    divide_index = cur_exp.find("/")
    add_index = cur_exp.find("+")
    subtract_index = -1
    for x in range(len(cur_exp)):
        if cur_exp[x] == "-":
            if x != 0:
                if cur_exp[x - 1].isdigit():
                    subtract_index = x
                    break
                else:
                    subtract_index = -1
                    break
            else:
                subtract_index = -1
                break

    # Performs all the operations within the brackets
    while multiply_index != -1 or divide_index != -1 or add_index != -1 or subtract_index != -1:
        # Gets the precedence operator and operator's index
        current_operator, operator_index = determine_operator(
            multiply_index, divide_index, add_index, subtract_index)

        # If there are no operators left in the bracket, break
        if current_operator == "Done":
            break

        first = ""
        second = ""
        first_index = 0
        second_index = len(cur_exp)

        # Gets the first number
        for index in range(operator_index - 1, -1, -1):
            if cur_exp[index] not in operators:
                first = cur_exp[index] + first
                first_index = index
            else:
                if cur_exp[index] == "-" and index == 0:
                    first = cur_exp[index] + first
                    first_index = index
                else:
                    break

        # Gets the second number
        for index in range(operator_index + 1, len(cur_exp), 1):
            if cur_exp[index] not in operators:
                second += cur_exp[index]
                second_index = index
            else:
                if cur_exp[index] == "-" and second == "":
                    second += cur_exp[index]
                    second_index = index
                else:
                    break

        result = 0

        # Evaluates the first and second number with the operator
        if current_operator == "*":
            result = float(first) * float(second)
        if current_operator == "/":
            result = float(first) / float(second)
        if current_operator == "+":
            result = float(first) + float(second)
        if current_operator == "-":
            result = float(first) - float(second)

        cur_exp = cur_exp[:first_index] + str(result) + cur_exp[second_index + 1:]

        # Gets the index for the operator
        multiply_index = cur_exp.find("*")
        divide_index = cur_exp.find("/")
        add_index = cur_exp.find("+")
        subtract_index = -1
        for x in range(len(cur_exp)):
            if cur_exp[x] == "-":
                if x != 0:
                    if cur_exp[x - 1].isdigit():
                        subtract_index = x
                        break
                    else:
                        subtract_index = -1
                        break
                else:
                    subtract_index = -1
                    break

    return cur_exp


def evaluate_brackets(exp):
    while exp.count("(") > 0:
        # Gets the current expression in the bracket
        left_index = exp.find("(")
        right_index = exp.find(")")
        current_expression = exp[left_index + 1: right_index]

        current_expression = evaluate_operations(current_expression)

        exp = exp[:left_index] + current_expression + exp[right_index + 1:]

    return exp


while True:
    try:
        line = input()
        if len(line) > 0:
            if not line[0].isdigit() and line[0] != "(" and line[0] != "-":
                break

        expression = ""

        for character in line:
            if character != " ":
                expression += character

        expression = convert_negatives(expression)
        expression = evaluate_brackets(expression)
        expression = evaluate_operations(expression)
        print(round(float(expression), 2))
    except EOFError:
        break
