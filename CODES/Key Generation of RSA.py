from random import randrange, getrandbits
import random
# For generating two large primes p and q, I should use an efficient algorithm.
# Primality testing algorithm are useful for this process.
def is_prime(o, k=128):
    if o == 2 or o == 3:
        return True
    if o <= 1 or o % 2 == 0:
        return False
    # find r and s
    s = 0
    r = o - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, o - 1)
        x_2 = pow(a, r, o)
        if x_2 != 1 and x_2 != o - 1:
            j_1 = 1
            while j_1 < s and x_2 != o - 1:
                x_2 = pow(x_2, 2, o)
                if x_2 == 1:
                    return False
                j_1 += 1
            if x_2 != o - 1:
                return False
    return True


def generate_prime_candidate(length):
    # generate random bits
    m = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    m |= (1 << length - 1) | 1
    return m


def generate_prime_number(length=1024):
    b = 4
    # keep generating while the primality test fail
    while not is_prime(b, 128):
        b = generate_prime_candidate(length)
    return b


# For generating d (decryption key), I need to calculate modular multiplicative inverse of e modulo phi_n.
def modInverse(a, m):
    m0 = m
    y1 = 0
    x_1 = 1
    if m == 1:
        return 0
    while a > 1:
        # q is quotient
        q_1 = a // m

        t = m

        # m is remainder now, process
        # same as Euclid's algorithm
        m = a % m
        a = t
        t = y1

        # Update x and y
        y1 = x_1 - q_1 * y1
        x_1 = t
    # Make x positive
    if x_1 < 0:
        x_1 = x_1 + m0
    return x_1


# Calculates the greatest common divisor of two integers
# Extended Euclidean Algorithm
def gcd(a, b):
    while a != 0 and b != 0:
        rem = a % b
        a = b
        b = rem
    return a


# Here, I generate two large primes (p and q)
p = generate_prime_number()
q = generate_prime_number()

# p should be greater than q. Therefore, if generated q is greater than generated p, I need to swap them.
temp = 0
if p < q:
    temp = p
    p = q
    q = temp

print("p = ", p)
print()
print("q = ", q)

# I calculate n which is multiplication of p and q.
n = p * q
print()
print("n = ", n)

# I calculate phi(n) which is multiplication of (p-1) and (q-1).
phi = (p - 1) * (q - 1)

#  I choose e which is co-prime to n and 1 < e < phi(n).
e = random.randint(1, phi)
g = gcd(e, phi)
while g != 1:
    e = random.randint(1, phi)
    g = gcd(e, phi)

print()
print("e = ", e)
print()
print("phi = ", phi)
# I calculate decryption key d
d = modInverse(e, phi)
d = d % phi
# If d is negative after calculated d mod phi(n), I should make it positive by adding phi(n) to d.
if d < 0:
    d += phi
print()
print("d = ", d)