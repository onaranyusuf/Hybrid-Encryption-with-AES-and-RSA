
print("AES - Input")
flag = True
str_key = input("Please enter your key (It should contain 16 ASCII characters): ")
str_plaintext = input("Please enter the message you want to encrypt (It should be 128 bits): ")
while flag:
    if len(str_key) > 16 or len(str_plaintext) > 16:
        str_key = input("Please enter your key (It should contain 16 ASCII characters): ")
        str_plaintext = input("Please enter the message you want to encrypt (It should be 128 bits): ")
    else:
        flag = False

key = []
for a in str_key:
    hex_s = hex(ord(a))
    x = int(hex_s, 16)
    hex_n = hex(x)
    key.append(hex_n)

plaintext = []
for b in str_plaintext:
    hex_s = hex(ord(b))
    x = int(hex_s, 16)
    hex_n = hex(x)
    plaintext.append(hex_n)

print()
print("Key (Round Key 0): ", key)
#decryption round key 0
row_11, row_22, row_33, row_44 = [0] * 4, [0] * 4, [0] * 4, [0] * 4
kkk, lll, mmm, nnn = 0, 1, 2, 3

for iii in range(4):
    row_11[iii] = key[kkk]
    row_22[iii] = key[lll]
    row_33[iii] = key[mmm]
    row_44[iii] = key[nnn]
    kkk += 4
    lll += 4
    mmm += 4
    nnn += 4
dec_rkey0 = [
    row_11,
    row_22,
    row_33,
    row_44
]
print("Plaintext: ", plaintext)

print()
print("AES - RoundKey")

s_box = {"0x0": "0x63", "0x1": "0x7c", "0x2": "0x77", "0x3": "0x7b", "0x4": "0xf2", "0x5": "0x6b", "0x6": "0x6f",
         "0x7": "0xc5", "0x8": "0x30", "0x9": "0x1", "0xa": "0x67", "0xb": "0x2b", "0xc": "0xfe", "0xd": "0xd7",
         "0xe": "0xab", "0xf": "0x76", "0x10": "0xca", "0x11": "0x82", "0x12": "0xc9", "0x13": "0x7d", "0x14": "0xfa",
         "0x15": "0x59", "0x16": "0x47", "0x17": "0xf0", "0x18": "0xad", "0x19": "0xd4", "0x1a": "0xa2", "0x1b": "0xaf",
         "0x1c": "0x9c", "0x1d": "0xa4", "0x1e": "0x72", "0x1f": "0xc0", "0x20": "0xb7", "0x21": "0xfd", "0x22": "0x93",
         "0x23": "0x26", "0x24": "0x36", "0x25": "0x3f", "0x26": "0xf7", "0x27": "0xcc", "0x28": "0x34", "0x29": "0xa5",
         "0x2a": "0xe5", "0x2b": "0xf1", "0x2c": "0x71", "0x2d": "0xd8", "0x2e": "0x31", "0x2f": "0x15", "0x30": "0x4",
         "0x31": "0xc7", "0x32": "0x23", "0x33": "0xc3", "0x34": "0x18", "0x35": "0x96", "0x36": "0xd5", "0x37": "0x9a",
         "0x38": "0x7", "0x39": "0x12", "0x3a": "0x80", "0x3b": "0xe2", "0x3c": "0xeb", "0x3d": "0x27", "0x3e": "0xb2",
         "0x3f": "0x75", "0x40": "0x9", "0x41": "0x83", "0x42": "0x2c", "0x43": "0x1a", "0x44": "0x1b", "0x45": "0x6e",
         "0x46": "0x5a", "0x47": "0xa0", "0x48": "0x52", "0x49": "0x3b", "0x4a": "0xd6", "0x4b": "0xb3", "0x4c": "0x29",
         "0x4d": "0xe3", "0x4e": "0x2f", "0x4f": "0x84", "0x50": "0x53", "0x51": "0xd1", "0x52": "0x0", "0x53": "0xed",
         "0x54": "0x20", "0x55": "0xfc", "0x56": "0xb1", "0x57": "0x5b", "0x58": "0x6a", "0x59": "0xcb", "0x5a": "0xbe",
         "0x5b": "0x39", "0x5c": "0x4a", "0x5d": "0x4c", "0x5e": "0x58", "0x5f": "0xcf", "0x60": "0xd0", "0x61": "0xef",
         "0x62": "0xaa", "0x63": "0xfb", "0x64": "0x43", "0x65": "0x4d", "0x66": "0x33", "0x67": "0x85", "0x68": "0x45",
         "0x69": "0xf9", "0x6a": "0x2", "0x6b": "0x7f", "0x6c": "0x50", "0x6d": "0x3c", "0x6e": "0x9f", "0x6f": "0xa8",
         "0x70": "0x51", "0x71": "0xa3", "0x72": "0x40", "0x73": "0x8f", "0x74": "0x92", "0x75": "0x9d", "0x76": "0x38",
         "0x77": "0xf5", "0x78": "0xbc", "0x79": "0xb6", "0x7a": "0xda", "0x7b": "0x21", "0x7c": "0x10", "0x7d": "0xff",
         "0x7e": "0xf3", "0x7f": "0xd2", "0x80": "0xcd", "0x81": "0xc", "0x82": "0x13", "0x83": "0xec", "0x84": "0x5f",
         "0x85": "0x97", "0x86": "0x44", "0x87": "0x17", "0x88": "0xc4", "0x89": "0xa7", "0x8a": "0x7e", "0x8b": "0x3d",
         "0x8c": "0x64", "0x8d": "0x5d", "0x8e": "0x19", "0x8f": "0x73", "0x90": "0x60", "0x91": "0x81", "0x92": "0x4f",
         "0x93": "0xdc", "0x94": "0x22", "0x95": "0x2a", "0x96": "0x90", "0x97": "0x88", "0x98": "0x46", "0x99": "0xee",
         "0x9a": "0xb8", "0x9b": "0x14", "0x9c": "0xde", "0x9d": "0x5e", "0x9e": "0xb", "0x9f": "0xdb", "0xa0": "0xe0",
         "0xa1": "0x32", "0xa2": "0x3a", "0xa3": "0xa", "0xa4": "0x49", "0xa5": "0x6", "0xa6": "0x24", "0xa7": "0x5c",
         "0xa8": "0xc2", "0xa9": "0xd3", "0xaa": "0xac", "0xab": "0x62", "0xac": "0x91", "0xad": "0x95", "0xae": "0xe4",
         "0xaf": "0x79", "0xb0": "0xe7", "0xb1": "0xc8", "0xb2": "0x37", "0xb3": "0x6d", "0xb4": "0x8d", "0xb5": "0xd5",
         "0xb6": "0x4e", "0xb7": "0xa9", "0xb8": "0x6c", "0xb9": "0x56", "0xba": "0xf4", "0xbb": "0xea", "0xbc": "0x65",
         "0xbd": "0x7a", "0xbe": "0xae", "0xbf": "0x8", "0xc0": "0xba", "0xc1": "0x78", "0xc2": "0x25", "0xc3": "0x2e",
         "0xc4": "0x1c", "0xc5": "0xa6", "0xc6": "0xb4", "0xc7": "0xc6", "0xc8": "0xe8", "0xc9": "0xdd", "0xca": "0x74",
         "0xcb": "0x1f", "0xcc": "0x4b", "0xcd": "0xbd", "0xce": "0x8b", "0xcf": "0x8a", "0xd0": "0x70", "0xd1": "0x3e",
         "0xd2": "0xb5", "0xd3": "0x66", "0xd4": "0x48", "0xd5": "0x3", "0xd6": "0xf6", "0xd7": "0xe", "0xd8": "0x61",
         "0xd9": "0x35", "0xda": "0x57", "0xdb": "0xb9", "0xdc": "0x86", "0xdd": "0xc1", "0xde": "0x1d", "0xdf": "0x9e",
         "0xe0": "0xe1", "0xe1": "0xf8", "0xe2": "0x98", "0xe3": "0x11", "0xe4": "0x69", "0xe5": "0xd9", "0xe6": "0x8e",
         "0xe7": "0x94", "0xe8": "0x9b", "0xe9": "0x1e", "0xea": "0x87", "0xeb": "0xe9", "0xec": "0xce", "0xed": "0x55",
         "0xee": "0x28", "0xef": "0xdf", "0xf0": "0x8c", "0xf1": "0xa1", "0xf2": "0x89", "0xf3": "0xd", "0xf4": "0xbf",
         "0xf5": "0xe6", "0xf6": "0x42", "0xf7": "0x68", "0xf8": "0x41", "0xf9": "0x99", "0xfa": "0x2d", "0xfb": "0xf",
         "0xfc": "0xb0", "0xfd": "0x54", "0xfe": "0xbb", "0xff": "0x16"}

