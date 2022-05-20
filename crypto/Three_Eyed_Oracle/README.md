# Three_Eyed_Oracle

## FLAG: HTB{345y_53cr37_r3c0v3ry}

## Status: Incomplete

+ DOCKER: YES
+ DOWNLOADABLE: YES

Description: Feeling very frustrated for getting excited about the AI and not thinking about the possibility of it malfunctioning, you blame the encryption of your brain. Feeling defeated and ashamed to have put Miyuki, who saved you, in danger, you slowly walk back to the lab. More determined than ever to find out what’s wrong with your brain, you start poking at one of its chips. This chip is linked to a decision-making algorithm based on human intuition. It seems to be encrypted… but some errors pop up when certain user data is entered. Is there a way to extract more information and fix the chip?

## NOTES

CREDIT TO: An00bRektn / 7h3 B14ck Kn1gh75 for the help <https://an00brektn.github.io/htb-cyber-apocalypse-crypto-three-eyed-oracle/>

Explanation: CREDIT An00bRektn
Suppose I could pad out my input to perfectly fill a certain amount of blocks, and I wanted to leak the stuff ahead (because that’s where the flag is). First, I’ll need to find the offset to be able to fill up a whole block with whatever I want:
XXXXXXBB AAAAAAAA AAAAAAAA

Once I do this, I know exactly what the block “AAAAAAAA” encrypts to. Recall the secret we want to leak is ahead of our input. So, by removing one “A” from my input, we see the following:

XXXXXXBB AAAAAAAH TB{win}X

At this point, I know that my encrypted block is the encryption of “AAAAAAA_” plus some unknown character, because I don’t know what the flag is. However, since this is ECB mode, I can just bruteforce a block for all ~90 characters that would show up in a flag by submitting them to the oracle, and comparing each against what I have here. Once I’ve determined that the last letter is H, I can pull back the curtain further to include the T. Since I then know what “AAAAAAAH” encrypts to, I can basically repeat the process until I leak the entire value.

1. > nc 165.227.224.55 32559
2. Took An00bRektn's python script and broke it down piece by piece manually sending information to the oracle each time - for learning purposes
3. RESPONSE: [+] HTB{345y_53cr37_r3c0v3ry}
