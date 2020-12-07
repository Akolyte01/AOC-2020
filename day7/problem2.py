import re
txt_input = open("input.txt", "r").read()
relationships = {}
for statement in re.findall(r'(^.*)s contain(.*)$',txt_input, re.MULTILINE):
    container = statement[0]
    relationships.setdefault(container, {'contains':[], 'contained_by': []})
    containees = re.split('[,.]',statement[1])
    for containee_statement in containees[:-1]:
        if containee_statement.startswith(' no'):
            continue
        number, containee = re.match(' (.)*? (.*?)s?$', containee_statement).groups()
        relationships[container]['contains'].append((int(number), containee))
        # relationships.get(containee, {'contains':[], 'contained_by': []})['contained_by'].append(container)
        relationships.setdefault(containee, {'contains':[], 'contained_by': []})
        relationships[containee]['contained_by'].append(container)

potential_containers = set()
def get_containers(bag_type):
    for container in relationships[bag_type]['contained_by']:
        if container in potential_containers:
            continue
        potential_containers.add(container)
        get_containers(container)

def get_containees(bag_type):
    total_contained = 1
    for number, containee in relationships[bag_type]['contains']:
        foo = get_containees(containee)
        total_contained += number * get_containees(containee)
    return total_contained


get_containers('shiny gold bag')
print(len(potential_containers))
print(get_containees('shiny gold bag')-1)
