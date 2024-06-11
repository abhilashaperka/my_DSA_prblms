#Two sum - input is a BST
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def Twosum(root: TreeNode, k: int) -> bool:
    def inorder(node, elements):
        if not node:
            return
        inorder(node.left, elements)
        elements.append(node.val)
        inorder(node.right, elements)
        
    elements = []
    inorder(root, elements)
    left, right = 0, len(elements) - 1
    
    while left < right:
        current_sum = elements[left] + elements[right]
        if current_sum == k:
            return True
        elif current_sum < k:
            left += 1
        else:
            right -= 1
            
    return False

# Example usage
root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)

print(Twosum(root, 4))  # Output: True
print(Twosum(root, 9))  # Output: False
