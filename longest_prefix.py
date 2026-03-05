#from itertools import takewhile

def longest_common_prefix_2d(arr):
    if not arr or not arr[0]:
        return []
    return [ x[0] for x in takewhile(lambda x: len(set(x)) == 1, zip(*arr)) ]

def manual_zip(arr):
    if not arr or not arr[0]:
        return [] 

    prefix = []
    cur_idx = 0;
    cur_val = arr[0][cur_idx]

    while True: 

        for i in arr:

            if cur_idx >= len(i) or i[cur_idx] != cur_val:
                return prefix

        cur_idx += 1;
        prefix.append(cur_val)

        if cur_idx >= len(arr[0]):
            break

        cur_val = arr[0][cur_idx]; 

    return prefix

# Example
arr = [[3, 2], [3, 2, 1, 4, 5], [3, 2, 1, 8, 9],[3,2,1]]
#print([ x for x in zip(*arr)])
#print(longest_common_prefix_2d(arr))  # Output: (3, 2, 1)
print(manual_zip(arr))
#print( list(takewhile(lambda x: len(set(x)), zip(*arr) ) )  );
#print( [ len(set(x)) for x in  zip(*arr) ] ); 

# Since 3.7 we have ot catch RuntimeError, A.I. answers are worthless.
# useful list of iterators and generator pattern
def my_zip(*iterables):
    iterators = [ iter(it) for it in iterables ]
    while True:
        try:
            yield tuple( next(it) for it in iterators )
        except RuntimeError as e:
            return


# Example usage
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
my_list_gen = my_zip(list1, list2);

#print(next(my_list_gen))
#print(next(my_list_gen))
#print(next(my_list_gen)) 
#print(next(my_list_gen))  
for x in my_zip(list1, list2):
    print(x)
#print([ x for x in my_zip(list1, list2) ])
#print( list(my_zip(list1, list2)) )  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
