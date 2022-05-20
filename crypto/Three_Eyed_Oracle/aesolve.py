#!/usr/bin/env python3
# Reference: An00bRektn / 7h3 B14ck Kn1gh75
from pwn import *


##### MODIFIED FROM ORIGINAL FOR PERSONAL LEARNING #####

flag = ""
padding = 'B' * 4 +'A' * (31-len(flag))
ct = padding + flag + chr(33) # chr(33) => '!'
ct_H = padding + flag + chr(72) # chr(72) => 'H'

print(padding.encode('latin-1').hex()) # paste this value into oracle
print(ct.encode('latin-1').hex())      # paste this value into oracle
print(ct_H.encode('latin-1').hex())    # paste this value into oracle

pad_ret = "7d58e01f04b1ffec02eaa8042e401932fe02b45b10f8561cff12ca20cdee633656f20e09170d03628d66f42b145b1b34556629f1c174a2dc9dce0fd429f4ebdb5356d76543e47682746cf4b0acdc269c"
ct_ret = "7d58e01f04b1ffec02eaa8042e401932fe02b45b10f8561cff12ca20cdee6336976a2af256c8c909222dd8b248c5a09e9491baf0181a5d862785b5190d827938a7b53b85c83faaaa820f4f2e0c77fb0e"
ct_H_ret = "7d58e01f04b1ffec02eaa8042e401932fe02b45b10f8561cff12ca20cdee633656f20e09170d03628d66f42b145b1b349491baf0181a5d862785b5190d827938a7b53b85c83faaaa820f4f2e0c77fb0e"

# In this, the first return (padding return) should equal the third return ("H" return) 
# Since "H" would be the first expected value of the flag
print(pad_ret[64:96])
print(ct_ret[64:96])
print(ct_H_ret[64:96])

# Now repeat this process for every character + num + symbols (ASCII) to find the flag




##### ORIGINAL SCRIPT #####
# r = remote('165.227.224.55', 32559)

# def oracle(plaintext: str):
#     r.sendlineafter(">", plaintext.encode('latin-1').hex())
#     return r.recvlineS().strip()

# flag = ""
# p = log.progress(f'working...')
# while True: 
#     padding = 'B' * 4 +'A' * (31-len(flag))
#     ref = oracle(padding)
#     for c in range(33, 126):
#         ct = oracle(padding+flag+chr(c))
#         p.status(f"\n  ct: {ct[64:96]}\n ref: {ref[64:96]}\nflag: {flag}\n pad: {padding+flag+chr(c)}")
#         if ct[64:96] == ref[64:96]:
#             flag += chr(c)
#             break
#     if '}' in flag:
#         break

# success(flag)