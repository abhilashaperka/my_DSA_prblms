class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def maxsumBST(root):
    def helper(node):
        nonlocal max_sum
        min_val,max_val=node.val,node.val
        is_left_BST,l_sum,l_min,l_max=True,0,node.val,node.val
        if node.left:
            l_min,l_max,is_bst,l_sum=helper(node.left)
            if not (is_bst and l_max<node.val):
                is_left_bst=False
        is_right_bst,r_sum,r_min,r_max=True,0,node.val,node.val
        if node.right:
            r_min,r_max,is_bst,r_sum=helper(node.right)
            if not (is_bst and r_min>node.val):
                is_right_bst=False
        if is_left_bst and is_right_bst:
            max_sum=max(max_sum,l_sum+r_sum+node.val)
            return l_min,r_max,True,l_sum+r_sum+node.val
        return 0,0,False,0
    max_sum=0
    helper(root)
    return max_sum
                




