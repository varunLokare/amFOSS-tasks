# LEVEL 3 — THE WAX LABYRINTH OF LITTLE GARDEN

## Repository: Terminal-Voyage-User-Edition

## Target Path: ~/Terminal-Voyage-User-Edition/GrandLine/Wax_Jungle/

## Objective :

We need to find an hidden branch `little_garden` , get into that branch using `git checkout` and then and then locate a file amongst plenty of decory files. Find the file location, and then read it toe pass this level.

## My approach :

First using `git branch -a` find all the hidden branch present in the directory , later git into the branch `little_garden`. Get into the `Wax_Jungle` folder . Now after u are in the folder u gotta encode the flag `BAROQUE_DIAL{SPLIT_TIMELINE_MISDIRECTION}` from level-2 into to Base64 format to get the search string . After the string is obtained just search for the location of that specific string using `grep -r "QkFSTDFVRV9ESUFMe1NQTElUX1RJTUVMSU5FX01JU0RJUkVDVElPTn0K"`, after the location of string is found just read is usiing `cat` and u will get the clearance page of the level-3

## Fragment Obtained :

PONEGLYPH_FRAGMENT_1=KjY2MjF4bW01KzYqNyBsIS0vbTAtJIcnL  