inv_s_box = {v: k for k, v in s_box.items()}

round_constant_array = [["0x01", "0x00", "0x00", "0x00"], ["0x02", "0x00", "0x00", "0x00"],
                        ["0x04", "0x00", "0x00", "0x00"], ["0x08", "0x00", "0x00", "0x00"],
                        ["0x10", "0x00", "0x00", "0x00"], ["0x20", "0x00", "0x00", "0x00"],
                        ["0x40", "0x00", "0x00", "0x00"], ["0x80", "0x00", "0x00", "0x00"],
                        ["0x1b", "0x00", "0x00", "0x00"], ["0x36", "0x00", "0x00", "0x00"]]


def split_array(round_key):
    w_0 = []
    w_1 = []
    w_2 = []
    w3_ = []
    i = 0
    for c in round_key:
        if 0 <= i <= 3:
            w_0.append(c)
        if 4 <= i <= 7:
            w_1.append(c)
        if 8 <= i <= 11:
            w_2.append(c)
        if 12 <= i <= 15:
            w3_.append(c)
        i += 1
    return w_0, w_1, w_2, w3_


def circular_byte_leftshift(arr):
    temp = arr[0]
    for o in range(3):
        arr[o] = arr[o + 1]

    arr[3] = temp
    return arr


def byte_substitution(arr):
    sub_list = []
    for s in arr:
        sub_list.append(s_box.get(s))
    return sub_list


def add_round_constant(step):
    j = 0
    w_3 = []
    for i in sub_arr_new:
        e1 = int(i, 16)
        e2 = int(round_constant_array[step][j], 16)
        j += 1
        addition = e1 ^ e2
        w_3.append(hex(addition))
    return w_3


w0, w1, w2, w3 = split_array(key)
print("w[0], w[1], w[2], w[3] = ", split_array(key))


temp_array = w3.copy()
arr_new = circular_byte_leftshift(w3)
print("circular byte left shift of w[3]:", arr_new)
sub_arr_new = byte_substitution(arr_new)
print("Byte Substitution (S-Box):", sub_arr_new)
gw3 = add_round_constant(0)
print("Adding round constant gives: g(w[3]) = ", gw3)

w4 = []
t1 = []
t2 = []
for u in w0:
    t1.append(int(u, 16))
for p in gw3:
    t2.append(int(p, 16))

for y in range(len(t1)):
    total = t1[y] ^ t2[y]
    w4.append(hex(total))

print("w[4] = ", w4)

w5 = []
t11 = []
t22 = []
for u in w1:
    t11.append(int(u, 16))
for p in w4:
    t22.append(int(p, 16))

for y in range(len(t1)):
    total = t11[y] ^ t22[y]
    w5.append(hex(total))

print("w[5] = ", w5)

w6 = []
t111 = []
t222 = []
for u in w2:
    t111.append(int(u, 16))
for p in w5:
    t222.append(int(p, 16))

for y in range(len(t1)):
    total = t111[y] ^ t222[y]
    w6.append(hex(total))

print("w[6] = ", w6)

w7 = []
t1111 = []
t2222 = []
for u in temp_array:
    t1111.append(int(u, 16))
for p in w6:
    t2222.append(int(p, 16))

for y in range(len(t1)):
    total = t1111[y] ^ t2222[y]
    w7.append(hex(total))

print("w[7] = ", w7)

first_r_key_arr = w4 + w5 + w6 + w7
print("First round key = ", first_r_key_arr)
#decryption round key 1
row_11, row_22, row_33, row_44 = [0] * 4, [0] * 4, [0] * 4, [0] * 4
kkk, lll, mmm, nnn = 0, 1, 2, 3

for iii in range(4):
    row_11[iii] = first_r_key_arr[kkk]
    row_22[iii] = first_r_key_arr[lll]
    row_33[iii] = first_r_key_arr[mmm]
    row_44[iii] = first_r_key_arr[nnn]
    kkk += 4
    lll += 4
    mmm += 4
    nnn += 4
dec_rkey1 = [
    row_11,
    row_22,
    row_33,
    row_44
]

w8, w9, w10, w11 = split_array(first_r_key_arr)
print("w[8], w[9], w[10], w[11] = ", w8, w9, w10, w11)
temp_array_2 = w11.copy()
arr_new = circular_byte_leftshift(w11)
print("circular byte left shift of w[11]:", arr_new)
sub_arr_new = byte_substitution(arr_new)
print("Byte Substitution (S-Box):", sub_arr_new)
gw11 = add_round_constant(1)
print("Adding round constant gives: g(w[11]) = ", gw11)

w12 = []
t1 = []
t2 = []
for u in w8:
    t1.append(int(u, 16))
for p in gw11:
    t2.append(int(p, 16))

for y in range(len(t1)):
    total = t1[y] ^ t2[y]
    w12.append(hex(total))

print("w[12] = ", w12)

w13 = []
t11 = []
t22 = []
for u in w9:
    t11.append(int(u, 16))
for p in w12:
    t22.append(int(p, 16))

for y in range(len(t1)):
    total = t11[y] ^ t22[y]
    w13.append(hex(total))

print("w[13] = ", w13)

w14 = []
t111 = []
t222 = []
for u in w10:
    t111.append(int(u, 16))
for p in w13:
    t222.append(int(p, 16))

for y in range(len(t1)):
    total = t111[y] ^ t222[y]
    w14.append(hex(total))

print("w[14] = ", w14)

w15 = []
t1111 = []
t2222 = []
for u in temp_array_2:
    t1111.append(int(u, 16))
for p in w14:
    t2222.append(int(p, 16))

for y in range(len(t1)):
    total = t1111[y] ^ t2222[y]
    w15.append(hex(total))

print("w[15] = ", w15)

second_r_key_arr = w12 + w13 + w14 + w15
print("Second round key = ", second_r_key_arr)
#decryption round key 2
row_11, row_22, row_33, row_44 = [0] * 4, [0] * 4, [0] * 4, [0] * 4
kkk, lll, mmm, nnn = 0, 1, 2, 3

