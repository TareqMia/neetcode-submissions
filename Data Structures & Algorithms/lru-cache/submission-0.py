class Node:
    def __init__(self, key, val):
        self.key = key 
        self.val = val 
        self.next = self.prev = None


"""

L -> <- 1 -> <- R ->

"""


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} 
        self.capacity = capacity 
        self.left = Node(-1, -1)
        self.right = Node(-1, -1)
        self.left.next = self.right 
        self.right.prev = self.left
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # return it and make it the most recently used 
        node = self.cache[key]

        # remove the node 
        self.remove(node)

        # add it back
        self.add(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value 
            self.cache[key] = node 

            # remove the node 
            self.remove(node)

            # add it back
            self.add(node)
        else:
            node = Node(key, value)
            self.cache[key] = node 
            self.add(node)


        if len(self.cache) > self.capacity:
            # need to evict LRU 
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]


    def add(self, node):
        prev = self.right.prev
        next = self.right 

        prev.next = node
        next.prev = node 

        node.prev = prev 
        node.next = next

    def remove(self, node):
        prev = node.prev
        next = node.next 

        prev.next = next
        next.prev = prev 



        





            



        
