## LEVEL 4 — THE CAMOUFLAGED BLUEPRINTS OF WATER 7

# Repository: Terminal-Voyage-User-Edition

# Target Path: ~/Terminal-Voyage-User-Edition/GrandLine/Water_7/galley_la_company/

# Objective :

The objective of the perticular task is to decript the corrupted blueprint file present in the `galley_la_company` directory . We need to identify the true identity of the true file rather then being dependent on the files extension . We need to rip away the curropted file to get the next key fragment.

# My Approach :

First get into the main branch `canonical-timeline` using " git branch " and " git checkout " after getting into the branch, march forward to `Water_7` and then to `galley_la_company`  now in there u would find a file. 
Now run the command `file puffing_tom_blueprints` to find out the format of the file and to chech the missing extension to the file , after u figure it out change the name of the file using the command `mv puffing_tom_blueprints puffing_tom_blueprints.gz` to make it to its correct extension file . Now that the file is brought to its original extension use `gunzip puffing_tom_blueprints.gz` to decompress it . Now lets get into the second layer of extraction , run the same "file " command on the folder to inspect the decompressed file(`tar` extension btw), later run the commands `tar -tf puffing_tom_blueprints` ( to list the contents present in the corrept file ) and `tar -xf puffing_tom_blueprints` (Extract the listed file ) after running the commands you will end up with a `file step1_blueprints.zip` , now unzip it later go into the file obtained ater the unzipping and there u would find a txt file `secret_link.txt`, read it and you will obtain the flag for this task .

# Fragment Obtained :

PONEGLYPH_FRAGMENT_II = "SwnbzptDiM3JSpvFiMuJ2BPjzAlJ28ViZA="   

