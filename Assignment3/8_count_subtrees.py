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

    def count_subtrees_with_sum(self, root, x):
        if root is None:
            return 0

        left_count = self.count_subtrees_with_sum(root.left, x)
        right_count = self.count_subtrees_with_sum(root.right, x)

        if (root.value + left_count + right_count) == x:
            return 1 + left_count + right_count
        else:
            return left_count + right_count


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
print(root.count_subtrees_with_sum(root,6))