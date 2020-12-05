def keep(keep_lower, low_bound, high_bound ):
    if keep_lower:
        high_bound = (low_bound + high_bound)//2
    else:
        low_bound = (low_bound + high_bound)//2 + 1
    return low_bound, high_bound

def find_row(row_chars):
    low_bound = 0
    high_bound = 127
    for row_char in row_chars:
        low_bound, high_bound = keep(row_char == 'F', low_bound, high_bound)
    return low_bound

def find_column(col_chars):
    low_bound = 0
    high_bound = 7
    for col_char in col_chars:
        low_bound, high_bound = keep(col_char == 'L', low_bound, high_bound)
    return low_bound

def find_row_column(seat_code):
    return find_row(seat_code[:7]), find_column(seat_code[7:])

def get_seat_id(seat_code):
    row, col = find_row_column(seat_code)
    return row * 8 + col

seat_codes = open("input.txt", "r").readlines()

max_seat_id = 0
min_seat_id = 127 * 8 + 7
full_set = set()
for seat_code in seat_codes:
    seat_id = get_seat_id(seat_code.strip())
    if seat_id > max_seat_id:
        max_seat_id = seat_id
    if seat_id < min_seat_id:
        min_seat_id = seat_id
    full_set.add(seat_id)

while min_seat_id < max_seat_id:
    if not min_seat_id in full_set:
        break
    min_seat_id += 1

print(min_seat_id)
