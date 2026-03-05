#!/usr/bin/env python3

def generate_permutations(arr, path, result):
    if not arr:
        print(f"base {path}")
        result.append(path[:])
        return

    print(f"A {arr}")
    print(f"P {path}")
    for i in range(len(arr)):
        path.append(arr[i])
        generate_permutations(arr[:i] + arr[i+1:], path, result)
        path.pop()

arr    = ['A', 'B', 'C']
path   = [] # working permutation
result = []

generate_permutations( arr, path, result )

#print(result)
