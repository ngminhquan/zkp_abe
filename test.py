from access_tree import *
with open('policy.txt','r') as policy:
    tree_dict = policy.read()
    tree_root = dict_to_tree(tree_dict)
    #print(print_tree(tree_root))
    #print(tree_to_expression(tree_root.root))

input_mapping = {
    "input1": "and",
    "input2": "input2",
    "input3": "and",
    "input4": "input4",
    "input5": "and",
    "input6": "input6"
}
tree_root = create_tree(input_mapping)
print(print_tree(tree_root))
# Chuyển cây thành biểu thức logic
expression = tree_to_expression(tree_root.root)
print("\nBiểu thức logic tương ứng:")
print(expression)