   # Git Exercises
IT ALL BEGINS WITH CLONING REPO
---

# 1. Master

The given first task was all about starting the tasks and initializing it.

## Commands Used

```bash
git start master
git verify
```

---

# 2. Commit One File

Now as per the task there are two files and we just need to commit one of the files.

Let the file be **A.file**.

## Commands Used

```bash
git add A.txt
```

> The command `git add A.txt` will look for a specific file named exactly `A.txt` in your current directory and stage it.

```bash
git commit -m "Commit A.txt file"
```

> This command is used to permanently save your changes to your project's local history.

---

# 3. Commit One File of Two Currently Staged

There are two files created in the root project directory, namely **A.txt** and **B.txt**, and both are added to the staging area. The goal is to commit only one file among them.

## Commands Used

```bash
git start commit-one-file-staged
```

```bash
git reset A.txt
```

> This command removes `A.txt` from the staging area without deleting your work or your actual file.

```bash
git commit -m "commit B.txt"
```

```bash
git verify
```
4.Ignore them 
Objective:
To ignore few files that are lowk useless and the files like generated files, compiled code, or libraries which are usually avoided by the developers.

commands used :
echo "*.exe" > .gitignore
echo "*.o" >> .gitignore
echo "*.jar" >> .gitignore
echo "libraries/" >> .gitignore

Here a file .gitignore and append the four rules line-by-line: *.exe *.o, *.jar, libraries/ in it 

git add .gitignore
It moves .gitignore from the working directory to the staging area. 
git commit -m "Add .gitignore rules"
Saves the staged .gitignore file as a permanent revision in your local Git repository with an attached descriptive information

git veryfy
To verify the exercise...

5.Chase branch
Objective :
Bring the missing work from the escaped branch to the main chase-branch so both branches are up to date and sharing the same progress.
commands used :
git merge escaped
Pulls all the information from the escape branch and drops it directly to the curruent working branch

git verify
To verify the exercise...

6.Merge Conflict
git reset --hard HEAD~2
Erases the last 2 git commits and then resets the work to get rid of the broked merge error 

echo "2+3=5" > equation.txt
Creates a file equation.txt with the correction of mathematically correct linw "2+3=5"
git add equation.txt
Movces equation.txt from working directory to the staging area 
git commit -m "Resolve merge conflict"
Changes get commited into your local git repo with and attacehed discriptive information

git verify
To verify the exercise...

7.Save your work
Objective :
Temporarily hide the incomplete and unfinshed work , jump in to an urgent commit fix then bring back the stashed work and then finish it 
commands used:

git stash
Takes the incomplete ,unfinished work and then stores it safely out of sight so that the work place stays completely clean 

nano bug.txt
It opends the fine bug.txt in the terminal editor to fix the text error 

git add bug.txt
git commit -m "Fix bug"
The file bug.txt moves from the working directory to the staging directory and then its commited to the local git repo

git stash pop
Retrieves the incomplete hidden file from the stash shelf and resotres it right where we left it 
echo "Finally, finished it!" >> bug.txt
Adding the text "Finally, finished it!" into bug.txt

git add .
stages all the file changes at once 
git commit -m "Finish work"
Saves the complete work as one single final commit

git verify
Vefiry the exercise ...

8.Change branch history 
Objective :
To move the current branch work above the hot-bugfix branch to adopt its bug fixes while keeping a clean amd linaewr history.

commands used:

git rebase hot-bugfix
It moves your branch's recent commits so they sit directly above the latest hot-bugfix updates, keeping the projeact and clean . 
git verify
Vefrify the exercise...

9.Remove Ignored 
Objective :
To tell git to stop tracking the files that are to be ignored while keepoing the l files safely on ur local device

commands used:
git rm --cached ignored.txt
Removes the file ignored.txt from the staging area but stores it intact into the device hardware

git commit -m "Stop tracking ignored.txt"
To commit changes into the actual working repo 
git verify
Verify the ecercise...

10.

