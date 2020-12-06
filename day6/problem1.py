txt_input = open("input.txt", "r").read()
group_answers = [answers for answers in txt_input.split('\n\n')]
total = 0
for group_answer in group_answers:
    group_set = set()
    for answer in group_answer:
        group_set.add(answer)
    if '\n' in group_set:
        group_set.remove('\n')
    total += len(group_set)
print(total)
