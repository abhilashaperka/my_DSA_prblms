#convert bst to greater tree 
def greater_tree(self,root:Optional[TreeNode])->Optional[TreeNode]:
    if not root:
        return None
    stack,val,curr=[],0,root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr=curr.right
        curr=stack.pop()
        val+=curr.val
        curr.val=val
        curr=curr.left
    return root