for iii in range(4):
    row_11[iii] = second_r_key_arr[kkk]
    row_22[iii] = second_r_key_arr[lll]
    row_33[iii] = second_r_key_arr[mmm]
    row_44[iii] = second_r_key_arr[nnn]
    kkk += 4
    lll += 4
    mmm += 4
    nnn += 4

dec_rkey2 = [
    row_11,
    row_22,
    row_33,
    row_44
]

w16, w17, w18, w19 = split_array(second_r_key_arr)
print("w[16], w[17], w[18], w[19] = ", w16, w17, w18, w19)
temp_array_3 = w19.copy()
arr_new = circular_byte_leftshift(w19)
print("circular byte left shift of w[19]:", arr_new)
sub_arr_new = byte_substitution(arr_new)
print("Byte Substitution (S-Box):", sub_arr_new)
gw19 = add_round_constant(2)
print("Adding round constant gives: g(w[19]) = ", gw19)

w20 = []
t1 = []
t2 = []
for u in w16:
    t1.append(int(u, 16))
for p in gw19:
    t2.append(int(p, 16))

for y in range(len(t1)):
    total = t1[y] ^ t2[y]
    w20.append(hex(total))

print("w[20] = ", w20)

w21 = []
t11 = []
t22 = []
for u in w17:
    t11.append(int(u, 16))
for p in w20:
    t22.append(int(p, 16))

for y in range(len(t1)):
    total = t11[y] ^ t22[y]
    w21.append(hex(total))

print("w[21] = ", w21)

w22 = []
t111 = []
t222 = []
for u in w18:
    t111.append(int(u, 16))
for p in w21:
    t222.append(int(p, 16))

for y in range(len(t1)):
    total = t111[y] ^ t222[y]
    w22.append(hex(total))

print("w[22] = ", w22)

w23 = []
t1111 = []
t2222 = []
for u in temp_array_3:
    t1111.append(int(u, 16))
for p in w22:
    t2222.append(int(p, 16))

for y in range(len(t1)):
    total = t1111[y] ^ t2222[y]
    w23.append(hex(total))

print("w[23] = ", w23)

third_r_key_arr = w20 + w21 + w22 + w23
print("Third round key = ", third_r_key_arr)
#decryption round key 3
row_11, row_22, row_33, row_44 = [0] * 4, [0] * 4, [0] * 4, [0] * 4
kkk, lll, mmm, nnn = 0, 1, 2, 3

for iii in range(4):
    row_11[iii] = third_r_key_arr[kkk]
    row_22[iii] = third_r_key_arr[lll]
    row_33[iii] = third_r_key_arr[mmm]
    row_44[iii] = third_r_key_arr[nnn]
    kkk += 4
    lll += 4
    mmm += 4
    nnn += 4
dec_rkey3 = [
    row_11,
    row_22,
    row_33,
    row_44
]

w24, w25, w26, w27 = split_array(third_r_key_arr)
print("w[24], w[25], w[26], w[27] = ", w24, w25, w26, w27)
temp_array_4 = w27.copy()
arr_new = circular_byte_leftshift(w27)
print("circular byte left shift of w[27]:", arr_new)
sub_arr_new = byte_substitution(arr_new)
print("Byte Substitution (S-Box):", sub_arr_new)
gw27 = add_round_constant(3)
print("Adding round constant gives: g(w[27]) = ", gw27)

w28 = []
t1 = []
t2 = []
for u in w24:
    t1.append(int(u, 16))
for p in gw27:
    t2.append(int(p, 16))

for y in range(len(t1)):
    total = t1[y] ^ t2[y]
    w28.append(hex(total))

print("w[28] = ", w28)

w29 = []
t11 = []
t22 = []
for u in w25:
    t11.append(int(u, 16))
for p in w28:
    t22.append(int(p, 16))

for y in range(len(t1)):
    total = t11[y] ^ t22[y]
    w29.append(hex(total))

print("w[29] = ", w29)

w30 = []
t111 = []
t222 = []
for u in w26:
    t111.append(int(u, 16))
for p in w29:
    t222.append(int(p, 16))

for y in range(len(t1)):
    total = t111[y] ^ t222[y]
    w30.append(hex(total))

print("w[30] = ", w30)

w31 = []
t1111 = []
t2222 = []
for u in temp_array_4:
    t1111.append(int(u, 16))
for p in w30:
    t2222.append(int(p, 16))

for y in range(len(t1)):
    total = t1111[y] ^ t2222[y]
    w31.append(hex(total))

print("w[31] = ", w31)

fourth_r_key_arr = w28 + w29 + w30 + w31
print("Fourth round key = ", fourth_r_key_arr)
#decryption round key 4
row_11, row_22, row_33, row_44 = [0] * 4, [0] * 4, [0] * 4, [0] * 4
kkk, lll, mmm, nnn = 0, 1, 2, 3

for iii in range(4):
    row_11[iii] = fourth_r_key_arr[kkk]
    row_22[iii] = fourth_r_key_arr[lll]
    row_33[iii] = fourth_r_key_arr[mmm]
    row_44[iii] = fourth_r_key_arr[nnn]
    kkk += 4
    lll += 4
    mmm += 4
    nnn += 4
dec_rkey4 = [
    row_11,
    row_22,
    row_33,
    row_44
]

w32, w33, w34, w35 = split_array(fourth_r_key_arr)
print("w[32], w[33], w[34], w[35] = ", w32, w33, w34, w35)
temp_array_5 = w35.copy()
arr_new = circular_byte_leftshift(w35)
print("circular byte left shift of w[35]:", arr_new)
sub_arr_new = byte_substitution(arr_new)
print("Byte Substitution (S-Box):", sub_arr_new)
gw35 = add_round_constant(4)
print("Adding round constant gives: g(w[35]) = ", gw35)

w36 = []
t1 = []
t2 = []
for u in w32:
    t1.append(int(u, 16))
for p in gw35:
    t2.append(int(p, 16))

for y in range(len(t1)):
    total = t1[y] ^ t2[y]
    w36.append(hex(total))

print("w[36] = ", w36)

w37 = []
t11 = []
t22 = []
for u in w33:
    t11.append(int(u, 16))
for p in w36:
    t22.append(int(p, 16))

for y in range(len(t1)):
    total = t11[y] ^ t22[y]
    w37.append(hex(total))

print("w[37] = ", w37)

w38 = []
t111 = []
t222 = []
for u in w34:
    t111.append(int(u, 16))
for p in w37:
    t222.append(int(p, 16))

for y in range(len(t1)):
    total = t111[y] ^ t222[y]
    w38.append(hex(total))

print("w[38] = ", w38)

w39 = []
t1111 = []
t2222 = []
for u in temp_array_5:
    t1111.append(int(u, 16))
for p in w38:
    t2222.append(int(p, 16))

for y in range(len(t1)):
    total = t1111[y] ^ t2222[y]
    w39.append(hex(total))

print("w[39] = ", w39)

fifth_r_key_arr = w36 + w37 + w38 + w39
print("Fifth round key = ", fifth_r_key_arr)

#decryption round key 5
row_11, row_22, row_33, row_44 = [0] * 4, [0] * 4, [0] * 4, [0] * 4
kkk, lll, mmm, nnn = 0, 1, 2, 3

