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
Saves the staged .gitignore file as a permanent revision in your local Git repository with an attached descriptive log mess

git veryfy
To verify the exercise.
