with open("dec6_data.txt", "r") as file:
    data = file.readlines()

map = [list(line.strip()) for line in data]


def guard_position(map):
    for row_indx, row in enumerate(map):
        for col_indx, cell in enumerate(row):
            # print(f"Checking cell: {cell} at ({row_indx}, {col_indx})")
            if cell == "^":
                return (row_indx, col_indx)
    return None


def move_guard(start_pos, map):
    # Directions: Up (0),  Right (1), Down (2), Left (3)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()
    position = start_pos
    direction = 0  # Starts facing up (1)

    while position:
        row, col = position
        visited.add(position)

        # Check the next cell the guard is facing
        next_row = row + directions[direction][0]
        next_col = col + directions[direction][1]

        # If the guard goes outside the map, Stop
        if not (0 <= next_row < 130 and 0 <= next_col < 130):
            break

        # If the guard hits an obstacle, turn right
        if map[next_row][next_col] == "#":
            direction = (direction + 1) % 4
        else:
            position = (next_row, next_col)

    return len(visited)


guard_start_pos = guard_position(map)
visited_positions = move_guard(guard_start_pos, map)

print(visited_positions)
