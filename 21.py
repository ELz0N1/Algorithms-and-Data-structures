class Node:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.children = []


class BinomialHeap:
    def __init__(self):
        self.trees = []
        self.min_node = None
        self.count = 0

    def is_empty(self):
        return self.min_node is None

    def insert(self, value):
        node = Node(value)
        new_heap = BinomialHeap()
        new_heap.trees.append(node)
        new_heap.min_node = node
        new_heap.count = 1
        self.merge(new_heap)
        return node

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
        self.find_min()
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


#Tests
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
    node_to_decrease = heap.insert(3)
    assert heap.peek_min() == 3
    heap.decrease_key(node_to_decrease, 1)
    assert heap.peek_min() == 1


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

    print("All tests passed")
