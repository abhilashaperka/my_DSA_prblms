#recover binary searrch tree
res=[]
startnode=None
prev=None
lastnode=None
def recoverbst(self):
    def dfs(root):
        nonlocal res, startnode, prev, lastnode
        if not root:
            return
        dfs(root.left)
        if prev and prev.val>root.val:
            if not startnode:
                startnode=prev
            lastnode=root
        prev=root
    dfs(root.right)
dfs(root)
if startnode and lastnode:
    startnode.val,lastnode.val=lastnode.val,startnode.val


