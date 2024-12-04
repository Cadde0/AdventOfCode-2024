with open("dec4_data.txt", "r") as file:
    data = file.readlines()

grid = [list(line.strip()) for line in data]

nof_Xmas = 0
# rows = 140
# cols = 140

for row in range(138):
    for col in range(138):
        if (
            grid[row][col] == "M"
            and grid[row + 1][col + 1] == "A"
            and grid[row + 2][col + 2] == "S"
        ) or (
            grid[row][col] == "S"
            and grid[row + 1][col + 1] == "A"
            and grid[row + 2][col + 2] == "M"
        ):
            if (
                grid[row + 2][col] == "M"
                and grid[row + 1][col + 1] == "A"
                and grid[row][col + 2] == "S"
            ) or (
                grid[row + 2][col] == "S"
                and grid[row + 1][col + 1] == "A"
                and grid[row][col + 2] == "M"
            ):
                nof_Xmas += 1

print(nof_Xmas)
