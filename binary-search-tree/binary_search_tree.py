class TreeNode:
    def __init__(self, value, left, right):
        self.data = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, values):
        self.tree = TreeNode(values.pop(0), None, None)
        for value in values:
            self.add(value)

    def add(self, value):
        current = self.tree
        while current:
            if value > current.data:
                if current.right is None:
                    current.right = TreeNode(value, None, None)
                    break
                else:
                    current = current.right
            else:
                if current.left is None:
                    current.left = TreeNode(value, None, None)
                    break
                else:
                    current = current.left

    def data(self):
        return self.tree

    def sorted_data(self):
        return self.get_data(self.tree)

    def get_data(self, tree):
        output = []
        if tree:
            if tree.left:
                output.extend(self.get_data(tree.left))
            output.append(tree.data)
            if tree.right:
                output.extend(self.get_data(tree.right))
        return output
