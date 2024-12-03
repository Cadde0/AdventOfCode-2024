import re


with open("dec3_data.txt", "r") as file:
    data = file.read()

pattern = r"mul\((\d+),(\d+)\)"
enable_pattern = r"do\(\)"
disable_pattern = r"don't\(\)"
is_enabled = True


def multiply(mul_expr):
    x, y = mul_expr
    return int(x) * int(y)


actions = list(re.finditer(f"{enable_pattern}|{disable_pattern}|{pattern}", data))

total_sum = 0

for action in actions:
    janne = action.group()
    if re.match(enable_pattern, janne):
        is_enabled = True
    elif re.match(disable_pattern, janne):
        is_enabled = False
    elif is_enabled and re.match(pattern, janne):
        mul_expr = re.match(pattern, janne).groups()
        total_sum += multiply(mul_expr)


print(f"Total sum: {total_sum}")
