#!/usr/bin/env python
# Cryptopals 1-1
# Convert a hex string into base64
# Rule: Operate on raw bytes not encoded string

import base64
from binascii import unhexlify

def hex_to_b64(s):
	bytes = unhexlify(s)
	return base64.b64encode(bytes)

if __name__ == '__main__':
	hex_str = \
		'49276d206b696c6c696e6720796f757220627261696e206c696b6520612' \
		'0706f69736f6e6f7573206d757368726f6f6d'
	print hex_to_b64(hex_str)
	print("SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")

