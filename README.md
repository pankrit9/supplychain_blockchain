# Supply Chain Solution using Blockchain

## Notes:

- [IMPORTANT] All applications must be run in the root directory (i.e. NOT ./app/ or ./contracts).
For example, to run `land_gui.py`, the command would be `python3 app/land_gui.py`.
- Create a new branch, make commits and submit your merge requests (don't push
  directly to master!)
- Run `git pull` on the master branch before working, then `git checkout
  YOUR_BRANCH` and `git merge master` to always have a copy of the latest
  changes.


A typical first-time session with a new branch (e.g. `edit_readme_branch`) looks like:
```
$ git clone gitlab@gitlab.cse.unsw.EDU.AU:z5313514/comp6452_project_2.git
$ git checkout -b edit_readme_branch
### Create file(s), e.g. README.md and .gitignore ###
$ git add README.md .gitignore
$ git commit -m "Added typical session in README.md and imported .gitignore files for solidity"
$ git push -u origin edit_readme_branch 
### Follow the link outputted and submit the merge request using Gitlab web interface ###
```

Subsequent session on a branch that's already been created:
```
$ git checkout master
$ git pull
$ git checkout edit_readme_branch
$ git merge master
### Edit file(s), e.g. README.md and .gitignore ###
$ git add README.md .gitignore
$ git commit -m "Edited README.md and .gitignore"
$ git push
### Follow the link outputted and submit the merge request using Gitlab web interface ###
```
