
class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class LeftView:
    def __init__(self):
        self.max_level = 0

    def left_view(self, node, level):
        if node is None:
            return None
        if self.max_level < level:
            print(node.value)
            self.max_level = level
        self.left_view(node.left_child, level + 1)
        self.left_view(node.right_child, level + 1)


if __name__ == '__main__':
    root = Node(3)
    root.left_child = Node(2)
    root.right_child = Node(4)
    root.right_child.right_child = Node(6)

    leftView = LeftView()
    leftView.left_view(root, 1)


