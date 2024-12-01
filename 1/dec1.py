totalDistance = 0

list1 = []
list2 = []
# test_l1 = [3, 4, 2, 1, 3, 3]
# test_l2 = [4, 3, 5, 3, 9, 3]

data = open("dec1_data.txt", "r")

for line in data:
    l1, l2 = line.strip().split()
    list1.append(int(l1))
    list2.append(int(l2))

list1.sort()
list2.sort()

# test_l1.sort()
# test_l2.sort()

for i in range(len(list1)):
    dist = abs(list1[i] - list2[i])
    totalDistance += dist

print("Total Distance: ", totalDistance)

# PART TWO

similarityScore = 0

for x in list1:
    apperances = 0
    for i in range(len(list2)):
        if x == list2[i]:
            apperances += 1
    similarityScore += x * apperances

print("Similarity Score: ", similarityScore)