for iii in range(4):
    row_11[iii] = fifth_r_key_arr[kkk]
    row_22[iii] = fifth_r_key_arr[lll]
    row_33[iii] = fifth_r_key_arr[mmm]
    row_44[iii] = fifth_r_key_arr[nnn]
    kkk += 4
    lll += 4
    mmm += 4
    nnn += 4
dec_rkey5 = [
    row_11,
    row_22,
    row_33,
    row_44
]
w40, w41, w42, w43 = split_array(fifth_r_key_arr)
print("w[40], w[41], w[42], w[43] = ", w40, w41, w42, w43)
temp_array_6 = w43.copy()
arr_new = circular_byte_leftshift(w43)
print("circular byte left shift of w[43]:", arr_new)
sub_arr_new = byte_substitution(arr_new)
print("Byte Substitution (S-Box):", sub_arr_new)
gw43 = add_round_constant(5)
print("Adding round constant gives: g(w[43]) = ", gw43)

w44 = []
t1 = []
t2 = []
for u in w40:
    t1.append(int(u, 16))
for p in gw43:
    t2.append(int(p, 16))

for y in range(len(t1)):
    total = t1[y] ^ t2[y]
    w44.append(hex(total))

print("w[44] = ", w44)

w45 = []
t11 = []
t22 = []
for u in w41:
    t11.append(int(u, 16))
for p in w44:
    t22.append(int(p, 16))

for y in range(len(t1)):
    total = t11[y] ^ t22[y]
    w45.append(hex(total))

print("w[45] = ", w45)

w46 = []
t111 = []
t222 = []
for u in w42:
    t111.append(int(u, 16))
for p in w45:
    t222.append(int(p, 16))

for y in range(len(t1)):
    total = t111[y] ^ t222[y]
    w46.append(hex(total))

print("w[46] = ", w46)

w47 = []
t1111 = []
t2222 = []
for u in temp_array_6:
    t1111.append(int(u, 16))
for p in w46:
    t2222.append(int(p, 16))

for y in range(len(t1)):
    total = t1111[y] ^ t2222[y]
    w47.append(hex(total))

print("w[47] = ", w47)

sixth_r_key_arr = w44 + w45 + w46 + w47
print("Sixth round key = ", sixth_r_key_arr)

#decryption round key 6
row_11, row_22, row_33, row_44 = [0] * 4, [0] * 4, [0] * 4, [0] * 4
kkk, lll, mmm, nnn = 0, 1, 2, 3

for iii in range(4):
    row_11[iii] = sixth_r_key_arr[kkk]
    row_22[iii] = sixth_r_key_arr[lll]
    row_33[iii] = sixth_r_key_arr[mmm]
    row_44[iii] = sixth_r_key_arr[nnn]
    kkk += 4
    lll += 4
    mmm += 4
    nnn += 4
dec_rkey6 = [
    row_11,
    row_22,
    row_33,
    row_44
]
w48, w49, w50, w51 = split_array(sixth_r_key_arr)
print("w[48], w[49], w[50], w[51] = ", w48, w49, w50, w51)
temp_array_7 = w51.copy()
arr_new = circular_byte_leftshift(w51)
print("circular byte left shift of w[51]:", arr_new)
sub_arr_new = byte_substitution(arr_new)
print("Byte Substitution (S-Box):", sub_arr_new)
gw51 = add_round_constant(6)
print("Adding round constant gives: g(w[51]) = ", gw51)

w52 = []
t1 = []
t2 = []
for u in w48:
    t1.append(int(u, 16))
for p in gw51:
    t2.append(int(p, 16))

for y in range(len(t1)):
    total = t1[y] ^ t2[y]
    w52.append(hex(total))

print("w[52] = ", w52)

w53 = []
t11 = []
t22 = []
for u in w49:
    t11.append(int(u, 16))
for p in w52:
    t22.append(int(p, 16))

for y in range(len(t1)):
    total = t11[y] ^ t22[y]
    w53.append(hex(total))

print("w[53] = ", w53)

w54 = []
t111 = []
t222 = []
for u in w50:
    t111.append(int(u, 16))
for p in w53:
    t222.append(int(p, 16))

for y in range(len(t1)):
    total = t111[y] ^ t222[y]
    w54.append(hex(total))

print("w[54] = ", w54)

w55 = []
t1111 = []
t2222 = []
for u in temp_array_7:
    t1111.append(int(u, 16))
for p in w54:
    t2222.append(int(p, 16))

for y in range(len(t1)):
    total = t1111[y] ^ t2222[y]
    w55.append(hex(total))

print("w[55] = ", w55)

seventh_r_key_arr = w52 + w53 + w54 + w55
print("Seventh round key = ", seventh_r_key_arr)
#decryption round key 7
row_11, row_22, row_33, row_44 = [0] * 4, [0] * 4, [0] * 4, [0] * 4
kkk, lll, mmm, nnn = 0, 1, 2, 3

for iii in range(4):
    row_11[iii] = seventh_r_key_arr[kkk]
    row_22[iii] = seventh_r_key_arr[lll]
    row_33[iii] = seventh_r_key_arr[mmm]
    row_44[iii] = seventh_r_key_arr[nnn]
    kkk += 4
    lll += 4
    mmm += 4
    nnn += 4
dec_rkey7 = [
    row_11,
    row_22,
    row_33,
    row_44
]
w56, w57, w58, w59 = split_array(seventh_r_key_arr)
print("w[56], w[57], w[58], w[59] = ", w56, w57, w58, w59)
temp_array_8 = w59.copy()
arr_new = circular_byte_leftshift(w59)
print("circular byte left shift of w[59]:", arr_new)
sub_arr_new = byte_substitution(arr_new)
print("Byte Substitution (S-Box):", sub_arr_new)
gw59 = add_round_constant(7)
print("Adding round constant gives: g(w[59]) = ", gw59)

w60 = []
t1 = []
t2 = []
for u in w56:
    t1.append(int(u, 16))
for p in gw59:
    t2.append(int(p, 16))

for y in range(len(t1)):
    total = t1[y] ^ t2[y]
    w60.append(hex(total))

print("w[60] = ", w60)

w61 = []
t11 = []
t22 = []
for u in w57:
    t11.append(int(u, 16))
for p in w60:
    t22.append(int(p, 16))

for y in range(len(t1)):
    total = t11[y] ^ t22[y]
    w61.append(hex(total))

print("w[61] = ", w61)

w62 = []
t111 = []
t222 = []
for u in w58:
    t111.append(int(u, 16))
for p in w61:
    t222.append(int(p, 16))

for y in range(len(t1)):
    total = t111[y] ^ t222[y]
    w62.append(hex(total))

print("w[62] = ", w62)

w63 = []
t1111 = []
t2222 = []
for u in temp_array_8:
    t1111.append(int(u, 16))
for p in w62:
    t2222.append(int(p, 16))

for y in range(len(t1)):
    total = t1111[y] ^ t2222[y]
    w63.append(hex(total))

print("w[63] = ", w63)

eighth_r_key_arr = w60 + w61 + w62 + w63
print("Eighth round key = ", eighth_r_key_arr)
#decryption round key 8
row_11, row_22, row_33, row_44 = [0] * 4, [0] * 4, [0] * 4, [0] * 4
kkk, lll, mmm, nnn = 0, 1, 2, 3

