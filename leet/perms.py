def generate_permutations(arr, path, result):
    if not arr:
        result.append(path[:])
        return

    for i in range(len(arr)):
        path.append(arr[i])
        print(arr[:i] + arr[i+1:])
        generate_permutations(arr[:i] + arr[i+1:], path, result)
        path.pop()

arr    = ['A', 'B', 'C']
path   = [] # working permutation
result = []

#generate_permutations( arr, path, result )


def rbt_perm( chars: list[str] ) -> list[list[str]]:

    ret = []
    if len(chars) == 1:
        return [chars[:]]

    for i in range(len(chars)):

       num   = chars.pop(0)
       perms = rbt_perm(chars)

       for perm in perms:
           #print(perm)
           perm.append(num)

       ret.extend(perms)
       chars.append(num)

    return ret

print(rbt_perm(['A','B','C']))
