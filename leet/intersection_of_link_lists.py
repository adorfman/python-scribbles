# from typing import Self   3.11+
from typing import Optional
from collections import defaultdict

class Node():

    def __init__(self, name: str, nxt: Optional['Node'] = None):

        self.name = name
        self.next = nxt

    def __repr__(self):

        return self.name


def findIntersect(n1: Node, n2: Node):

    next_map = {}

    while n1.next is not None:

        next_map[(n1.next)] = n1.next
        n1 = n1.next

    while n2.next is not None:

        if n2.next in next_map:
            return n2.next

    return None

def fastFindIntersect(n1: Node, n2: Node):

    # a1 a2 c1 c2 c3 b1 b2 c1 c2 c3
    # p1 p2
    #    p1    p2
    #       p1       p2
    #          p1          p2
    #             p12

    n1_end = n1
    while n1_end.next is not None:
        n1_end = n1_end.next

    n1_end.next = n2

    p1: Node | None = n1
    p2: Node | None = n1.next
    while p1 is not None:

        if p2 is None:
            p1 = None
            break

        if (p2 is p1 or
           p2.next is p1 or
           (p2.next is not None and p1 is p2.next.next)):
            break

        p1 = p1.next

        if p2.next is not None:
            p2 = p2.next.next
        else:
            p2 = p2.next

    n1_end.next = None

    return p1


c3 = Node('c3', None)
c2 = Node('c2', c3)
c1 = Node('c1', c2)

b2 = Node('b2', c1)
b1 = Node('b1', b2)

a2 = Node('a2', c1)
a1 = Node('a1', a2)

print(fastFindIntersect(a1, b1))

b2.next = None
a2.next = None

print(fastFindIntersect(a1, b1))

def findIntersection2(n1: Node, n2: Node):
   p1, p2 = n1, n2

   while p1 != p2:
       p1 = p1.next if p1 else n2
       p2 = p2.next if p2 else n1

   return p2

b2.next = c2
a2.next = c2

print(findIntersection2(a1, b1))

b2.next = None
a2.next = None

print(findIntersection2(a1, b1))



