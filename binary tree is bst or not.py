#chack whether a binary tree is a binary search tree(BST) or not
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def is_bst(root):
    def inorder_traversal(node, res):
        if node:
            inorder_traversal(node.left, res)
            res.append(node.key)
            inorder_traversal(node.right, res)
    
    keys_in_order = []
    inorder_traversal(root, keys_in_order)

    for i in range(1, len(keys_in_order)):
        if keys_in_order[i] <= keys_in_order[i - 1]:
            return False
    return True

if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    if is_bst(root):
        print("True")
    else:
        print("False")
