print("*********************************************************")
print("Encryption")
print("*********************************************************")

# These dictionaries are used for encryption and decryption processes.
alphabet = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9, "K": 10, "L": 11, "M": 12,
            "N": 13, "O": 14, "P": 15,
            "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23, "Y": 24, "Z": 25, " ": 26, "a": 27,
            "b": 28, "c": 29, "d": 30, "e": 31, "f": 32, "g": 33, "h": 34, "i": 35, "j": 36, "k": 37, "l": 38, "m": 39,
            "n": 40, "o": 41, "p": 42, "q": 43, "r": 44, "s": 45, "t": 46, "u": 47, "v": 48, "w": 49, "x": 50, "y": 51,
            "z": 52}
alphabet2 = {v: k for k, v in alphabet.items()}

# plaintext should be uppercase characters with no spaces and symbols.
plaintext = input("Please enter the text will be encrypted: ")


# I converted plaintext to plainList to calculate plaintext integer
plainList = list(plaintext)
print(plainList)
reverseList = []
i = len(plainList) - 1
while i >= 0:
    reverseList.append(i)
    i -= 1
print(reverseList)

plaintextInt = 0

y = 0
for x in plainList:
    plaintextInt += alphabet[x] * (53 ** reverseList[y])
    y += 1
print("Plaintext integer is:", plaintextInt)


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


n = int(input("Please enter public key n: "))
e = int(input("Please enter public key e: "))

ciphertextInt = fast_exp(plaintextInt, e, n)
print("Ciphertext integer is: ", ciphertextInt)
tempCipherInt = ciphertextInt

# finding ciphertext number
a = []
for f in range(15, -1, -1):
    l_1 = ciphertextInt // 53 ** f
    a.append(l_1)
    ciphertextInt %= 53 ** f

print(a)

# creating ciphertext
aw = []
for i in a:
    if i > 52:
        i %= 53
    aw.append(alphabet2[i])

print(aw)



# list to string
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


ciphertext = listToString(aw)
print(ciphertext)