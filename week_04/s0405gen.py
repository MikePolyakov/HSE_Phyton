# Проверка числа на простоту

'''
Write a generator, genPrimes, that returns the sequence of prime numbers
on successive calls to its next() method: 2, 3, 5, 7, 11, ...

Have the generator keep a list of the primes it's generated.
A candidate number x is prime if (x % p) != 0 for all earlier primes p.
'''


def genPrimes():
    prime_list = []
    x = 1
    while True:
        x += 1
        for e in prime_list:
            if x % e == 0:
                break
            else:
                prime_list.append(x)
                yield x

def genPrimes():
    prime_list = []
    x = 1
    while True:
        x += 1
        for elem in prime_list:
            if x % elem == 0:
                break
        else:
            prime_list.append(x)
            yield x

