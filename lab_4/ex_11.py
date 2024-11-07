class Node:
    """Class for representing a node in a doubly linked list."""
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    """LRU Cache implemented with a dictionary and a doubly linked list."""
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0)  # Dummy head
        self.tail = Node(0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove a node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node):
        """Add a node right before the tail (most recently used)."""
        prev_tail = self.tail.prev
        prev_tail.next = node
        node.prev = prev_tail
        node.next = self.tail
        self.tail.prev = node

    def access(self, key):
        """Access an item in the cache, or add it if it's a cache miss."""
        if key in self.cache:
            # Cache hit: Move the node to the end (most recently used)
            node = self.cache[key]
            self._remove(node)
            self._add(node)
        else:
            # Cache miss: Add new node to the end
            if len(self.cache) == self.capacity:
                # Remove the least recently used item
                lru_node = self.head.next
                self._remove(lru_node)
                del self.cache[lru_node.key]

            # Add new node
            new_node = Node(key)
            self.cache[key] = new_node
            self._add(new_node)

def count_cache_misses(cache_size, requests):
    lru_cache = LRUCache(cache_size)
    cache_misses = 0

    for request in requests:
        if request not in lru_cache.cache:
            cache_misses += 1
        lru_cache.access(request)

    return cache_misses

# Чтение данных из ввода
import sys

input_data = sys.stdin.read().strip().split()
cache_size = int(input_data[0])
num_requests = int(input_data[1])
requests = list(map(int, input_data[2:]))

# Вычисляем количество обращений к распределенной системе
result = count_cache_misses(cache_size, requests)
print(result)