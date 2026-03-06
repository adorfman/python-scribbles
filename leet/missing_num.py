nums = [ 3, 0, 1 ]

h = nums[0]
l = nums[len(nums)-1]

for num in nums:
    if num > h:
        h = num
    if num < l:
        l = num

print(f"{l=} {h=}")

xor_t = 0

for n in nums + [n for n in range(l,h+1)]:
    print(f"{n}\n")
    xor_t ^= n

print(xor_t)

range_total = 0
for n in range(l,h+1):
    range_total += n

num_total = 0
for n in nums:
    num_total += n

print(range_total - num_total)