for iii in range(4):
    row_11[iii] = eighth_r_key_arr[kkk]
    row_22[iii] = eighth_r_key_arr[lll]
    row_33[iii] = eighth_r_key_arr[mmm]
    row_44[iii] = eighth_r_key_arr[nnn]
    kkk += 4
    lll += 4
    mmm += 4
    nnn += 4
dec_rkey8 = [
    row_11,
    row_22,
    row_33,
    row_44
]
w64, w65, w66, w67 = split_array(eighth_r_key_arr)
print("w[64], w[65], w[66], w[67] = ", w64, w65, w66, w67)
temp_array_9 = w67.copy()
arr_new = circular_byte_leftshift(w67)
print("circular byte left shift of w[67]:", arr_new)
sub_arr_new = byte_substitution(arr_new)
print("Byte Substitution (S-Box):", sub_arr_new)
gw67 = add_round_constant(8)
print("Adding round constant gives: g(w[67]) = ", gw67)

w68 = []
t1 = []
t2 = []
for u in w64:
    t1.append(int(u, 16))
for p in gw67:
    t2.append(int(p, 16))

for y in range(len(t1)):
    total = t1[y] ^ t2[y]
    w68.append(hex(total))

print("w[68] = ", w68)

w69 = []
t11 = []
t22 = []
for u in w65:
    t11.append(int(u, 16))
for p in w68:
    t22.append(int(p, 16))

for y in range(len(t1)):
    total = t11[y] ^ t22[y]
    w69.append(hex(total))

print("w[69] = ", w69)

w70 = []
t111 = []
t222 = []
for u in w66:
    t111.append(int(u, 16))
for p in w69:
    t222.append(int(p, 16))

for y in range(len(t1)):
    total = t111[y] ^ t222[y]
    w70.append(hex(total))

print("w[70] = ", w70)

w71 = []
t1111 = []
t2222 = []
for u in temp_array_9:
    t1111.append(int(u, 16))
for p in w70:
    t2222.append(int(p, 16))

for y in range(len(t1)):
    total = t1111[y] ^ t2222[y]
    w71.append(hex(total))

print("w[71] = ", w71)

ninth_r_key_arr = w68 + w69 + w70 + w71
print("Ninth round key = ", ninth_r_key_arr)
#decryption round key 9
row_11, row_22, row_33, row_44 = [0] * 4, [0] * 4, [0] * 4, [0] * 4
kkk, lll, mmm, nnn = 0, 1, 2, 3

for iii in range(4):
    row_11[iii] = ninth_r_key_arr[kkk]
    row_22[iii] = ninth_r_key_arr[lll]
    row_33[iii] = ninth_r_key_arr[mmm]
    row_44[iii] = ninth_r_key_arr[nnn]
    kkk += 4
    lll += 4
    mmm += 4
    nnn += 4
dec_rkey9 = [
    row_11,
    row_22,
    row_33,
    row_44
]

w72, w73, w74, w75 = split_array(ninth_r_key_arr)
print("w[72], w[73], w[74], w[75] = ", w72, w73, w74, w75)
temp_array_10 = w75.copy()
arr_new = circular_byte_leftshift(w75)
print("circular byte left shift of w[75]:", arr_new)
sub_arr_new = byte_substitution(arr_new)
print("Byte Substitution (S-Box):", sub_arr_new)
gw75 = add_round_constant(9)
print("Adding round constant gives: g(w[75]) = ", gw75)

w76 = []
t1 = []
t2 = []
for u in w72:
    t1.append(int(u, 16))
for p in gw75:
    t2.append(int(p, 16))

for y in range(len(t1)):
    total = t1[y] ^ t2[y]
    w76.append(hex(total))

print("w[76] = ", w76)

w77 = []
t11 = []
t22 = []
for u in w73:
    t11.append(int(u, 16))
for p in w76:
    t22.append(int(p, 16))

for y in range(len(t1)):
    total = t11[y] ^ t22[y]
    w77.append(hex(total))

print("w[77] = ", w77)

w78 = []
t111 = []
t222 = []
for u in w74:
    t111.append(int(u, 16))
for p in w77:
    t222.append(int(p, 16))

for y in range(len(t1)):
    total = t111[y] ^ t222[y]
    w78.append(hex(total))

print("w[78] = ", w78)

w79 = []
t1111 = []
t2222 = []
for u in temp_array_10:
    t1111.append(int(u, 16))
for p in w78:
    t2222.append(int(p, 16))

for y in range(len(t1)):
    total = t1111[y] ^ t2222[y]
    w79.append(hex(total))

print("w[79] = ", w79)

tenth_r_key_arr = w76 + w77 + w78 + w79
print("Tenth round key = ", tenth_r_key_arr)
#decryption round key 10
row_11, row_22, row_33, row_44 = [0] * 4, [0] * 4, [0] * 4, [0] * 4
kkk, lll, mmm, nnn = 0, 1, 2, 3

for iii in range(4):
    row_11[iii] = tenth_r_key_arr[kkk]
    row_22[iii] = tenth_r_key_arr[lll]
    row_33[iii] = tenth_r_key_arr[mmm]
    row_44[iii] = tenth_r_key_arr[nnn]
    kkk += 4
    lll += 4
    mmm += 4
    nnn += 4
dec_rkey10 = [
    row_11,
    row_22,
    row_33,
    row_44
]

print()
print("Round 0")
print()

row_1, row_2, row_3, row_4 = [0] * 4, [0] * 4, [0] * 4, [0] * 4
kk, ll, mm, nn = 0, 1, 2, 3

for ii in range(4):
    row_1[ii] = plaintext[kk]
    row_2[ii] = plaintext[ll]
    row_3[ii] = plaintext[mm]
    row_4[ii] = plaintext[nn]
    kk += 4
    ll += 4
    mm += 4
    nn += 4

state_matrix = [
    row_1,
    row_2,
    row_3,
    row_4
]
print("State Matrix = ", state_matrix)

row_11, row_22, row_33, row_44 = [0] * 4, [0] * 4, [0] * 4, [0] * 4
kkk, lll, mmm, nnn = 0, 1, 2, 3

for iii in range(4):
    row_11[iii] = key[kkk]
    row_22[iii] = key[lll]
    row_33[iii] = key[mmm]
    row_44[iii] = key[nnn]
    kkk += 4
    lll += 4
    mmm += 4
    nnn += 4

round_key0_matrix = [
    row_11,
    row_22,
    row_33,
    row_44
]
print("Round Key 0 Matrix = ", round_key0_matrix)


def XOR(arr1, arr2):
    row = []
    for t in range(4):
        e1 = int(arr1[t], 16)
        e2 = int(arr2[t], 16)
        addition = e1 ^ e2
        row.append(hex(addition))
    return row


new_state_matrix = [
    XOR(row_1, row_11),
    XOR(row_2, row_22),
    XOR(row_3, row_33),
    XOR(row_4, row_44)
]

print("New State Matrix in Round 0 = ", new_state_matrix)

print()
print("Round 1")
print()


def substitution_bytes(arr):
    r = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            r.append(s_box.get(arr[i][j]))
    row1, row2, row3, row4 = [], [], [], []
    u, a, e = 4, 8, 12
    for p in range(4):
        row1.append(r[p])
        row2.append(r[u])
        row3.append(r[a])
        row4.append(r[e])
        u += 1
        a += 1
        e += 1

    result_array = [
        row1,
        row2,
        row3,
        row4
    ]
    return result_array


r1_subst_bytes_array = substitution_bytes(new_state_matrix)
print("After substitution in Round 1 = ", r1_subst_bytes_array)


