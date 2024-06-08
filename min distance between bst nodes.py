from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        nums = []
        
        def inOrder(root):
            if root:
                inOrder(root.left)
                nums.append(root.val)
                inOrder(root.right)
        
        inOrder(root)
        diff = nums[1] - nums[0]
        for i in range(2, len(nums)):
            diff = min(diff, nums[i] - nums[i - 1])
        return diff


def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

# Driver code to test the solution
if __name__ == "__main__":
    # Create a binary search tree
    values = [4, 2, 6, 1, 3, 5, 7]
    root = None
    for value in values:
        root = insert_into_bst(root, value)
    
    # Create an instance of the solution and find the minimum difference
    sol = Solution()
    print(sol.minDiffInBST(root))  # Expected output: 1
