import heapq
import collections

nums = [1, 3, -1, -3, 5, 3, 6, 7]

window_size: int = 3

def max_sliding_window( nums: list[int], k: int) -> list[int]:

    opts = 0
    output = []
    q = collections.deque();
    l = r = 0

    while r < len(nums):
        opts += 1
        while q and nums[q[-1]] < nums[r]:
            opts += 1
            q.pop()
        q.append(r)

        if l > q[0]:
            q.popleft()

        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1

        r += 1

    print(f"{opts=}")

    return output


print(max_sliding_window(nums, window_size))

nums2 = [1, 4, 3, 2, 2, 5, 0, 9]
print(max_sliding_window(nums2, window_size))

nums3 = [1,1,2,1,1,3,2,2,4]

print(max_sliding_window(nums3, window_size))

nums4 = [7,6,5,4,3,2,1] # O(n)

print(max_sliding_window(nums4, window_size))

nums5 = [1,2,3,4,5,6,7] # O(2n -1)

print(max_sliding_window(nums5, window_size))

nums5 = [1,1,2,1,1,3,4] # O(2n -1)

print(max_sliding_window(nums5, window_size))

