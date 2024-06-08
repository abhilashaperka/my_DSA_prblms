#range sum of bst
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root is None:
            return 0
        if low <= root.key <= high:
            return root.key + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
        elif root.key < low:
            return self.rangeSumBST(root.right, low, high)
        else:  # root.key > high
            return self.rangeSumBST(root.left, low, high)

# Driver code to test the rangeSumBST method
if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)

    solution = Solution()
    low, high = 7, 15
    print("Range Sum BST:", solution.rangeSumBST(root, low, high))  # Output should be 32




#function
"""def rangesumBST(self, root: Optimal[TreeNode], low: int, high: int)->int:
    if root is None:
        return 0
    if low<=root.val<=high:
        return root.val+self.rangesumBSt(root.left,low,high)+self.rangesumBST()
    elif low<=root.val:
        return self.rangesumBSt(root.left,low,high)
    elif root.val<=high:
        return self.rangesumBSt(root.right,low,high)

"""