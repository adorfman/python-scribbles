from typing import Optional

class Node():

    def __init__(self, value, nxt: Optional['Node'] = None):

        self.value = value
        self.nxt   = nxt



def build_list( nums_list: list[int] ):

    start_node = cur_node = Node(None)
    prev_node  = None
    for num in nums_list:
        cur_node.value = num

        if prev_node:
            prev_node.nxt = cur_node

        prev_node = cur_node
        cur_node = Node(num)

    return start_node

def n_from_end( start_node: Node, n: int ):

    offset_node = start_node
    for i in range(n):
        if not offset_node:
            return -1

        offset_node = offset_node.nxt

    while offset_node:
        offset_node = offset_node.nxt
        start_node  = start_node.nxt

    return start_node


#cur_node = start_node

my_nums: list = [3,7,24,65,9,32,11,0,99,4]

start_node = cur_node = build_list(my_nums)
while ( cur_node ):
   print(cur_node.value)
   cur_node = cur_node.nxt

print(n_from_end(start_node, 4).value)




# 3,7,24,65,9,32,11,0,99,4
