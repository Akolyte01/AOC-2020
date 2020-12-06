txt_input = open("input.txt", "r").read()
group_answers = [[set(answer) for answer in answers.split()] for answers in txt_input.split('\n\n')]
total = 0
for group_answer in group_answers:
    total += len(set.intersection(*group_answer))
print(total)
