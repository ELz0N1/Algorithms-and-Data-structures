import unittest
from random import randint


class Treap:
    class TreapNode:
        def __init__(self, priority, val, rank, summa):
            self.priority = priority
            self.key = val
            self.rank = rank
            self.sum = summa
            self.right = None
            self.left = None

    def __init__(self):
        self.root = None
        self.priorities = set()

    def gen_prio(self):
        p = randint(0, 2 ** 32 - 1)
        while p in self.priorities:
            p = randint(0, 2 ** 32 - 1)
        self.priorities.add(p)
        return p

    def merge(self, node1, node2):
        if not node1:
            return node2
        if not node2:
            return node1
        if node1.priority < node2.priority:
            node1.right = self.merge(node1.right, node2)
            self.update(node1)
            return node1
        else:
            node2.left = self.merge(node1, node2.left)
            self.update(node2)
            return node2

    def split(self, node, k):
        if not node:
            return [None, None]

        l = 0 if not node.left else node.left.rank
        if k <= l:
            ll, lr = self.split(node.left, k)
            node.left = lr
            self.update(node)
            return ll, node
        else:
            rl, rr = self.split(node.right, k - l - 1)
            node.right = rl
            self.update(node)
            return node, rr

    def insert(self, treap, val, pos):
        r, l = self.split(treap, pos - 1)
        priority = self.gen_prio()
        node = self.TreapNode(priority, val, 1, val)
        r = self.merge(r, node)
        r = self.merge(r, l)
        return r

    def erase(self, root, pos):
        l, r = self.split(root, pos - 1)
        rl, rr = self.split(r, 1)
        root = self.merge(l, rr)
        return root

    def sum(self, _from, to):
        l, r = self.split(self.root, _from - 1)
        rl, rr = self.split(r, to - _from + 1)
        return rl.sum

    def make(self, values):
        n = len(values)
        nodes = [self.TreapNode(self.gen_prio(), values[i], 1, values[i]) for i in range(n)]
        self.root = nodes[0]
        for i in range(1, n):
            self.root = self.merge(self.root, nodes[i])
        return self.root

    def update(self, root):
        rank_left = 0 if not root.left else root.left.rank
        rank_right = 0 if not root.right else root.right.rank
        sum_left = 0 if not root.left else root.left.sum
        sum_right = 0 if not root.right else root.right.sum
        root.sum = sum_left + sum_right + root.key
        root.rank = 1 + rank_left + rank_right


class Tests(unittest.TestCase):
    def test1(self):
        values = [1, 1, 1]
        treap = Treap()
        treap.make(values)
        expected = 3
        self.assertEqual(expected, treap.sum(1, 3))

    def test2(self):
        values = [1, 2, 3]
        treap = Treap()
        treap.make(values)
        treap.insert(treap.root, 4, 4)
        expected = 7
        self.assertEqual(expected, treap.sum(3, 4))

    def test3(self):
        values = [1, 1, 19, 1, 1]
        treap = Treap()
        treap.make(values)
        expected = 19
        self.assertEqual(expected, treap.sum(3, 3))

    def test4(self):
        values = [1, 2, 6, 3, 4, 5]
        treap = Treap()
        treap.make(values)
        treap.erase(treap.root, 3)
        expected = 15
        self.assertEqual(expected, treap.sum(1, 5))


unittest.main()
