# Android_in_the_middle

## FLAG: HTB{7h15_p2070c0l_15_pr0tec73d_8y_D@nb3er_c0pyr1gh7_1aws}

## Status: Complete dwith afterparty

+ DOCKER: YES
+ DOWNLOADABLE: YES

Description: Years have passed since Miyuki rescued you from the graveyard. When Virgil tells you that he needs your help with something he found there, desperate thoughts about your father and the disabilities you developed due to the disposal process come to mind. The device looks like an advanced GPS with AI capabilities. Riddled with questions about the past, you are pessimistic that you could be of any value. After hours of fiddling and observing the power traces of this strange device, you and Virgil manage to connect to the debugging interface and write an interpreter to control the signals. The protocol looks familiar to you. Your father always talked about implementing this scheme in devices for security reasons. Could it have been him?

## NOTES

1. CREDIT TO: willwam845 for the help
2. > nc 46.101.30.188 31958
3. RESPONSE

    ```text
    DEBUG MSG - Generating The Global DH Parameters
    DEBUG MSG - g = 2, p = 10177459997049772558637057109490700048394574760284564283959324525695097805837401714582821820424475480057537817583807249627119267268524840254542683041588432363128111683358536204391767254517057859973149680238170237977230020947732558089671785239121778309357814575486749623687357688511361367822815452806637006568922401890961240475060822815400430220536180181951862931844638638933951683988349468373510128406899660648258602475728913837826845743111489145006566908004165703542907243208106044538037004824530893555918497937074663828069774495573109072469750423175863678445547058247156187317168731446722852098571735569138516533993
    DEBUG MSG - Calculation Complete

    DEBUG MSG - Generating The Public Key of CPU...
    DEBUG MSG - Calculation Complete
    DEBUG MSG - Public Key is: ???

    Enter The Public Key of The Memory:
    ```

4. > for the public key enter: 1
5. RESPONSE

    ```text
    DEBUG MSG - The CPU Calculates The Shared Secret
    DEBUG MSG - Calculation Complete

    Enter The Encrypted Initialization Sequence:
    ```

6. run apsolve.py to generate the message.hex() that will then be pasted into the Initialization Sequence
7. > 7fd4794e77290bf65808e95467f284966d71995c16e83da2192aecfd2d0df7a4
8. RESPONSE: `DEBUG MSG - HTB{7h15_p2070c0l_15_pr0tec73d_8y_D@nb3er_c0pyr1gh7_1aws}`
