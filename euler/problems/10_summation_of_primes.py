def test_if_prime(num):
    for i in range(num):
        if i not in (0, 1, num) and not num % i:
            return False
    return True


def get_sum_of_primes(limit):
    primes = []
    for i in range(limit):
        if test_if_prime(i):
            primes.append(i)
            primes = [sum(primes)]
    return sum(primes)


print get_sum_of_primes(2000000)
