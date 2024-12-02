with open("dec2_data.txt", "r") as data:
    reports = [list(map(int, line.strip().split())) for line in data]

safe_reports = 0

for row in reports:

    def is_row_safe(row):
        for j in range(len(row)):
            if j > 0:
                diff_prev = abs(row[j] - row[j - 1])
                if diff_prev < 1 or diff_prev > 3:
                    return False
            if j < len(row) - 1:
                diff_next = abs(row[j] - row[j + 1])
                if diff_next < 1 or diff_next > 3:
                    return False
        # Check growth
        for k in range(2, len(row)):
            if (row[k - 1] > row[k - 2] and row[k] < row[k - 1]) or (
                row[k - 1] < row[k - 2] and row[k] > row[k - 1]
            ):
                return False
        return True

    # Check if the row is safe
    if is_row_safe(row):
        safe_reports += 1
        continue

    # Try removing one element at a time
    for j in range(len(row)):
        modified_row = row[:j] + row[j + 1 :]
        if is_row_safe(modified_row):
            safe_reports += 1
            break

print(f"Safe reports: {safe_reports}")
