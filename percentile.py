import math
import functools


def percentile2(N, percent, key=lambda x:x):
    """
    Find the percentile of a list of values.

    @parameter N - is a list of values. Note N MUST BE already sorted.
    @parameter percent - a float value from 0.0 to 1.0.
    @parameter key - optional key function to compute value from each
                     element of N.

    @return - the percentile of the values
    """
    if not N:
        return None
    k = (len(N)-1) * percent
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return key(N[int(k)])
    d0 = key(N[int(f)]) * (c-k)
    d1 = key(N[int(c)]) * (k-f)

    print(f"{k=} {c=} {f=}")
    return d0+d1


# median is 50th percentile.
median = functools.partial(percentile2, percent=0.95)


print(median([25, 26, 64, 69, 75, 76, 89, 90]))


def my_new_func():
    """
    bleh
    """


my_new_func()
