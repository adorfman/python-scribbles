
class CacheNode:
    def __init__(self, key, val):

        self.key, self.val = key, val

        self.prev = self.next = None

class LRUCache:

    def __init__(self, size: int):
        self.size = size
        self.cache: dict[int, CacheNode] = {}

        # Dummy end nodes, avoids edge cases in
        # in insert/remove functions of dangling ends
        self.left, self.right = CacheNode(0, 0), CacheNode(0, 0)

        # init with ends linked to eachother
        self.left.next, self.right.prev = self.right, self.left

    # splice a nodes prev/next nodes together to remove node
    # from link list
    def remove(self, node):

        prev, nxt = node.prev, node.next

        prev.next, next.prev = nxt, prev

    # insert at end of list by splicing node with right and right.prev nodes
    def insert(self, node):

        prev, nxt = self.right.prev, self.right

        prev.next = next.prev = node

        node.prev, node.next = prev, nxt


    def get(self, key: int ) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val

        return -1


    def put(self, key: int, value: int ) -> None:

        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = CacheNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.size:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

        return None

# LRU [2]   -> null ,
# put [1,1] -> null,
# put [2,2] -> null,
# get [1]   -> 1,
# put [3,3] -> null,
# get [2],  -> -1,
# put [4,4] -> null,
# get [1]   -> -1,
# get [3]   -> 3,
# get [4]   -> 4

cache = LRUCache(2)
print(cache.put(1,1,))
print(cache.put(2,2))
print(cache.get(1))
print(cache.put(3,3))
print(cache.get(2))

print(cache.put(4,4))
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))

