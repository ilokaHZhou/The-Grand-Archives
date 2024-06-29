```git
git branch -m old_branch_name new_branch_name    # Rename branch locally    
git push origin :old_branch_name                 # Delete the old branch    
git push --set-upstream origin new_branch_name   # Push the new branch, set local branch to track the new remote
```