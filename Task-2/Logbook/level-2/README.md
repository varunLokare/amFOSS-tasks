### LEVEL 2 — THE TWO FACES OF WHISKEY PEAK

## Repository: Terminal-Voyage-User-Edition
## Target Path: ~/Terminal-Voyage-User-Edition/GrandLine/Whiskey_Peak/.baroque_works_cache/

## OBJECTIVE:

We need to find the hidden branch then investigate the hidden directory Whiskey Peak, then run the decriptive script with the flag obtained from the level-1 and then execute it to furthe progress in the task.

## My approach:

Now after the level-1 we gotta change the branch as the task requires to get into the other sub-branch , I used the command `git branch -a` to find the hidden branches then get into the sub-branch using `git checkout whiskey_peak_investigation` then get into the directory Whiskey peak then with the command `ls -a` find the hidden files in the directory. You would find a folder `.baroque_works_cache` and then get into that folder . After u get into the file go through the file and read the file `unlock.sh` ( u should have run the script and do it directly but I did it the hard way ._.), now go into unlock.sh using `nano` .
Get into the unlock.sh , there u would find an expected(Target) hash which should match to the decoded hash that you would get after running the command `INPUT_HASH=$(echo -n "$AWAKENING_SIGNATURE" | sha256sum | awk '{print $1}'` . Now put the obtained key in WAKENING_SIGNATURE position and run it in the terminal, you would expectedly get an hash which should match the hash that way given in the unlock.sh . After it satifies the condition do the further working given in the unlock.sh . Later  Decrypt the Level 2 flag using the student's input as the  password key so now run the command `REAL_FLAG=$(echo "$ENCRYPTED_FLAG" | openssl enc -aes-256-cbc -d -a -pbkdf2 -iter 100000 -pass pass:"$AWAKENING_SIGNATURE" 2>/dev/null)` but now replace the `ENCRYPTED_FLAG1` with the obtained hash and `AWAKENING_SIGNATURE` with the flag obtained in the level-1 and then run the commands and volaaaa you would get the flag for level-2.

## Flag Obtained :
BAROQUE_DIAL{SPLIT_TIMELINE_MISDIRECTION}
 

