def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True


def get_prime_factors_generator(num):
    if is_prime(num):
        yield num
    else:
        counter = int(num/2) + 1
        while num > 1:
            if num % counter == 0 and is_prime(counter):
                num /= counter
                yield counter
            else:
                counter -= 1
