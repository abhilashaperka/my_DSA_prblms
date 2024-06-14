#trim a bst
class Solution:
    def trimBST(self, root:Optional[TreeNode],low:int, high:int)->Optional[TreeNode]:
        if root:
            root.left=self.trimBST(root.left,low,high)
            root.right=self.trimBST(root.right,low,high)
            if root.val<low:
                return root.right
            elif root.val>high:
                return root.left
            return root
        return root

"""
from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Trim the left and right subtrees
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        
        # Now deal with the current node
        if root.val < low:
            return root.right
        elif root.val > high:
            return root.left
        
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
    keys = [3, 0, 4, 2, 1]

    # Construct BST
    root = None
    for key in keys:
        root = insert(root, key)

    print("Inorder traversal of the given tree:")
    inorder(root)
    print()

    low, high = 1, 3
    solution = Solution()
    root = solution.trimBST(root, low, high)

    print(f"Inorder traversal of the trimmed tree with range [{low}, {high}]:")
    inorder(root)
    print()

"""