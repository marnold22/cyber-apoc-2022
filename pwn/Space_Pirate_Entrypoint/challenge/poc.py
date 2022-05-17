#!/usr/bin/env python3

from pwn import *

### - THIS IS A SECOND ATTEMPT AT ROP-V1 NOW USING SETBUF() - ###
### - FOR COMMENTS AND BREAKDOWN SEE V1 - ###

# This process is for the remote connection
p = remote("178.62.73.26", 32103)
res = p.sendline(b'0nlyTh30r1g1n4lCr3wM3mb3r5C4nP455')
print(res)