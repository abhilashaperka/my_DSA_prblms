#minimum distance in BST
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right
def minDiffInBST(root):
    res=[]

    def inorder(node):
        if node:
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
    inorder(root)
    min_diff=float('inf')
    for i  in range(1,len(res)):
        min_diff=min(min_diff,abs(res[i-1]-res[i]))
    return min_diff
root1 = TreeNode(4)
root1.left = TreeNode(2)
root1.right = TreeNode(6)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(3)
print("output:",minDiffInBST(root1))