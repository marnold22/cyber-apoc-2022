# WIDE

## FLAG: HTB{str1ngs_4r3nt_4lw4ys_4sc11}

## Status: Complete

+ DOCKER: NO
+ DOWNLOADABLE: YES

Description: We've received reports that Draeger has stashed a huge arsenal in the pocket dimension Flaggle Alpha. You've managed to smuggle a discarded access terminal to the Widely Inflated Dimension Editor from his headquarters, but the entry for the dimension has been encrypted. Can you make it inside and take control?

## NOTES

1. > file db.ex
    + `db.ex: Matlab v4 mat-file (little endian) , numeric, rows 1835627088, columns 29557`

2. > strings db.ex

    ```text
    Primus
    people breathe variety practice
    Our home dimension
    Cheagaz
    scene control river importance
    The Ice Dimension
    Byenoovia
    fighting cast it parallel
    The Berserk Dimension
    Cloteprea
    facing motor unusual heavy
    The Hungry Dimension
    Maraqa
    stomach motion sale valuable
    The Water Dimension
    Aidor
    feathers stream sides gate
    The Bone Dimension
    Flaggle Alpha
    admin secret power hidden
    HOt*
    ```

3. > ghidra wide -> (main funtion)

    ```c
    undefined8 main(int param_1,undefined8 *param_2)

    {
    int iVar1;
    FILE *__stream;
    ulong uVar2;
    void *__ptr;
    uint uVar3;
    int local_28;
    
    if (param_1 < 2) {
        printf("Usage: %s db.ex\n",*param_2);
                        /* WARNING: Subroutine does not return */
        exit(-1);
    }
    puts("[*] Welcome user: kr4eq4L2$12xb, to the Widely Inflated Dimension Editor [*]");
    puts("[*]    Serving your pocket dimension storage needs since 14,012.5 B      [*]");
    __stream = fopen((char *)param_2[1],"r");
    if (__stream == (FILE *)0x0) {
        puts("[x] There was a problem accessing your database [x]");
                        /* WARNING: Subroutine does not return */
        exit(-1);
    }
    fseek(__stream,0,2);
    uVar2 = ftell(__stream);
    fseek(__stream,0,0);
    uVar2 = (uVar2 - uVar2 % 0xb4) / 0xb4;
    iVar1 = (int)uVar2;
    __ptr = calloc((long)iVar1,0xb4);
    fread(__ptr,0xb4,(long)iVar1,__stream);
    fclose(__stream);
    puts("[*]                       Displaying Dimensions....                      [*]");
    puts("[*]       Name       |              Code                |   Encrypted    [*]");
    for (local_28 = 0; local_28 < iVar1; local_28 = local_28 + 1) {
        if (*(int *)((long)__ptr + (long)local_28 * 0xb4) == 0) {
        uVar3 = 0x20;
        }
        else {
        uVar3 = 0x2a;
        }
        printf("[X] %-16s | %-32s | %6s%c%7s [*]\n",(long)__ptr + (long)local_28 * 0xb4 + 4,
            (long)__ptr + (long)local_28 * 0xb4 + 0x14,&DAT_0010132d,(ulong)uVar3,&DAT_0010132d);
    }
    menu(__ptr,uVar2 & 0xffffffff);
    return 0;
    }
    ```

    In here we see that this just prints out table, then runs menu()