def shift_row(arr):
    temp1 = arr[1][0]
    arr[1][0] = arr[1][1]
    arr[1][1] = arr[1][2]
    arr[1][2] = arr[1][3]
    arr[1][3] = temp1

    temp20 = arr[2][0]
    temp21 = arr[2][1]
    arr[2][0] = arr[2][2]
    arr[2][1] = arr[2][3]
    arr[2][2] = temp20
    arr[2][3] = temp21

    temp30 = arr[3][0]
    temp31 = arr[3][1]
    temp32 = arr[3][2]
    arr[3][0] = arr[3][3]
    arr[3][1] = temp30
    arr[3][2] = temp31
    arr[3][3] = temp32
    return arr


new = shift_row(r1_subst_bytes_array)
print("Round 1 Shift Row = ", new)


def g_mul(g, h):
    if h == 1:
        return g
    tmp = (g << 1) & 0xff
    if h == 2:
        return tmp if g < 128 else tmp ^ 0x1b
    if h == 3:
        return g_mul(g, 2) ^ g


def mix_column(arr):
    r1 = []
    r2 = []
    r3 = []
    r4 = []
    fixed = [["0x2", "0x3", "0x1", "0x1"], ["0x1", "0x2", "0x3", "0x1"], ["0x1", "0x1", "0x2", "0x3"],
             ["0x3", "0x1", "0x1", "0x2"]]
    e1 = g_mul(int(arr[0][0], 16), int(fixed[0][0], 16))
    e2 = g_mul(int(arr[1][0], 16), int(fixed[0][1], 16))
    e3 = g_mul(int(arr[2][0], 16), int(fixed[0][2], 16))
    e4 = g_mul(int(arr[3][0], 16), int(fixed[0][3], 16))
    sum_r1 = e1 ^ e2 ^ e3 ^ e4
    r1.append(hex(sum_r1))

    e1 = g_mul(int(arr[0][1], 16), int(fixed[0][0], 16))
    e2 = g_mul(int(arr[1][1], 16), int(fixed[0][1], 16))
    e3 = g_mul(int(arr[2][1], 16), int(fixed[0][2], 16))
    e4 = g_mul(int(arr[3][1], 16), int(fixed[0][3], 16))
    sum_r2 = e1 ^ e2 ^ e3 ^ e4
    r1.append(hex(sum_r2))

    e1 = g_mul(int(arr[0][2], 16), int(fixed[0][0], 16))
    e2 = g_mul(int(arr[1][2], 16), int(fixed[0][1], 16))
    e3 = g_mul(int(arr[2][2], 16), int(fixed[0][2], 16))
    e4 = g_mul(int(arr[3][2], 16), int(fixed[0][3], 16))
    sum_r3 = e1 ^ e2 ^ e3 ^ e4
    r1.append(hex(sum_r3))

    e1 = g_mul(int(arr[0][3], 16), int(fixed[0][0], 16))
    e2 = g_mul(int(arr[1][3], 16), int(fixed[0][1], 16))
    e3 = g_mul(int(arr[2][3], 16), int(fixed[0][2], 16))
    e4 = g_mul(int(arr[3][3], 16), int(fixed[0][3], 16))
    sum_r4 = e1 ^ e2 ^ e3 ^ e4
    r1.append(hex(sum_r4))

    e1 = g_mul(int(arr[0][0], 16), int(fixed[1][0], 16))
    e2 = g_mul(int(arr[1][0], 16), int(fixed[1][1], 16))
    e3 = g_mul(int(arr[2][0], 16), int(fixed[1][2], 16))
    e4 = g_mul(int(arr[3][0], 16), int(fixed[1][3], 16))
    sum_r11 = e1 ^ e2 ^ e3 ^ e4
    r2.append(hex(sum_r11))

    e1 = g_mul(int(arr[0][1], 16), int(fixed[1][0], 16))
    e2 = g_mul(int(arr[1][1], 16), int(fixed[1][1], 16))
    e3 = g_mul(int(arr[2][1], 16), int(fixed[1][2], 16))
    e4 = g_mul(int(arr[3][1], 16), int(fixed[1][3], 16))
    sum_r22 = e1 ^ e2 ^ e3 ^ e4
    r2.append(hex(sum_r22))

    e1 = g_mul(int(arr[0][2], 16), int(fixed[1][0], 16))
    e2 = g_mul(int(arr[1][2], 16), int(fixed[1][1], 16))
    e3 = g_mul(int(arr[2][2], 16), int(fixed[1][2], 16))
    e4 = g_mul(int(arr[3][2], 16), int(fixed[1][3], 16))
    sum_r33 = e1 ^ e2 ^ e3 ^ e4
    r2.append(hex(sum_r33))

    e1 = g_mul(int(arr[0][3], 16), int(fixed[1][0], 16))
    e2 = g_mul(int(arr[1][3], 16), int(fixed[1][1], 16))
    e3 = g_mul(int(arr[2][3], 16), int(fixed[1][2], 16))
    e4 = g_mul(int(arr[3][3], 16), int(fixed[1][3], 16))
    sum_r44 = e1 ^ e2 ^ e3 ^ e4
    r2.append(hex(sum_r44))

    e1 = g_mul(int(arr[0][0], 16), int(fixed[2][0], 16))
    e2 = g_mul(int(arr[1][0], 16), int(fixed[2][1], 16))
    e3 = g_mul(int(arr[2][0], 16), int(fixed[2][2], 16))
    e4 = g_mul(int(arr[3][0], 16), int(fixed[2][3], 16))
    sum_r111 = e1 ^ e2 ^ e3 ^ e4
    r3.append(hex(sum_r111))

    e1 = g_mul(int(arr[0][1], 16), int(fixed[2][0], 16))
    e2 = g_mul(int(arr[1][1], 16), int(fixed[2][1], 16))
    e3 = g_mul(int(arr[2][1], 16), int(fixed[2][2], 16))
    e4 = g_mul(int(arr[3][1], 16), int(fixed[2][3], 16))
    sum_r222 = e1 ^ e2 ^ e3 ^ e4
    r3.append(hex(sum_r222))

    e1 = g_mul(int(arr[0][2], 16), int(fixed[2][0], 16))
    e2 = g_mul(int(arr[1][2], 16), int(fixed[2][1], 16))
    e3 = g_mul(int(arr[2][2], 16), int(fixed[2][2], 16))
    e4 = g_mul(int(arr[3][2], 16), int(fixed[2][3], 16))
    sum_r333 = e1 ^ e2 ^ e3 ^ e4
    r3.append(hex(sum_r333))

    e1 = g_mul(int(arr[0][3], 16), int(fixed[2][0], 16))
    e2 = g_mul(int(arr[1][3], 16), int(fixed[2][1], 16))
    e3 = g_mul(int(arr[2][3], 16), int(fixed[2][2], 16))
    e4 = g_mul(int(arr[3][3], 16), int(fixed[2][3], 16))
    sum_r444 = e1 ^ e2 ^ e3 ^ e4
    r3.append(hex(sum_r444))

    e1 = g_mul(int(arr[0][0], 16), int(fixed[3][0], 16))
    e2 = g_mul(int(arr[1][0], 16), int(fixed[3][1], 16))
    e3 = g_mul(int(arr[2][0], 16), int(fixed[3][2], 16))
    e4 = g_mul(int(arr[3][0], 16), int(fixed[3][3], 16))
    sum_r1111 = e1 ^ e2 ^ e3 ^ e4
    r4.append(hex(sum_r1111))

    e1 = g_mul(int(arr[0][1], 16), int(fixed[3][0], 16))
    e2 = g_mul(int(arr[1][1], 16), int(fixed[3][1], 16))
    e3 = g_mul(int(arr[2][1], 16), int(fixed[3][2], 16))
    e4 = g_mul(int(arr[3][1], 16), int(fixed[3][3], 16))
    sum_r2222 = e1 ^ e2 ^ e3 ^ e4
    r4.append(hex(sum_r2222))

    e1 = g_mul(int(arr[0][2], 16), int(fixed[3][0], 16))
    e2 = g_mul(int(arr[1][2], 16), int(fixed[3][1], 16))
    e3 = g_mul(int(arr[2][2], 16), int(fixed[3][2], 16))
    e4 = g_mul(int(arr[3][2], 16), int(fixed[3][3], 16))
    sum_r3333 = e1 ^ e2 ^ e3 ^ e4
    r4.append(hex(sum_r3333))

    e1 = g_mul(int(arr[0][3], 16), int(fixed[3][0], 16))
    e2 = g_mul(int(arr[1][3], 16), int(fixed[3][1], 16))
    e3 = g_mul(int(arr[2][3], 16), int(fixed[3][2], 16))
    e4 = g_mul(int(arr[3][3], 16), int(fixed[3][3], 16))
    sum_r4444 = e1 ^ e2 ^ e3 ^ e4
    r4.append(hex(sum_r4444))

    result_array = [
        r1,
        r2,
        r3,
        r4
    ]

    return result_array


