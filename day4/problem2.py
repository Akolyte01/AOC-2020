import re
def validate_hgt(value):
    units = value[-2:]
    value = int(value[:-2])
    if units == 'cm':
        return 150 <= value and value <= 193
    elif units == 'in':
        return 59 <= value and value <= 76
    else:
        return False

required_fields = {
    'byr': lambda value : 1920 <= int(value) and int(value) <= 2002,
    'iyr': lambda value : 2010 <= int(value) and int(value) <= 2020,
    'eyr': lambda value : 2020 <= int(value) and int(value) <= 2030,
    'hgt': validate_hgt,
    'hcl': lambda value : re.match('^\#[a-f0-9]{6}$', value),
    'ecl': lambda value : value in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid': lambda value : re.match('^[0-9]{9}$', value)
}

def validate_fields(required_fields, present_fields):

    for field, validator in required_fields.items():
        try:
            if not validator(present_fields[field]):
                return False
        except Exception as e:
            return False
    return True

txt_input = open("input.txt", "r").read()
passports = [passport.split() for passport in txt_input.split('\n\n')]
valid_passports = 0
for passport in passports:
    present_fields = {line_item.split(':')[0] : line_item.split(':')[1] for line_item in passport}
    if validate_fields(required_fields, present_fields):
        valid_passports += 1

print(valid_passports)
