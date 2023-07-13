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

    def maxLevelSum(self):
        if self.value is None:
            return 0

        q = deque()
        q.append(self)
        max_level = 1
        level = 1
        max_sum =float('-inf')

        while q:
            level_sum = 0
            next_level = []

            for node in q:
                level_sum += node.value

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            q = next_level
            level += 1
        return f"maximum value is {max_sum} at level {max_level}"



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
print(root.maxLevelSum())