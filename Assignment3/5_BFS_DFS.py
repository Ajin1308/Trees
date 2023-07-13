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

    def Breadth_Fs(self):
        queue = deque()
        visited = []

        queue.append(self)

        while queue:
            node = queue.popleft()
            visited.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return visited

    def Depth_Fs_inorder(self):
        visited = []

        if self.left:
            visited.extend(self.left.Depth_Fs_inorder())

        visited.append(self.value)

        if self.right:
            visited.extend(self.right.Depth_Fs_inorder())

        return visited

    def Depth_Fs_preorder(self):
        visited = []

        visited.append(self.value)
        if self.left:
            visited.extend(self.left.Depth_Fs_preorder())

        if self.right:
            visited.extend(self.right.Depth_Fs_preorder())

        return visited

    def Depth_Fs_postorder(self):
        visited = []

        if self.left:
            visited.extend(self.left.Depth_Fs_preorder())

        if self.right:
            visited.extend(self.right.Depth_Fs_preorder())

        visited.append(self.value)

        return visited



root = BinaryTree(5)
root.add_child(3)
root.add_child(2)
root.add_child(4)
root.add_child(9)
root.add_child(7)
root.add_child(6)
root.add_child(8)
root.add_child(10)

print(root.Breadth_Fs())
print("--------------------------------")
print(root.Depth_Fs_inorder())
print("--------------------------------")
print(root.Depth_Fs_preorder())
print("--------------------------------")
print(root.Depth_Fs_postorder())
print("--------------------------------")