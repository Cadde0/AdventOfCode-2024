import re


data = open("dec3_data.txt", "r")

pattern = r"mul\((\d{1,3}|mul\(.*?\)),(\d{1,3}|mul\(.*?\))\)"

multiples = re.findall(pattern, data.read())


def multiply(mul_expr):
    expr1, expr2 = mul_expr
    if "mul" in expr1:
        x = multiply(re.match(pattern, expr1).groups())
    else:
        x = int(expr1)

    if "mul" in expr2:
        y = multiply(re.match(pattern, expr2).groups())
    else:
        y = int(expr2)

    return x * y


total_sum = sum(multiply(mul_expr) for mul_expr in multiples)

print(f"Total sum: {total_sum}")
