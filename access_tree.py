from anytree import Node, RenderTree
from anytree.exporter import DictExporter
from anytree.importer import DictImporter
from anytree import Node, RenderTree
import json
#Hàm in cây
def print_tree(tree_root):
    result = "Cây:\n"
    for pre, fill, node in RenderTree(tree_root):
        result += "%s%s\n" % (pre, node.name)
    return result

# Tạo cây từ input dictionary
def create_tree(input_mapping):
    root = None
    current_parent = None
    for key, value in input_mapping.items():
        if value == "and" or value == "or":
            if root is None:
                root = Node(key)
                current_parent = root
            else:
                current_parent = Node(key, parent=current_parent)
        else:
            Node(value, parent=current_parent)
    return root

# Hàm chuyển cây thành biểu thức logic
def tree_to_expression(node):
    if node.is_leaf:
        return node.name
    elif node.name == "and":
        children_expr = ' and '.join(tree_to_expression(child) for child in node.children)
        return f"({children_expr})"
    elif node.name == "or":
        children_expr = ' or '.join(tree_to_expression(child) for child in node.children)
        return f"({children_expr})"
    
# Hàm tạo cây con từ lá
def create_subtree_from_leaf(root, key1, subtree_input_mapping):
    # Tìm lá có giá trị bằng key1
    target_leaf = None
    for leaf in root.leaves:
        if leaf.name == key1:
            target_leaf = leaf
            break
    # Nếu tìm thấy lá, tạo cây con từ lá đó
    if target_leaf:
        for key, value in subtree_input_mapping.items():
            parent = target_leaf
            if key != target_leaf.name:
                if value == "and":
                    root = Node(key + "()".format(value))
                    parent = root
                else:
                    Node(key, parent=parent)
        return parent
    else:
        return None
    
#Hàm chuyển định dạng cây về dict và ngược lại
def tree_to_dict(tree_root):
    exporter = DictExporter()
    tree_dict = exporter.export(tree_root)
    return json.dumps(tree_dict)
    #return tree_dict
def dict_to_tree(tree_dict):
    tree_dict = json.loads(tree_dict)
    importer = DictImporter()
    root_node = importer.import_(tree_dict)
    return root_node
