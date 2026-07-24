# Git Exercises

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
