def parse_entry(entry):
    letter_range, letter, password = entry.split()
    min_range, max_range = letter_range.split('-')
    return int(min_range), int(max_range), letter[0], password.strip()

def validate_entry(min_range, max_range, letter, password):
    occurences = password.count(letter)
    return min_range <= occurences and occurences <= max_range

def alt_validate_entry(index_1, index_2, letter, password):
    value_1 = password[index_1-1]
    value_2 = password[index_2-1]
    return (value_1 == letter) ^ (value_2 == letter)

num_valid = 0
txtInput = open("input.txt", "r")
for entry in txtInput:
     if alt_validate_entry(*parse_entry(entry)):
         num_valid += 1

print(num_valid)
