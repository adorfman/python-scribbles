from collections import deque

def quick_sort(nums: list[int]) -> list[int]:

    sorted = []
    q      = deque([nums])

    # [...]
    # [ [...] [7] [...] ]
    # [ [...] [2] [...] [7] [...]]
    # [ [2] [...] [7] [...]]
    # [ [2] [...] [6] [...] [7] [...] ]
    while len(q):

        cur_nums = q.popleft()

        if len(cur_nums) == 1:
            sorted.append(cur_nums[0])
            continue

        pivot = cur_nums[-1]

        l = [ num for num in cur_nums[:-1] if num <  pivot ]
        r = [ num for num in cur_nums[:-1] if num >= pivot ]

        if len(r) > 0:
            q.appendleft(r)
        q.appendleft([pivot])
        if len(l) > 0:
            q.appendleft(l)

    return sorted

nums = [3, 7, 5, 6, 2, 9, 11, 7]
     # [2, 3, 5, 6, 7, 7, 9, 11]
print(quick_sort(nums))
