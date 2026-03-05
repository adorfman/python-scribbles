import random

# Worst case is p always being the largest
# value / list already or mostly sorted

def findKthLargest( arr: list[int], k: int ) -> int:

    k = len(arr) - k

    def quick_partition(l, r):

        # r = len(arr) - 1
        # pivot_index = r # random.randint(0, r)

        # arr[pivot_index], arr[r] = arr[r], arr[pivot_index]
        p = arr[r]  # pivot value
        i = l       # pivot pointer

        # 3, 5, 2, 1, 4
        # 3, 5, 2, 1, 4
        # 3, 2, 5, 1, 4
        # 3, 2, 1, 5, 4
        # 3, 2, 1, 4, 5

        for j in range(l, r): # exclude last element we always swap
            # swap with itself until we find larger
            # values. Then next time we find a smaller
            # value go back and swap with first larger
            # value
            if arr[j] <= p:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[r] = arr[r], arr[i]

        if i > k:    return quick_partition(l, i - 1)
        elif i < k:  return quick_partition(i + 1, r)
        else:        return arr[i]

        #return i

    return quick_partition(0, len(arr) - 1)

arr = [ 3, 5, 10, 2, 10, 1, 4, 9, 13, 15, 8 ]

print(findKthLargest(arr, 3))
print(findKthLargest(arr, len(arr) - 4))
print(arr)
