PRIME_TARGET = 10001


def test_if_prime(num):
    for i in range(num):
        if i not in (0, 1, num) and not num % i:
            return False
    return True


def get_prime(target):
    prime_counter, num = 0, 1
    while True:
        if test_if_prime(num):
            r = {'prime': prime_counter, 'number': num}
            print r
            prime_counter += 1
            # as it doesn't count itself
            if prime_counter == target + 1:
                return num
        num += 1


print get_prime(PRIME_TARGET)