after_mix_column = mix_column(new)
print("Round 1 Mix Column = ", after_mix_column)

row_11, row_22, row_33, row_44 = [0] * 4, [0] * 4, [0] * 4, [0] * 4
kkk, lll, mmm, nnn = 0, 1, 2, 3

for iii in range(4):
    row_11[iii] = first_r_key_arr[kkk]
    row_22[iii] = first_r_key_arr[lll]
    row_33[iii] = first_r_key_arr[mmm]
    row_44[iii] = first_r_key_arr[nnn]
    kkk += 4
    lll += 4
    mmm += 4
    nnn += 4

round_key1_matrix_before = [
    row_11,
    row_22,
    row_33,
    row_44
]

round_key1_matrix = [
    XOR(after_mix_column[0], row_11),
    XOR(after_mix_column[1], row_22),
    XOR(after_mix_column[2], row_33),
    XOR(after_mix_column[3], row_44)
]

print("AES Output after Round 1 = ", round_key1_matrix)

print()
print("Round 2")
print()

r2_subst_bytes_array = substitution_bytes(round_key1_matrix)
print("After substitution in Round 2 = ", r2_subst_bytes_array)

new_ar = shift_row(r2_subst_bytes_array)
print("Round 2 Shift Row = ", new_ar)

after_mix_column_ar = mix_column(new_ar)
print("Round 2 Mix Column = ", after_mix_column_ar)

row_11, row_22, row_33, row_44 = [0] * 4, [0] * 4, [0] * 4, [0] * 4
kkk, lll, mmm, nnn = 0, 1, 2, 3

for iii in range(4):
    row_11[iii] = second_r_key_arr[kkk]
    row_22[iii] = second_r_key_arr[lll]
    row_33[iii] = second_r_key_arr[mmm]
    row_44[iii] = second_r_key_arr[nnn]
    kkk += 4
    lll += 4
    mmm += 4
    nnn += 4

round_key2_matrix_before = [
    row_11,
    row_22,
    row_33,
    row_44
]

round_key2_matrix = [
    XOR(after_mix_column_ar[0], row_11),
    XOR(after_mix_column_ar[1], row_22),
    XOR(after_mix_column_ar[2], row_33),
    XOR(after_mix_column_ar[3], row_44)
]

print("AES Output after Round 2 = ", round_key2_matrix)

print()
print("Round 3")
print()

r3_subst_bytes_array = substitution_bytes(round_key2_matrix)
print("After substitution in Round 3 = ", r3_subst_bytes_array)

new_ar = shift_row(r3_subst_bytes_array)
print("Round 3 Shift Row = ", new_ar)

after_mix_column_ar = mix_column(new_ar)
print("Round 3 Mix Column = ", after_mix_column_ar)

row_11, row_22, row_33, row_44 = [0] * 4, [0] * 4, [0] * 4, [0] * 4
kkk, lll, mmm, nnn = 0, 1, 2, 3

for iii in range(4):
    row_11[iii] = third_r_key_arr[kkk]
    row_22[iii] = third_r_key_arr[lll]
    row_33[iii] = third_r_key_arr[mmm]
    row_44[iii] = third_r_key_arr[nnn]
    kkk += 4
    lll += 4
    mmm += 4
    nnn += 4

round_key3_matrix_before = [
    row_11,
    row_22,
    row_33,
    row_44
]

round_key3_matrix = [
    XOR(after_mix_column_ar[0], row_11),
    XOR(after_mix_column_ar[1], row_22),
    XOR(after_mix_column_ar[2], row_33),
    XOR(after_mix_column_ar[3], row_44)
]

print("AES Output after Round 3 = ", round_key3_matrix)

print()
print("Round 4")
print()

r4_subst_bytes_array = substitution_bytes(round_key3_matrix)
print("After substitution in Round 4 = ", r4_subst_bytes_array)

new_ar = shift_row(r4_subst_bytes_array)
print("Round 4 Shift Row = ", new_ar)

after_mix_column_ar = mix_column(new_ar)
print("Round 4 Mix Column = ", after_mix_column_ar)

row_11, row_22, row_33, row_44 = [0] * 4, [0] * 4, [0] * 4, [0] * 4
kkk, lll, mmm, nnn = 0, 1, 2, 3

for iii in range(4):
    row_11[iii] = fourth_r_key_arr[kkk]
    row_22[iii] = fourth_r_key_arr[lll]
    row_33[iii] = fourth_r_key_arr[mmm]
    row_44[iii] = fourth_r_key_arr[nnn]
    kkk += 4
    lll += 4
    mmm += 4
    nnn += 4

round_key4_matrix_before = [
    row_11,
    row_22,
    row_33,
    row_44
]

round_key4_matrix = [
    XOR(after_mix_column_ar[0], row_11),
    XOR(after_mix_column_ar[1], row_22),
    XOR(after_mix_column_ar[2], row_33),
    XOR(after_mix_column_ar[3], row_44)
]

print("AES Output after Round 4 = ", round_key4_matrix)

print()
print("Round 5")
print()

r5_subst_bytes_array = substitution_bytes(round_key4_matrix)
print("After substitution in Round 5 = ", r5_subst_bytes_array)

new_ar = shift_row(r5_subst_bytes_array)
print("Round 5 Shift Row = ", new_ar)

after_mix_column_ar = mix_column(new_ar)
print("Round 5 Mix Column = ", after_mix_column_ar)

row_11, row_22, row_33, row_44 = [0] * 4, [0] * 4, [0] * 4, [0] * 4
kkk, lll, mmm, nnn = 0, 1, 2, 3

for iii in range(4):
    row_11[iii] = fifth_r_key_arr[kkk]
    row_22[iii] = fifth_r_key_arr[lll]
    row_33[iii] = fifth_r_key_arr[mmm]
    row_44[iii] = fifth_r_key_arr[nnn]
    kkk += 4
    lll += 4
    mmm += 4
    nnn += 4

