class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.lru = Node(0, 0)   # left sentinel (LRU side)
        self.mru = Node(0, 0)   # right sentinel (MRU side)

        self.lru.next = self.mru
        self.mru.prev = self.lru

    def remove(self, node: Node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node: Node):
        # insert right before MRU sentinel
        prev, nxt = self.mru.prev, self.mru
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru_node = self.lru.next
            self.remove(lru_node)
            del self.cache[lru_node.key]
