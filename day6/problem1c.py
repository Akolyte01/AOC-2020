import functools
print(functools.reduce(lambda a,b : a+b, [len(set.union(*[set(answer) for answer in answers.split()])) for answers in open("input.txt", "r").read().split('\n\n')]))
