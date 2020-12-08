instructions = open("input.txt", "r").readlines()

stored_visited = set()
stored_current = 0
stored_accumulator = 0
in_experiment = False

current = 0
while current < len(instructions):
    in_experiment = False
    visited = stored_visited.copy()
    current = stored_current
    accumulator = stored_accumulator
    while not current in visited and current < len(instructions):
        visited.add(current)
        instruction = instructions[current]
        code = instruction[:3]
        sign = instruction[4]
        value = instruction[5:]
        value = int(value) if sign == '+' else int(value)*-1
        if code == 'nop':
            if not in_experiment: #store state as if this instruction had run, but instead run swp
                in_experiment = True
                stored_visited = visited.copy()
                stored_current = current + 1
                stored_accumulator = accumulator
                current += value
            else:
                current += 1
        elif code == 'acc':
            accumulator += value
            current += 1
        else:
            if not in_experiment: #store state as if this instruction had run, but instead run nop 
                in_experiment = True
                stored_visited = visited.copy()
                stored_current = current + value
                stored_accumulator = accumulator
                current += 1
            else:
                current += value

print(accumulator)
