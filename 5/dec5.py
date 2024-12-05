with open("dec5_data.txt", "r") as file:
    data = file.readlines()

page_rules = {}

# Dictionary with 1st page as key with all pages it "unlocks as
# an array with pages"
for line in data:
    if not line.strip():
        break
    # Page rules dictionary
    part = line.strip().split("|")
    key_page, sec_page = int(part[0]), int(part[1])
    if key_page in page_rules:
        page_rules[key_page].append(sec_page)
    else:
        page_rules[key_page] = [sec_page]

pages_to_produce = []

for line in data[1177:]:
    pages = list(map(int, line.strip().split(",")))
    pages_to_produce.append(pages)


def fix_pages(pages):
    is_fixed = False
    while not is_fixed:
        is_fixed = True
        for i in range(len(pages) - 1):
            curr_page = pages[i]
            next_page = pages[i + 1]
            if curr_page in page_rules.get(next_page, []):
                pages[i] = next_page
                pages[i + 1] = curr_page
                is_fixed = False
                break

    return pages


sum_of_pgs = 0
is_correct = True

for i in range(len(pages_to_produce)):
    is_correct = True
    for j in range(len(pages_to_produce[i]) - 1):
        current_page = pages_to_produce[i][j]
        next_page = pages_to_produce[i][j + 1]

        if current_page in page_rules.get(next_page, []):
            is_correct = False
            break

    # if is_correct:
    #    middle_page = pages_to_produce[i][len(pages_to_produce[i]) // 2]
    #   sum_of_pgs += middle_page

    if not is_correct:
        corrected_pages = fix_pages(pages_to_produce[i])

        middle_page = corrected_pages[len(corrected_pages) // 2]
        sum_of_pgs += middle_page


print(sum_of_pgs)
# print(page_rules)
# 5158 too low
# 5405 too high