4. > ghidra wide -> (menu function)

    ```c

    /* WARNING: Could not reconcile some variable overlaps */

    void menu(long param_1,int param_2)

    {
    int iVar1;
    long lVar2;
    undefined8 *puVar3;
    long in_FS_OFFSET;
    uint local_1d4;
    wchar_t local_1c8 [16];
    undefined8 local_188;
    undefined8 local_180;
    undefined8 local_178;
    undefined8 local_170;
    undefined8 local_168;
    undefined8 local_160;
    undefined4 local_158;
    undefined4 uStack340;
    undefined4 local_150;
    undefined4 uStack332;
    undefined4 local_148;
    undefined4 uStack324;
    undefined4 local_140;
    undefined4 uStack316;
    undefined4 local_138;
    undefined4 uStack308;
    undefined4 local_130;
    undefined4 uStack300;
    undefined4 local_128;
    undefined4 uStack292;
    undefined4 local_120;
    undefined4 uStack284;
    undefined4 local_118;
    undefined4 uStack276;
    undefined4 local_110;
    undefined4 uStack268;
    undefined4 local_108;
    undefined4 uStack260;
    undefined4 local_100;
    undefined4 uStack252;
    undefined4 local_f8;
    undefined4 uStack244;
    undefined4 local_f0;
    undefined4 uStack236;
    undefined4 local_e8;
    undefined4 uStack228;
    undefined4 local_e0;
    undefined4 uStack220;
    undefined4 local_d8;
    char local_c8 [16];
    undefined8 local_b8;
    undefined8 local_b0;
    undefined8 local_a8;
    undefined8 local_a0;
    undefined8 local_98;
    undefined8 local_90;
    undefined8 local_88;
    undefined8 local_80;
    undefined8 local_78;
    undefined8 local_70;
    undefined8 local_68;
    undefined8 local_60;
    undefined8 local_58;
    undefined8 local_50;
    undefined8 local_48;
    undefined8 local_40;
    undefined8 local_38;
    undefined8 local_30;
    undefined8 local_28;
    undefined8 local_20;
    undefined8 local_10;
    
    local_10 = *(undefined8 *)(in_FS_OFFSET + 0x28);
    local_b8 = 0;
    local_b0 = 0;
    local_a8 = 0;
    local_a0 = 0;
    do {
        while( true ) {
        while( true ) {
            printf("Which dimension would you like to examine? ");
            fgets((char *)&local_b8,0x20,stdin);
            lVar2 = strtol((char *)&local_b8,(char **)0x0,10);
            iVar1 = (int)lVar2;
            if ((-1 < iVar1) && (iVar1 < param_2)) break;
            puts("That option was invalid.");
        }
        puVar3 = (undefined8 *)(param_1 + (long)iVar1 * 0xb4);
        local_188 = *puVar3;
        local_180 = puVar3[1];
        local_178 = puVar3[2];
        local_170 = puVar3[3];
        local_168 = puVar3[4];
        local_160 = puVar3[5];
        local_158 = (undefined4)puVar3[6];
        uStack340 = (undefined4)((ulong)puVar3[6] >> 0x20);
        local_150 = (undefined4)puVar3[7];
        uStack332 = (undefined4)((ulong)puVar3[7] >> 0x20);
        local_148 = (undefined4)puVar3[8];
        uStack324 = (undefined4)((ulong)puVar3[8] >> 0x20);
        local_140 = (undefined4)puVar3[9];
        uStack316 = (undefined4)((ulong)puVar3[9] >> 0x20);
        local_138 = (undefined4)puVar3[10];
        uStack308 = (undefined4)((ulong)puVar3[10] >> 0x20);
        local_130 = (undefined4)puVar3[0xb];
        uStack300 = (undefined4)((ulong)puVar3[0xb] >> 0x20);
        local_128 = (undefined4)puVar3[0xc];
        uStack292 = (undefined4)((ulong)puVar3[0xc] >> 0x20);
        local_120 = (undefined4)puVar3[0xd];
        uStack284 = (undefined4)((ulong)puVar3[0xd] >> 0x20);
        local_118 = (undefined4)puVar3[0xe];
        uStack276 = (undefined4)((ulong)puVar3[0xe] >> 0x20);
        local_110 = (undefined4)puVar3[0xf];
        uStack268 = (undefined4)((ulong)puVar3[0xf] >> 0x20);
        local_108 = (undefined4)puVar3[0x10];
        uStack260 = (undefined4)((ulong)puVar3[0x10] >> 0x20);
        local_100 = (undefined4)puVar3[0x11];
        uStack252 = (undefined4)((ulong)puVar3[0x11] >> 0x20);
        local_f8 = (undefined4)puVar3[0x12];
        uStack244 = (undefined4)((ulong)puVar3[0x12] >> 0x20);
        local_f0 = (undefined4)puVar3[0x13];
        uStack236 = (undefined4)((ulong)puVar3[0x13] >> 0x20);
        local_e8 = (undefined4)puVar3[0x14];
        uStack228 = (undefined4)((ulong)puVar3[0x14] >> 0x20);
        local_e0 = (undefined4)puVar3[0x15];
        uStack220 = (undefined4)((ulong)puVar3[0x15] >> 0x20);
        local_d8 = *(undefined4 *)(puVar3 + 0x16);
        if ((int)local_188 != 0) break;
        puts((char *)&uStack340);
        }
        local_98 = CONCAT44(local_150,uStack340);
        local_90 = CONCAT44(local_148,uStack332);
        local_88 = CONCAT44(local_140,uStack324);
        local_80 = CONCAT44(local_138,uStack316);
        local_78 = CONCAT44(local_130,uStack308);
        local_70 = CONCAT44(local_128,uStack300);
        local_68 = CONCAT44(local_120,uStack292);
        local_60 = CONCAT44(local_118,uStack284);
        local_58 = CONCAT44(local_110,uStack276);
        local_50 = CONCAT44(local_108,uStack268);
        local_48 = CONCAT44(local_100,uStack260);
        local_40 = CONCAT44(local_f8,uStack252);
        local_38 = CONCAT44(local_f0,uStack244);
        local_30 = CONCAT44(local_e8,uStack236);
        local_28 = CONCAT44(local_e0,uStack228);
        local_20 = CONCAT44(local_d8,uStack220);
        printf("[X] That entry is encrypted - please enter your WIDE decryption key: ");
        fgets(local_c8,0x10,stdin);
        mbstowcs(local_1c8,local_c8,0x10);
        iVar1 = wcscmp(local_1c8,L"sup3rs3cr3tw1d3");
        if (iVar1 == 0) {
        for (local_1d4 = 0;
            (local_1d4 < 0x80 && (*(char *)((long)&local_98 + (long)(int)local_1d4) != '\0'));
            local_1d4 = local_1d4 + 1) {
            *(byte *)((long)&local_98 + (long)(int)local_1d4) =
                *(byte *)((long)&local_98 + (long)(int)local_1d4) ^
                (char)(local_1d4 * 0x1b) + (char)((int)(local_1d4 * 0x1b) / 0xff);
        }
        puts((char *)&local_98);
        }
        else {
        puts("[X]                          Key was incorrect                           [X]");
        }
    } while( true );
    }
    ```

    In here we see the wcscmp() using the key of `sup3rs3cr3tw1d3`

5. > ./wide db.ex (run the program)
    1. + Which dimension would you like to examine?
    2. > 6
    3. + That entry is encrypted please enter your WIDE decryption key
    4. > sup3rs3cr3tw1d3
    5. + HTB{str1ngs_4r3nt_4lw4ys_4sc11}
