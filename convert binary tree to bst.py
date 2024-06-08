#convert a binary tree to a binary search tree(BST)
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def inorder_traversal(node, res):
    if node:
        inorder_traversal(node.left, res)
        res.append(node.key)
        inorder_traversal(node.right, res)

def build_bst(keys):
    if not keys:
        return None
    mid = len(keys) // 2
    root = TreeNode(keys[mid])
    root.left = build_bst(keys[:mid])
    root.right = build_bst(keys[mid + 1:])
    return root

def convert_to_bst(root):
    keys = []
    inorder_traversal(root, keys)
    keys.sort()
    return build_bst(keys)

def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.key, end=" ")
        print_inorder(root.right)

if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(7)
    bst_root = convert_to_bst(root)
    print("Inorder traversal of converted BST:")
    print_inorder(bst_root)
