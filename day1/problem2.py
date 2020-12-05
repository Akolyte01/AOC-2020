txtInput = open("input.txt", "r")
entries = sorted([int(line.strip()) for line in txtInput])
l = 0
m = l + 1
r = len(entries)-1
while l < r-1:
    m = l + 1
    left = entries[l]
    middle = entries[m]
    right = entries[r]
    total = left + middle + right
    # print(entries)
    # print(l, left, m, middle, r, right, total)
    if total > 2020:
        r -= 1
        continue
    while total < 2020:
        m += 1
        middle = entries[m]
        total = left + middle + right
        print(entries)
        print(l, left, m, middle, r, right, total)
    if total == 2020:
        break
    l += 1
#
# print('yay')
print(l, left, m, middle, r, right, total)
# while l < m and m < r:
#     left = entries[l]
#     right = entries[r]
#     middle = entries[m]
#     total = left + right + middle
#     if total == 2020:
#         break
#     if total > 2020:
#         r -= 1
#         m = l + 1
#     if total < 2020:
#         if m < (r-1):
#             m += 1
#         else:
#             l += 1
#             m = l + 1
#
#
# while l < r:
#     while m < r:
#         left = entries[l]
#         right = entries[r]
#         middle = entries[m]
#         total = left + right + middle
#         if total > 2020:
#             r -= 1
#         elif total < 2020:
#             m += 1
#         elif total == 2020:
#             print(l, left, m, middle, r, right, total)
#             break
