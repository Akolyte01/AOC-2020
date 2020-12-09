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
        print(value)
        break
