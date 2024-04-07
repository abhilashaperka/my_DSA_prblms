#diagonal traversal of a binary tree
from collections import deque
class treenode:
    def __init__(self,value):
        self.val=value
        self.left=None
        self.right=None
    def diagonal_traversal(root):
        if not root:
            return []
        result=[]
        queue=deque([(root,0)])
        while queue:
            node,level=queue.popleft()
            if level==len(result):
                result.append([])
            result[level].append(node.val)
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level))
        return result
#driver code
root=treenode(8)
root.left=treenode(3)
root.left.left=treenode(1)
root.left.right=treenode(6)
root.left.right.right=treenode(7)
root.left.right.left=treenode(4)
root.right=treenode(10)
root.right.right=treenode(14)
root.right.right.left=treenode(13)
diagonal_trav=treenode.diagonal_traversal(root)
print("diagonal traversal of a binary tree is:")
for level in diagonal_trav:
    print(level)
        
