
def parse_entry(entry):
    letter_range, letter, password = entry.split()
    min_range, max_range = letter_range.split('-')
    return int(min_range), int(max_range), letter[0], password.strip()

def validate_entry(min_range, max_range, letter, password):
    occurences = password.count(letter)
    return min_range <= occurences and occurences <= max_range

num_valid = 0
txtInput = open("input.txt", "r")
for entry in txtInput:
     if validate_entry(*parse_entry(entry)):
         num_valid += 1

print(num_valid)
