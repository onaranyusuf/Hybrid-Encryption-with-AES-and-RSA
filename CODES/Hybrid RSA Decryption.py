import math
print("*********************************************************")
print("Decryption")
print("*********************************************************")
# These dictionaries are used for encryption and decryption processes.
alphabet = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12,
            "N": 13, "O": 14, "P": 15,
            "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25, " ": 26, "a": 27,
            "b": 28, "c": 29, "d": 30, "e": 31, "f": 32, "g": 33, "h": 34, "i": 35, "j": 36, "k": 37, "l": 38, "m": 39,
            "n": 40, "o": 41, "p": 42, "q": 43, "r": 44, "s": 45, "t": 46, "u": 47, "v": 48, "w": 49, "x": 50, "y": 51,
            "z": 52}
alphabet2 = {v: k for k, v in alphabet.items()}
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
# fast modular exponentiation
def fast_exp(base, exponent, modulo):
    r = 1
    if 1 & exponent:
        r = base
    while exponent:
        exponent >>= 1
        base = (base * base) % modulo
        if exponent & 1:
            r = (r * base) % modulo
    return r

# For decryption process, I need to obtain ciphertext and ciphertext integer from public area.

ciphertextInt_1 = int(input("Please enter ciphertextint :"))
ciphertext = input("Please enter the ciphertext: ")


d = int(input("Please enter secret key d: "))
p = int(input("Please enter secret prime p: "))
q = int(input("Please enter secret prime q: "))
# For speeding up calculation of q', I divide it here.
dp = d % (p - 1)
dq = d % (q - 1)
q_inverse = modInverse(q, p)
q_inverse = q_inverse % p

# If q' is negative, I should make it positive.
if q_inverse < 0:
    q_inverse += p

x1 = fast_exp(ciphertextInt_1, dp, p)
x2 = fast_exp(ciphertextInt_1, dq, q)

if x1 > x2:
    h = q_inverse * (x1 - x2) % p
else:
    h = (q_inverse * ((x1 + math.ceil(q / p) * p) - x2)) % p

plaintextInt_1 = (x2 + h * q) % (p * q)

print("Plaintext integer 1 is: ", plaintextInt_1)

plainList = []
for i in ciphertext:
    plainList.append(i)
print(plainList)
reverseList = []
i = len(plainList) - 1
while i >= 0:
    reverseList.append(i)
    i -= 1
print(reverseList)
plaintextInt = 0
# finding plaintext number
plaintextList_0 = []
for f in reverseList:
    j = plaintextInt_1 // 53 ** f
    plaintextList_0.append(j)
    plaintextInt_1 %= 53 ** f

print(plaintextList_0)

# creating ciphertext
plaintextList = []
for i in plaintextList_0:
    if i > 52:
        i %= 53
    plaintextList.append(alphabet2[i])

print(plaintextList)


# I convert plaintextList to decrypted ciphertext (plaintext)
def listToString(s):
    str1 = ""
    for element in s:
        str1 += element
    return str1


plaintext_b = listToString(plaintextList)
print(plaintext_b)


