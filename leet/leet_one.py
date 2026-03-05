

def two_sum(nums: list[int], target: int ) -> list[int]:
    map = {}

    for i in range(len(nums)):

        needed = target - nums[i];

        if ( needed in map ):
            idx = map[needed]
            return [i, idx]
        else:
            map[nums[i]] = i

    return []


nums = [2,1,5,3]
print(two_sum(nums,4))

nums2 = [5,3,8,4,7,2,1]
print(two_sum(nums2,10))
