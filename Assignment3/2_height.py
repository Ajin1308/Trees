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

    def height(self):
        left_height = 0
        right_height = 0

        if self.left:
            left_height = self.left.height()

        if self.right:
            right_height = self.right.height()

        return max(left_height, right_height) + 1


root = BinaryTree(5)
root.add_child(3)
root.add_child(2)
root.add_child(4)
root.add_child(9)
root.add_child(7)
root.add_child(6)
root.add_child(8)
root.add_child(10)

root.inorder_display()
print("--------------------------------")
print(root.height())
print("--------------------------------")
