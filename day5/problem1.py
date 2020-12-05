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

seat_codes = open("input.txt", "r").readlines()

max_seat_id = 0
for seat_code in seat_codes:
    row, col = find_row_column(seat_code.strip())
    seat_id = row * 8 + col
    if seat_id > max_seat_id:
        max_seat_id = seat_id

print(max_seat_id)
