#!/usr/bin/env python
# Cryptopals 1-2
# XOR two equal length hex buffers

from binascii import unhexlify, hexlify

s1 = '1c0111001f010100061a024b53535009181c'
s2 = '686974207468652062756c6c277320657965'

result=hexlify(''.join(chr(ord(c1) ^ ord(c2)) for c1, c2 in zip(unhexlify(s1), unhexlify(s2))))

expected = '746865206b696420646f6e277420706c6179'
print result
print expected

