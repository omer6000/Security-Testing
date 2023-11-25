"""
Use this file to implement your solution for exercise 3-1 a.
"""

def find_subtrees(tree, symbol):
    subtrees = []
    if tree[0] == symbol:
        subtrees.append(tree)
    if tree[1] is not None:
        for child in tree[1]:
            subtrees += find_subtrees(child,symbol)
    return subtrees
