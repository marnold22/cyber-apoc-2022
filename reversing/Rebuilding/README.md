# Rebuilding

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: NO
+ DOWNLOADABLE: YES

Description: You arrive on a barren planet, searching for the hideout of a scientist involved in the Longhir resistance movement. You touch down at the mouth of a vast cavern, your sensors picking up strange noises far below. All around you, ancient machinery whirrs and spins as strange sigils appear and change on the walls. You can tell that this machine has been running since long before you arrived, and will continue long after you're gone. Can you hope to understand its workings?

## NOTES

1. unzip rev_building.zip
2. file rev_building
    `rebuilding: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=4097a7628977579d82b46c5cebc04ef3d6d045d2, not stripped`
3. Run the binary
    > ./rebuilding aaaa -> (aaaa is the temp password I am trying)
    > "Prepairing Secret Keys, Password Length Incorrect"
4. ran binary through ghidra for analysis

    ```c
    undefined8 main(int param_1,long param_2)

    {
    int __c;
    size_t sVar1;
    undefined8 uVar2;
    int local_14;
    int local_10;
    int local_c;
    
    if (param_1 != 2) {
        puts("Missing required argument");
                        /* WARNING: Subroutine does not return */
        exit(-1);
    }
    local_14 = 0;
    sVar1 = strlen(*(char **)(param_2 + 8));
    if (sVar1 == 0x20) {
        for (local_10 = 0; local_10 < 0x20; local_10 = local_10 + 1) {
        printf("\rCalculating");
        for (local_c = 0; local_c < 6; local_c = local_c + 1) {
            if (local_c == local_10 % 6) {
            __c = 0x2e;
            }
            else {
            __c = 0x20;
            }
            putchar(__c);
        }
        fflush(stdout);
        local_14 = local_14 +
                    (uint)((byte)(encrypted[local_10] ^ key[local_10 % 6]) ==
                        *(byte *)((long)local_10 + *(long *)(param_2 + 8)));
        usleep(200000);
        }
        puts("");
        if (local_14 == 0x20) {
        puts("The password is correct");
        uVar2 = 0;
        }
        else {
        puts("The password is incorrect");
        uVar2 = 0xffffffff;
        }
    }
    else {
        puts("Password length is incorrect");
        uVar2 = 0xffffffff;
    }
    return uVar2;
    }
    ```

    ```c
    void _INIT_1(void)

    {
    puts("Preparing secret keys");
    key[0] = 'a';
    key[1] = 'l';
    key[2] = 'i';
    key[3] = 'e';
    key[4] = 'n';
    key[5] = 's';
    return;
    }
    ```

5. So in this we first see that we need to get the correct password length to even access the "password checker"
6. running calc.py (for calulating the password length)
7. printing "A" *32 we get past the first check and now are onto: `Calculating... Incorrect Passsword`
8. The next part loops through 32 times
9. Local_c -> this loops 6 times and checks if the iteration of local_c = the iteration of local_10 mod 6
    If true -> the integer __C = 46
    If false -> the integer__C = 32
