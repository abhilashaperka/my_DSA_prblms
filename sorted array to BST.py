class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST(nums: list[int]) -> TreeNode:
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])
    return root

def preorder_traversal(root: TreeNode):
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

# Example usage
nums = [-10, -3, 0, 5, 9]
root = sortedArrayToBST(nums)
print("Preorder Traversal of the BST:", preorder_traversal(root))
