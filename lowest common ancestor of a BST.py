#lowest common ancestor of a bst
"""
def lowestcommonancestor(self,root:'TreeNode',p:'TreeNode',q:'TreeNode')->'TreeNode':
    if not root:
        return
    if ((root.val>=p.val and root.val<=q.val) or (root.val<=p.val and root.val>=q.val)):
        return root
    if (root.val>p.val and root.val>q.val):
        return self.lowestcommonancestor(root.left,p,q)
    return self.lowestcommonancestor(root.right,p,q)
"""
from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        # If both p and q are greater than root, then LCA lies in right
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        # If both p and q are smaller than root, then LCA lies in left
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # If one of p or q is the root or they are on either side, return root
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

# Driver code
if __name__ == "__main__":
    keys = [6, 2, 8, 0, 4, 7, 9, 3, 5]

    # Construct BST
    root = None
    for key in keys:
        root = insert(root, key)
    
    solution = Solution()
    
    # Create nodes for p and q
    p = TreeNode(2)
    q = TreeNode(8)
    
    # Find the LCA of nodes with values 2 and 8
    lca = solution.lowestCommonAncestor(root, p, q)
    print(f"Lowest Common Ancestor of {p.val} and {q.val}: {lca.val if lca else 'None'}")
    
    # Test with different nodes
    p = TreeNode(2)
    q = TreeNode(4)
    
    lca = solution.lowestCommonAncestor(root, p, q)
    print(f"Lowest Common Ancestor of {p.val} and {q.val}: {lca.val if lca else 'None'}")

