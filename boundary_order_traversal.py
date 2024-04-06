#boundary traversal of the binary tree
class treenode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def print_leaves(self, result):
        if self:
            if self.left:
                self.left.print_leaves(result)
            if not self.left and not self.right:
                result.append(self.val)
            if self.right:
                self.right.print_leaves(result)

    def print_left_boundary(self, result):
        if self:
            if self.left:
                result.append(self.val)
                self.left.print_left_boundary(result)
            elif self.right:
                result.append(self.val)
                self.right.print_left_boundary(result)

    def print_right_boundary(self, result):
        if self:
            if self.right:
                self.right.print_right_boundary(result)
                result.append(self.val)
            elif self.left:
                self.left.print_right_boundary(result)
                result.append(self.val)

    def boundary_traversal(self):
        if not self:
            return []
        result = []
        result.append(self.val)  # Add root node value only once
        self.left.print_left_boundary(result)
        self.print_leaves(result)
        self.right.print_right_boundary(result)
        return result

# Driver code
root = treenode(20)
root.left = treenode(8)
root.right = treenode(22)
root.left.left = treenode(4)
root.left.right = treenode(12)
root.left.right.left = treenode(10)
root.left.right.right = treenode(14)
root.right.right = treenode(25)

print("Boundary order traversal:")
print(root.boundary_traversal())
(root.boundary_traversal())
        
