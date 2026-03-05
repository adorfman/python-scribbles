
def find_min( nums: list[int]) -> int:

    res = nums[0]

    l,r = 0, len(nums) - 1

    while l <= r:
        if nums[l] < nums[r]: # in a sorted subset
            res = min( nums[l], res )
            break

        m = (l + r) // 2
        res = min( nums[m], res )

        if nums[m] >= nums[l]:
            # search right
            l = m + 1
        else:
            r = m - 1

    return res

rotated = [ 6, 7, 8, 9, 10, 3, 4, 5 ]

print(find_min(rotated))

