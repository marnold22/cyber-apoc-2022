# Compressor

## FLAG: HTB{GTFO_4nd_m4k3_th3_b35t_4rt1f4ct5}

## Status: Complete

+ DOCKER: NO
+ DOWNLOADABLE: YES

Description: Ramona's obsession with modifications and the addition of artifacts to her body has slowed her down and made her fail and almost get killed in many missions. For this reason, she decided to hack a tiny robot under Golden Fang's ownership called 'Compressor', which can reduce and increase the volume of any object to minimize/maximize it according to the needs of the mission. With this item, she will be able to carry any spare part she needs without adding extra weight to her back, making her fast. Can you help her take it and hack it?

## NOTES

1. > nc 159.65.89.199 30837
2. Offers prompt with several options

    ```text
    Component-List:
    ---------------
    1. Head
    2. Torso
    3. Hands
    4. Legs
    ---------------
    [*] Choose component: 
    ```

3. Select any option for example 1
4. New prompt is offered

    ```text
    ---------------
    Actions:
    1. Create artifact
    2. List directory    (pwd; ls -la)
    3. Read artifact     (cat ./<name>)
    4. Compress artifact (zip <name>.zip <name> <options>)
    5. Change directory  (cd <dirname>)
    6. Clean directory   (rm -rf *)
    7. Exit
    ---------------

    [*] Choose action: 2
    /home/ctf/SmsqU71Ui0jqifazWpwKEh93sGHy8tm3/Head
    ```

5. Knowiung that the path is `/home/ctf/SmsqU71Ui0jqifazWpwKEh93sGHy8tm3/Head`
6. Using the cat function, I try and cat out a flag IFF there is a flag at the `/home/ctf/` folder level

    ```text
    [*] Choose action: 3

    Insert name you want to read: ../../flag
    cat: can't open './../../flag': No such file or directory

    [*] Choose action: 3

    Insert name you want to read: ../../flag.txt
    HTB{GTFO_4nd_m4k3_th3_b35t_4rt1f4ct5}
    ```

7. Attemped to see if there was a flag, but needed the .txt file extension
