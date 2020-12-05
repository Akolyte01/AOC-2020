required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

txt_input = open("input.txt", "r").read()
passports = [passport.split() for passport in txt_input.split('\n\n')]

def validate_fields(required_fields, present_fields):
    return len(required_fields.intersection(present_fields)) == len(required_fields)

valid_passports = 0
for passport in passports:
    present_fields = {line_item.split(':')[0] for line_item in passport}
    if validate_fields(required_fields, present_fields):
        valid_passports += 1

print(valid_passports)
