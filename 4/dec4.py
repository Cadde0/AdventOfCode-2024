with open("dec4_data.txt", "r") as file:
    data = file.readlines()

grid = [list(line.strip()) for line in data]

rows = 140
cols = 140

nof_xmas = 0

# Horisontell sökning
for row in grid:
    for start_index in range(137):
        window = row[start_index: start_index + 4]
        word = ''.join(window)
        if word == "XMAS" or word == "SAMX":
            nof_xmas += 1


# Vertikal sökning
for col in range(140):
    for start_row in range(137):
        window = 
        for i in range(4):
            window[i] = grid[start_row + i][col]
        word = ''.join(window)
        if word == "XMAS" or word == "SAMX":
            nof_xmas += 1

# Diagonal Sökning // eller flera diagonala, en åt varje håll




print(nof_xmas)
