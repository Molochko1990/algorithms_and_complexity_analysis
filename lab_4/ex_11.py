class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0)  # Dummy head
        self.tail = Node(0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add(self, node):
        prev_tail = self.tail.prev
        prev_tail.next = node
        node.prev = prev_tail
        node.next = self.tail
        self.tail.prev = node

    def access(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
        else:
            if len(self.cache) == self.capacity:
                lru_node = self.head.next
                self._remove(lru_node)
                del self.cache[lru_node.key]

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


cache_size = 5
requests = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 7, 9, 3]

result = count_cache_misses(cache_size, requests)
print(result)