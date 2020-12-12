input_numbers = [int(line) for line in open("input.txt", "r")]
input_numbers.sort()
input_numbers.append(input_numbers[-1]+3)
input_numbers.insert(0,0)
print(input_numbers)
threes = 0
ones = 0
for index in range(len(input_numbers)-1):
    delta = input_numbers[index+1] - input_numbers[index]
    if delta == 3:
        threes += 1
    elif delta == 1:
        ones += 1
    else:
        print('ya dun goofed')
print(ones * threes)
