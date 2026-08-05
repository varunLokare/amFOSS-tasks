# Git Exercises

## 1. Master

### Commands Used

```bash
git start master
git verify
```
THIS IS WHERE THE TASK BEGINS 
---

## 2. Commit One File

In this task, there are two files, but only one file needs to be committed.

Let the file be **A.txt**.

### Commands Used

```bash
git add A.txt
```

> Moves the  file `A.txt` from the working directory to the staging area.

```bash
git commit -m "Commit A.txt file"
```

> Saves all the committed changes locally with a descriptive message .

---

## 3. Commit One File of Two Currently Staged

Here both  files **A.txt** and **B.txt** are staged. Our objective here is to commit only **B.txt**.

### Commands Used

```bash
git start commit-one-file-staged
```

```bash
git reset A.txt
```

> Removes `A.txt` from the staging area while keeping the file unchanged.

```bash
git commit -m "Commit B.txt"
```

> Commits only `B.txt`.

```bash
git verify
```

> Verifies the exercise.

---

## 4. Ignore Them

### Objective

Here out objective is to ignore files and folders that should not be tracked by Git, such as compiled files, and libraries.

### Commands Used

```bash
echo "*.exe" > .gitignore
echo "*.o" >> .gitignore
echo "*.jar" >> .gitignore
echo "libraries/" >> .gitignore
```

> A file `.gitignore` is been created and then add rules to ignore `.exe`, `.o`, `.jar` files and the `libraries/` directory so that these files of such format be ignored .

```bash
git add .gitignore
```

> Takes the `.gitignore` file from working directory to staging area.

```bash
git commit -m "Add .gitignore rules"
```

> Saves the ignore rules in the repository by committing the changes.

```bash
git verify
```

> Verifies the exercise.

---

## 5. Chase Branch

### Objective

Bring the missing work from the `escaped` branch into the current branch.

### Commands Used

```bash
git merge escaped
```

> Merges the changes from the `escaped` branch into the current branch.

```bash
git verify
```

> Verifies the exercise.

---

## 6. Merge Conflict

### Objective

Resolve the merge conflict and commit the corrected version.

### Commands Used

```bash
git reset --hard HEAD~2
```

> Removes the last two commits and the drags the branch to the revious state.

```bash
echo "2+3=5" > equation.txt
```

>This command  Replaces the contents of `equation.txt` with the correct equation.

```bash
git add equation.txt
git commit -m "Resolve merge conflict"
```

> Commits the resolved changes with a discriptive message.

```bash
git verify
```

> Verifies the exercise.

---

## 7. Save Your Work

### Objective

To Temporarily save unfinished work, fix an urgent bug,restore the unfinished work and complete it.

### Commands Used

```bash
git stash
```

> Temporarily stores all uncommitted changes.

```bash
nano bug.txt
```

> Opens `bug.txt` to fix the bug.

```bash
git add bug.txt
git commit -m "Fix bug"
```

> Stages and commits the bug fix.

```bash
git stash pop
```

> Restores the previously stashed work.

```bash
echo "Finally, finished it!" >> bug.txt
```

> Adds the final line to complete the file.

```bash
git add .
git commit -m "Finish work"
```

> Stages all remaining changes and commits the completed work.

```bash
git verify
```

> Verifies the exercise.

---

## 8. Change Branch History

### Objective

Move the current branch commits on top of the `hot-bugfix` branch while maintaining a clean, linear history.

### Commands Used

```bash
git rebase hot-bugfix
```

> Replays the current branch commits on top of `hot-bugfix`branch .

```bash
git verify
```

> Verifies the exercise.

---

## 9. Remove Ignored

### Objective

Stop unwanted tracking of a file while keeping the file on the local machine.

### Commands Used

```bash
git rm --cached ignored.txt
```

> Removes `ignored.txt` from Git tracking without any deleting the local file.

```bash
git commit -m "Stop tracking ignored.txt"
```

> Saves the change in the Git history.

```bash
git verify
```

> Verifies the exercise.

---

## 10. Case-Sensitive Filename

### Objective

Renaming the name of the file if there is an error in case of the spelling or cases.

### Commands Used

```bash
git mv File.txt file.txt
```

> Renames the file and stages the changes automatically.

```bash
git commit -m "Rename File.txt to file.txt"
```

> Commit the changes made in the file name with a commit message .

```bash
git verify
```

> Verifies the exercise.

---

## 11. Fix Typo

### Objective

Update the previous commit by adding the missed changes without creating a new commit.

### Commands Used

```bash
nano file.txt
```

> Opens `file.txt` to correct the typo.

```bash
git add file.txt
```

> Staging the corret file to the staging area .

```bash
git commit --amend -m "Add Hello world"
```

> Replaces the previous commit with the updated changes and commit message.

```bash
git verify
```

> Verifies the exercise.


## 12.Forge-data

### Objective 
To forge the commit date.

### Commands Used

```bash
git commit --amend --date="1987-01-01" --no-edit
```
>Replaces the last commit , keeping the same commit message, but changes the author date to `1987-01-01`.

```bash
git verify
```

> Verifies the exercise.

## 13. Fix Old Typo

### Objective
Correcting the typo in the previous commit without creating a new commit and preserveing the clean history while resolving any merge conflicts.

### Commands Used 
```bash
git rebase -i HEAD~2
```

>It enables us to edti , modity and delecte the last two commits rewriting the commit history.

```bash
nano file.txt
```
> Opens the file `file.txt` to fix the typo.

```bash
git add file.txt
git commit --amend
git rebase --continue
```

>Stages the fix to the staging area , amends the target commit and then continues the rebase proceass.

