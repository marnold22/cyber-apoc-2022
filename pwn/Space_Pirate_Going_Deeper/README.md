# Space_Pirate_Going_Deeper

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: YES
+ DOWNLOADABLE: YES

Description: We are inside D12! We bypassed the scanning system, and now we are right in front of the Admin Panel. The problem is that there are some safety mechanisms enabled so that not everyone can access the admin panel and become the user right below Draeger. Only a few of his intergalactic team members have access there, and they are the mutants that Draeger trusts. Can you disable the mechanisms and take control of the Admin Panel?

## NOTES

1. Running ghidra we see admin panel

    ```c
    void admin_panel(long param_1,long param_2,long param_3)

    {
    int iVar1;
    char local_38 [40];
    long local_10;
    
    local_10 = 0;
    printf("[*] Safety mechanisms are enabled!\n[*] Values are set to: a = [%x], b = [%ld], c = [%ld]. \n[*] If you want to continue, disable the mechanism or login as admin.\n"
            ,param_1,param_2,param_3);
    while (((local_10 != 1 && (local_10 != 2)) && (local_10 != 3))) {
        printf(&DAT_004014e8);
        local_10 = read_num();
    }
    if (local_10 == 1) {
        printf("\n[*] Input: ");
    }
    else {
        if (local_10 != 2) {
        puts("\n[!] Exiting..\n");
                        /* WARNING: Subroutine does not return */
        exit(0x1b39);
        }
        printf("\n[*] Username: ");
    }
    read(0,local_38,0x39);
    if (((param_1 != 0xdeadbeef) || (param_2 != 0x1337c0de)) || (param_3 != 0x1337beef)) {
        iVar1 = strncmp("DRAEGER15th30n34nd0nly4dm1n15tr4t0R0fth15sp4c3cr4ft",local_38,0x34);
        if (iVar1 != 0) {
        printf("\n%s[-] Authentication failed!\n",&DAT_00400c40);
        goto LAB_00400b38;
        }
    }
    printf("\n%s[+] Welcome admin! The secret message is: ",&DAT_00400c38);
    system("cat flag*");
    LAB_00400b38:
    puts("\n[!] For security reasons, you are logged out..\n");
    return;
    }
    ```
