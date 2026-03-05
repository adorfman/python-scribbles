


def find_pos(nums: list[int], target: int ) -> int:

    l,r = 0, len(nums) - 1

    def bin_search( n: list[int], l: int, r: int, t: int ):

        if r < l:
            return [-1,-1]

        m = (l + r) // 2

        mv = n[m]
        print(f"{l=} {m=} {r=} {t=} {mv=}")

        if mv == t:

            lt = bin_search(n, l, m - 1, t)
            rt = bin_search(n, m + 1, r, t)

            return [ m if lt[0] < 0  else lt[0], m if rt[0] < 0  else rt[1] ]
        elif mv > t:
            return bin_search(n, l, m - 1, t)
        else:
            return bin_search(n, m + 1, r, t)

    return bin_search(nums, l, r, target)

nums = [1,3,3,3,5,6,8,8,8,8,8,11,16,21,36,36,41]

#print(find_pos(nums, 5))
print(find_pos(nums, 8))
print(find_pos(nums, 7))
#print(find_pos(nums, 13))
