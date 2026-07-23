GIT EXERCISES 
1.Master :
the given first task was all about starting the tasks and initializing it 
commands used :
-git start master 
-git verify

2.Commit one file :
Now as per the task there are two files and we just need to commit one of the files 
let the file be A.file
commands used :
-git add A.txt
->The command git add .a will look for a specific file or folder named exactly A.file in your current directory and stage it
-git commit -m "Commit A.txt file"
-> This command is used to permenently save your changes to your projext's local history

3.Commit one file of two currently staged
There are two files crated  in root project directory namingly A.txt and B.txt and both are added to the staging area and the goal is to commit only one file among them
commands used :
git start commit-one-file-staged
git reset A.txt
this command removes A.txt from the staging area  without deleting your work or w3your actual file
git commit -m "commit B.txt"
git verify
