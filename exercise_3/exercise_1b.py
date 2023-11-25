"""
Use this file to implement your solution for exercise 3-1 b.
"""
import random
from exercise_1a import find_subtrees

def modified_tree(tree,old_subtree,new_subtree):
    if tree == old_subtree:
        tree = new_subtree
    elif tree[1] is not None:
        tree = (tree[0],[modified_tree(child,old_subtree,new_subtree) for child in tree[1]])
    return tree

def replace_random_subtree(tree, symbol, subtrees):
    to_replace = random.choice(find_subtrees(tree,symbol))
    replace_with = random.choice(subtrees)
    return modified_tree(tree,to_replace,replace_with)