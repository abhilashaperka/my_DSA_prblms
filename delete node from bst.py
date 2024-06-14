#delete node from bst
from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return root
        if val < root.val:
            root.left = self.deleteNode(root.left, val)
        elif val > root.val:
            root.right = self.deleteNode(root.right, val)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                curr = root.right
                while curr.left:
                    curr = curr.left
                root.val = curr.val
                root.right = self.deleteNode(root.right, curr.val)
        return root

# Helper function to insert a new node with the given key in the BST
def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# Helper function to print the inorder traversal of the BST
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

# Driver code
if __name__ == "__main__":
    keys = [5, 3, 6, 2, 4, 7]

    # Construct BST
    root = None
    for key in keys:
        root = insert(root, key)

    print("Inorder traversal of the given tree")
    inorder(root)
    print("\nDelete 3")
    root = Solution().deleteNode(root, 3)
    print("Inorder traversal of the modified tree")
    inorder(root)
    print("\nDelete 6")
    root = Solution().deleteNode(root, 6)
    print("Inorder traversal of the modified tree")
    inorder(root)
