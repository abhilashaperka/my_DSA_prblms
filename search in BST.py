# Search in a BST
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root, val):
    if root is None or root.val == val:
        return root
    if val < root.val:
        return searchBST(root.left, val)
    else:
        return searchBST(root.right, val)

def preorder(root):
    if root:
        print(root.val, end=" ")
        preorder(root.left)
        preorder(root.right)

# Example usage
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

target_value = 2
result = searchBST(root, target_value)
if result:
    print("Node with value", target_value, "found in the BST.")
    print("Preorder traversal starting from the found node:")
    preorder(result)
else:
    print("Node with value", target_value, "not found in the BST.")