round_key5_matrix_before = [
    row_11,
    row_22,
    row_33,
    row_44
]

round_key5_matrix = [
    XOR(after_mix_column_ar[0], row_11),
    XOR(after_mix_column_ar[1], row_22),
    XOR(after_mix_column_ar[2], row_33),
    XOR(after_mix_column_ar[3], row_44)
]

print("AES Output after Round 5 = ", round_key5_matrix)

print()
print("Round 6")
print()

r6_subst_bytes_array = substitution_bytes(round_key5_matrix)
print("After substitution in Round 6 = ", r6_subst_bytes_array)

new_ar = shift_row(r6_subst_bytes_array)
print("Round 6 Shift Row = ", new_ar)

after_mix_column_ar = mix_column(new_ar)
print("Round 6 Mix Column = ", after_mix_column_ar)

row_11, row_22, row_33, row_44 = [0] * 4, [0] * 4, [0] * 4, [0] * 4
kkk, lll, mmm, nnn = 0, 1, 2, 3

for iii in range(4):
    row_11[iii] = sixth_r_key_arr[kkk]
    row_22[iii] = sixth_r_key_arr[lll]
    row_33[iii] = sixth_r_key_arr[mmm]
    row_44[iii] = sixth_r_key_arr[nnn]
    kkk += 4
    lll += 4
    mmm += 4
    nnn += 4

round_key6_matrix_before = [
    row_11,
    row_22,
    row_33,
    row_44
]

round_key6_matrix = [
    XOR(after_mix_column_ar[0], row_11),
    XOR(after_mix_column_ar[1], row_22),
    XOR(after_mix_column_ar[2], row_33),
    XOR(after_mix_column_ar[3], row_44)
]

print("AES Output after Round 6 = ", round_key6_matrix)

print()
print("Round 7")
print()

r7_subst_bytes_array = substitution_bytes(round_key6_matrix)
print("After substitution in Round 7 = ", r7_subst_bytes_array)

new_ar = shift_row(r7_subst_bytes_array)
print("Round 7 Shift Row = ", new_ar)

after_mix_column_ar = mix_column(new_ar)
print("Round 7 Mix Column = ", after_mix_column_ar)

row_11, row_22, row_33, row_44 = [0] * 4, [0] * 4, [0] * 4, [0] * 4
kkk, lll, mmm, nnn = 0, 1, 2, 3

for iii in range(4):
    row_11[iii] = seventh_r_key_arr[kkk]
    row_22[iii] = seventh_r_key_arr[lll]
    row_33[iii] = seventh_r_key_arr[mmm]
    row_44[iii] = seventh_r_key_arr[nnn]
    kkk += 4
    lll += 4
    mmm += 4
    nnn += 4

round_key7_matrix_before = [
    row_11,
    row_22,
    row_33,
    row_44
]

round_key7_matrix = [
    XOR(after_mix_column_ar[0], row_11),
    XOR(after_mix_column_ar[1], row_22),
    XOR(after_mix_column_ar[2], row_33),
    XOR(after_mix_column_ar[3], row_44)
]

print("AES Output after Round 7 = ", round_key7_matrix)

print()
print("Round 8")
print()

r8_subst_bytes_array = substitution_bytes(round_key7_matrix)
print("After substitution in Round 8 = ", r8_subst_bytes_array)

new_ar = shift_row(r8_subst_bytes_array)
print("Round 8 Shift Row = ", new_ar)

after_mix_column_ar = mix_column(new_ar)
print("Round 8 Mix Column = ", after_mix_column_ar)

row_11, row_22, row_33, row_44 = [0] * 4, [0] * 4, [0] * 4, [0] * 4
kkk, lll, mmm, nnn = 0, 1, 2, 3

for iii in range(4):
    row_11[iii] = eighth_r_key_arr[kkk]
    row_22[iii] = eighth_r_key_arr[lll]
    row_33[iii] = eighth_r_key_arr[mmm]
    row_44[iii] = eighth_r_key_arr[nnn]
    kkk += 4
    lll += 4
    mmm += 4
    nnn += 4

round_key8_matrix_before = [
    row_11,
    row_22,
    row_33,
    row_44
]

round_key8_matrix = [
    XOR(after_mix_column_ar[0], row_11),
    XOR(after_mix_column_ar[1], row_22),
    XOR(after_mix_column_ar[2], row_33),
    XOR(after_mix_column_ar[3], row_44)
]

print("AES Output after Round 8 = ", round_key8_matrix)

print()
print("Round 9")
print()

r9_subst_bytes_array = substitution_bytes(round_key8_matrix)
print("After substitution in Round 9 = ", r9_subst_bytes_array)

new_ar = shift_row(r9_subst_bytes_array)
print("Round 9 Shift Row = ", new_ar)

after_mix_column_ar = mix_column(new_ar)
print("Round 9 Mix Column = ", after_mix_column_ar)

row_11, row_22, row_33, row_44 = [0] * 4, [0] * 4, [0] * 4, [0] * 4
kkk, lll, mmm, nnn = 0, 1, 2, 3

for iii in range(4):
    row_11[iii] = ninth_r_key_arr[kkk]
    row_22[iii] = ninth_r_key_arr[lll]
    row_33[iii] = ninth_r_key_arr[mmm]
    row_44[iii] = ninth_r_key_arr[nnn]
    kkk += 4
    lll += 4
    mmm += 4
    nnn += 4

round_key9_matrix_before = [
    row_11,
    row_22,
    row_33,
    row_44
]

round_key9_matrix = [
    XOR(after_mix_column_ar[0], row_11),
    XOR(after_mix_column_ar[1], row_22),
    XOR(after_mix_column_ar[2], row_33),
    XOR(after_mix_column_ar[3], row_44)
]

print("AES Output after Round 9 = ", round_key9_matrix)

print()
print("Round 10")
print()

r10_subst_bytes_array = substitution_bytes(round_key9_matrix)
print("After substitution in Round 10 = ", r10_subst_bytes_array)

new_ar = shift_row(r10_subst_bytes_array)
print("Round 10 Shift Row = ", new_ar)

row_11, row_22, row_33, row_44 = [0] * 4, [0] * 4, [0] * 4, [0] * 4
kkk, lll, mmm, nnn = 0, 1, 2, 3

for iii in range(4):
    row_11[iii] = tenth_r_key_arr[kkk]
    row_22[iii] = tenth_r_key_arr[lll]
    row_33[iii] = tenth_r_key_arr[mmm]
    row_44[iii] = tenth_r_key_arr[nnn]
    kkk += 4
    lll += 4
    mmm += 4
    nnn += 4

round_key10_matrix_before = [
    row_11,
    row_22,
    row_33,
    row_44
]

round_key10_matrix = [
    XOR(new_ar[0], row_11),
    XOR(new_ar[1], row_22),
    XOR(new_ar[2], row_33),
    XOR(new_ar[3], row_44)
]

print("AES Output after Round 10 = ", round_key10_matrix)

ciphertext = []
for i in range(4):
    for j in range(4):
        ciphertext.append(round_key10_matrix[j][i])

print()
print("Ciphertext = ", ciphertext)

newCipher = []
for j in ciphertext:
    newCipher.append(j[2:])
print("New ciphertext = ", newCipher)





