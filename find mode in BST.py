#Find Mode in BST
from collections import defaultdict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
def findmode(root):
    freq_map= defaultdict(int)
    def inorder(node):
        if node:
            inorder(node.left)
            freq_map[node.val]+= 1
            inorder(node.right)
    inorder(root)
    max_freq= max(freq_map.values())
    modes=[key for key, freq_map in freq_map.items() if freq_map == max_freq]
    return modes
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)
print(findmode(root))
