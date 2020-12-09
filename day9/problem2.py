input_numbers = [int(line) for line in open("input.txt", "r")]

preamble_size = 25

def does_valid_pair_exist(target, preamble):
    pairs_for_small_numbers = { target - number for number in preamble if number <= target//2 }
    large_numbers = { number for number in preamble if number > target//2 }
    large_numbers_with_pairs = large_numbers.intersection(pairs_for_small_numbers)
    return True if len(large_numbers_with_pairs) else False

invalid = 0

for index, value in enumerate(input_numbers[preamble_size:]):
    if not does_valid_pair_exist(value, input_numbers[index:index+preamble_size]):
        invalid = value
        break

print(invalid)

l = 0
r = 0
summation = input_numbers[0]
while summation != invalid:
    r += 1
    summation += input_numbers[r]
    if summation > invalid:
        summation -= input_numbers[l]
        l += 1
        while summation > invalid:
            summation -= input_numbers[r]
            r -= 1

print(min(*input_numbers[l:r+1]) + max(*input_numbers[l:r+1]))
