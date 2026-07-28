class Node:
    def __init__(self,key,val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None 
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        self.MRU = Node(0,0)
        self.LRU = Node(0,0)

        self.MRU.next = self.LRU
        self.LRU.prev = self.MRU

    def remove(self,node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def insert(self,node):
        node.next = self.MRU.next
        node.prev = self.MRU

        self.MRU.next.prev = node
        self.MRU.next = node
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key , value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.LRU.prev

            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)