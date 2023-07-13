from collections import deque

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

    def sum_left_leafs(self, root):
        if root is None:
            return 0

        if root.left and root.left.left is None and root.left.right is None:
            left_leaf_value = root.left.value
        else:
            left_leaf_value = 0

        return left_leaf_value + self.sum_left_leafs(root.left) + self.sum_left_leafs(root.right)




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
print(root.sum_left_leafs(root))
print("--------------------------------")