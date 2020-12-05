txtInput = open("input.txt", "r")
tree_map = [row.strip() for row in txtInput]
print(tree_map)

def check_space(column, row, tree_map):
    width = len(tree_map[0])
    return tree_map[row][column%width]

def check_collisions(slope, tree_map):
    tree_count = 0
    position = [0,0]
    while position[1] < len(tree_map):
        if check_space(position[0], position[1], tree_map) == '#':
            tree_count += 1
        position[0] += slope[0]
        position[1] += slope[1]
    return tree_count

product = 1
for slope in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
    product *= check_collisions(slope, tree_map)

print(product)
