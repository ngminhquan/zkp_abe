from access_tree import *
# Khởi tạo dictionary để lưu ánh xạ giữa các yêu cầu và giá trị nhập
input_mapping = {}
print("Nhập các input (nhập 'q' để kết thúc):")
i = 1
while True:
    user_input = input(f"Nhập giá trị cho input thứ {i}: ")
    if user_input.lower() == 'q':
        break
        
    input_mapping[user_input] = user_input
    if i == 1:
        input_mapping[user_input] = 'and'
    i += 1
print(input_mapping)
tree_root = create_tree(input_mapping)
with open('policy.txt', 'r+') as policy:
    tree_dict = policy.read()
    if tree_dict == '':
        print(print_tree(tree_root))
        policy.write(tree_to_dict(tree_root))
    else:
        tree_root = dict_to_tree(tree_dict)
        key1 = list(input_mapping.keys())[0]
        subtree_root = create_subtree_from_leaf(tree_root, key1, input_mapping)
        policy.seek(0)
        print(print_tree(tree_root))
        policy.write(tree_to_dict(tree_root))


from anytree import Node, RenderTree


