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


    def oddLevelnodes(self, level=1):
        odd = []
        if self.value is None:
            return odd
    
        if level % 2 == 1:
            odd.append(self.value)

        if self.left:
            odd += self.left.oddLevelnodes(level + 1)
        if self.right:
            odd += self.right.oddLevelnodes(level + 1)

        return odd

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
print(root.oddLevelnodes())