n = 2  # 00000010
m = 0xffffffff


def reverse_bits( n: int, b: int ) -> int:

    if b == 1:
        return n

    ml = b / 2

    lm  = m << b
    #   1011 -> 101100 -> 11
    l = (n << ml) & lm >> ml
    r = n >> ml

    l = reverse_bits(l, ml)
    r = reverse_bits(r, ml)




























