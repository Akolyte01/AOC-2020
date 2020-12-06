txt_input = open("input.txt", "r").read()
group_answers = [answers.split() for answers in txt_input.split('\n\n')]
total = 0
for group_answer in group_answers:
    group_count = {}
    for person in group_answer:
        for answer in person:
            group_count[answer] = group_count.get(answer,0)+1
    print(group_count)
    for answer, count in group_count.items():
        if count == len(group_answer):
            total += 1
print(total)
