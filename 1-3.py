#!/usr/bin/env python
# Cryptopals 1-3
# Single-byte XOR cipher
# Find the key to decrypt a message from a hex encoded string

import binascii

string1 = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

#unhexlify the string
bytes = binascii.unhexlify(string1)

#Write a loop that XORs string against key(256)

possibilities = (''.join(chr(ord(byte) ^ key) for byte in bytes) for key in range(256))

# print the possible string with the most spaces.

print max(possibilities, key=lambda s: s.count(' ')) 




