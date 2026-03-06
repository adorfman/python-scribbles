
def num_bits( n: int ) -> int:
    m = 0x00000001

    one_bits = 0
    while n:

        one_bits += m & n
        n = n >> 1

    return one_bits

print(num_bits(1))
print(num_bits(11))
print(num_bits(255))

def num_bits2( n: int ) -> int:

    one_bits = 0

    while n:
        one_bits += 1
        n &= ( n -1 )

    return one_bits

print(num_bits2(1))
print(num_bits2(11))
print(num_bits2(255))
