class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []
        self.degree = 0
        self.marked = False


class BinomialHeap:
    def __init__(self):
        self.trees = []
        self.min_node = None
        self.count = 0

    def is_empty(self):
        return self.min_node is None

    def insert(self, value):
        node = Node(value)
        self.merge(BinomialHeap(node))

    def peek_min(self):
        return self.min_node.value

    def extract_min(self):
        min_node = self.min_node
        self.trees.remove(min_node)
        self.merge(BinomialHeap(*min_node.children))
        self.find_min()
        self.count -= 1
        return min_node.value

    def decrease_key(self, node, new_value):
        if new_value > node.value:
            raise ValueError("New value is greater than current value")
        node.value = new_value
        self.sift_up(node)

    def merge(self, other_heap):
        self.trees.extend(other_heap.trees)
        self.count += other_heap.count
        self.find_min()

    def delete(self, node):
        self.decrease_key(node, float('-inf'))
        self.extract_min()

    def find_min(self):
        self.min_node = None
        for tree in self.trees:
            if self.min_node is None or tree.value < self.min_node.value:
                self.min_node = tree

    def sift_up(self, node):
        parent = node.parent
        while parent is not None and node.value < parent.value:
            node.value, parent.value = parent.value, node.value
            node, parent = parent, node

    def __len__(self):
        return self.count


