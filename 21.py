class BinomialTree:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []

    def __len__(self):
        return len(self.children)


class BinomialHeap:
    def __init__(self):
        self.trees = []
        self.min_node = None
        self.size = 0

    def is_empty(self):
        return self.min_node is None

    def insert(self, value):
        node = BinomialTree(value)
        new_heap = BinomialHeap()
        new_heap.trees.append(node)
        new_heap.min_node = node
        new_heap.size = 1
        self.merge(new_heap)
        return node

    def peek_min(self):
        return self.min_node.value

    def extract_min(self):
        min_node = self.min_node
        self.trees.remove(min_node)
        child_heap = BinomialHeap()
        child_heap.trees = min_node.children
        child_heap.count = len(min_node)
        self.merge(child_heap)
        self.find_min()
        self.size -= 1
        return min_node.value

    def decrease_key(self, node, new_value):
        if new_value > node.value:
            raise ValueError("New value is greater than current value")
        node.value = new_value
        self.sift_up(node)
        self.find_min()

    def merge_tree(self, t1, t2):
        if t1.value > t2.value:
            t2.children.append(t1)
            t1.parent = t2
            return t2
        else:
            t1.children.append(t2)
            t2.parent = t1
            return t1

    def merge(self, other_heap):
        carry = None
        merged_trees = []
        for i in range(max(len(self.trees), len(other_heap.trees)) + 1):
            try:
                tree1 = self.trees[i]
            except IndexError:
                tree1 = None

            try:
                tree2 = other_heap.trees[i]
            except IndexError:
                tree2 = None

            if tree1 is not None and tree2 is not None and carry is not None:
                merged_trees.append(carry)
                carry = self.merge_tree(tree1, tree2)
            elif tree1 is not None and tree2 is not None:
                carry = self.merge_tree(tree1, tree2)
            elif tree1 is not None and carry is not None:
                carry = self.merge_tree(tree1, carry)
            elif tree2 is not None and carry is not None:
                carry = self.merge_tree(tree2, carry)
            elif tree1 is not None:
                merged_trees.append(tree1)
            elif tree2 is not None:
                merged_trees.append(tree2)
            elif carry is not None:
                merged_trees.append(carry)
                carry = None

        self.trees = merged_trees
        self.size += other_heap.size
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

    def __len__(self):
        return self.size


# Tests
def insert_and_extract_min():
    heap = BinomialHeap()
    heap.insert(8)
    heap.insert(2)
    heap.insert(6)

    assert heap.extract_min() == 2
    assert heap.extract_min() == 6
    assert heap.extract_min() == 8
    assert heap.is_empty()


def peek_min():
    heap = BinomialHeap()
    heap.insert(8)
    heap.insert(2)
    heap.insert(6)
    assert heap.peek_min() == 2


def decrease_key():
    heap = BinomialHeap()
    heap.insert(1)
    heap.insert(2)
    heap.insert(3)
    heap.insert(4)
    heap.insert(5)
    node = heap.insert(6)
    heap.insert(7)
    assert heap.peek_min() == 1
    heap.decrease_key(node, 0)
    heap.insert(8)
    heap.insert(9)
    heap.insert(10)
    assert heap.peek_min() == 0


def delete():
    heap = BinomialHeap()
    node_to_delete = heap.insert(9)
    heap.insert(4)
    heap.delete(node_to_delete)

    assert heap.peek_min() == 4
    assert heap.extract_min() == 4

    assert heap.is_empty()


def merge():
    heap1 = BinomialHeap()
    heap2 = BinomialHeap()
    heap1.insert(1)
    heap1.insert(3)
    heap1.insert(2)
    heap1.insert(4)

    heap2.insert(5)
    heap2.insert(6)
    heap2.insert(7)
    heap2.insert(8)

    heap1.merge(heap2)

    assert heap1.extract_min() == 1
    assert heap1.extract_min() == 2
    assert heap1.extract_min() == 3
    assert heap1.extract_min() == 4
    assert heap1.extract_min() == 5
    assert heap1.extract_min() == 6
    assert heap1.extract_min() == 7
    assert heap1.extract_min() == 8

    assert heap1.is_empty()


if __name__ == "__main__":
    insert_and_extract_min()
    peek_min()
    decrease_key()
    delete()
    merge()

    print("Tests passed")
