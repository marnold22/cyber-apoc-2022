#!/usr/bin/env python3
from pwn import *
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
import hashlib

### -- CREDIT TO: willwam845 for writeup <https://willwam.me/posts/2022-05-19-htb-cyberapocalypse-2022> -- ###


# Modified code for personal learning
# Need to pass the program a "1" for the first request ie...

# Enter The Public Key of The Memory: 1

# Then this will build out the encypted text to paste into the second field
target_message = b"Initialization Sequence - Code 0"
key = hashlib.md5(long_to_bytes(1)).digest() # shared secret will always be 1
cipher = AES.new(key, AES.MODE_ECB)
message = cipher.encrypt(target_message)


# Enter The Encrypted Initialization Sequence:
print(message.hex())
