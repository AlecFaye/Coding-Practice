tree_count = int(input())

trees = input().split()
tree_int = [int(s) for s in trees]

tree_int.sort()
tree_int.reverse()

planted_trees = []

print("Before Tree:", tree_int)

for tree in tree_int:
    if len(planted_trees) > 0:
        for index in range(len(planted_trees)):
            planted_trees[index] -= 1
    planted_trees.append(tree)
    print(planted_trees)

print("After Tree:", planted_trees)

print(max(planted_trees) + len(planted_trees) + 1)
