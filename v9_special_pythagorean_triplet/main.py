'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3squared + 4squared = 9 + 16 = 25 = 5squared.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

import math


def get_product_of_lesser_sum():
    lim = 1000
    x = [a * b * c for c in range(lim) for b in range(lim)
         for a in range(lim)
         if math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2)
         and a < b and b < c and a + b + c == lim]
    return x[0]


print get_product_of_lesser_sum()
