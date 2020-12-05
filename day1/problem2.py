txtInput = open("input.txt", "r")
entries = sorted([int(line.strip()) for line in txtInput])

def get_pair_for_sum(l, r, target_sum, entries):
    while l < r:
        left = entries[l]
        right = entries[r]
        total = left + right
        if total > target_sum:
            r -= 1
        elif total < target_sum:
            l += 1
        elif total == target_sum:
            return l, left, r, right
    return None, None, None, None

for l, left in enumerate(entries):
    m, middle, r, right = get_pair_for_sum(l+1, len(entries)-1, 2020-left, entries)
    if m:
        print(left*middle*right)
        break
