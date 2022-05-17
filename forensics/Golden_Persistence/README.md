# Golden_Persistence

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: NO
+ DOWNLOADABLE: YES

Description: Emergency! A space station near Urkir was compromised. Although Urkir is considered to be the very embodiment of the neutral state, it is rich of fuel substances, something that Dreager is very much interested in. Thus, there are now fears that the intergalactic war will also affect this neutral planet. If Draeger and his mercenaries manage to maintain unauthorised access in Urkir's space station and escalate their privileges, they will soon be able to activate the station's defence mechanisms that are able to prevent any spaceship from entering Urkir's airspace. For now, the infected machine is isolated until the case is closed. Help Miyuki find their persistence mechanisms so they cannot gain access again.

## NOTES

1. > unzip forensics_golden_persistence.zip
2. > file NTUSER.DAT
    + `NTUSER.DAT: MS Windows registry file, NT/2000 or above`
    + This tells me that the .DAT file is probably a windows regestry which hints at a "dirty-hive" problem... maybe?
    + RESSEARCH: <https://cybermeisam.medium.com/blue-team-system-live-analysis-part-11-windows-user-account-forensics-ntuser-dat-495ab41393db>
3. strings NTUSER.DAT > ntuser.txt

## DIRTY HIVE

1. > hexedit NTUSER.DAT (Looking for first values to see if they are the same)
