input_numbers = [int(line) for line in open("input.txt", "r")]
input_numbers.sort(reverse=True)

input_numbers.append(0)

arrangements_from = {input_numbers[0]+3 : 1}
for number in input_numbers:
    arrangements = 0
    for delta in range(1,4):
        arrangements += arrangements_from.get(number+delta, 0)
    arrangements_from[number] = arrangements

print(arrangements_from[input_numbers[-1]])
