instructions = open("input.txt", "r").readlines()
visited = set()
current = 0
accumulator = 0


while not current in visited:
    visited.add(current)
    instruction = instructions[current]
    code = instruction[:3]
    sign = instruction[4]
    value = instruction[5:]
    value = int(value) if sign == '+' else int(value)*-1
    if code == 'nop':
        current += 1
    elif code == 'acc':
        accumulator += value
        current += 1
    else:
        current += value

print(accumulator)
