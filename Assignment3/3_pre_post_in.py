class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_child(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BinaryTree(value)
            else:
                self.left.add_child(value)
        else:
            if self.right is None:
                self.right = BinaryTree(value)
            else:
                self.right.add_child(value)

    def inorder_display(self):
        if self.left:
            self.left.inorder_display()
        print(self.value)
        if self.right:
            self.right.inorder_display()

    def preorder_display(self):
        print(self.value)
        if self.left:
            self.left.preorder_display()
        if self.right:
            self.right.preorder_display()

    def postorder_display(self):
        if self.left:
            self.left.postorder_display()
        if self.right:
            self.right.postorder_display()
        print(self.value)

root = BinaryTree(5)
root.add_child(3)
root.add_child(2)
root.add_child(4)
root.add_child(9)
root.add_child(7)
root.add_child(6)
root.add_child(8)
root.add_child(10)

print("--------------------------------")
root.inorder_display()
print("--------------------------------")
root.preorder_display()
print("--------------------------------")
root.postorder_display()