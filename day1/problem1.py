input = open("input.txt", "r")
entries = sorted([int(line.strip()) for line in input])
l = 0
r = len(entries)-1
while l < r:
    left = entries[l]
    right = entries[r]
    total = left + right
    if total > 2020:
        r -= 1
    elif total < 2020:
        l += 1
    elif total == 2020:
        break
print(right * left)
