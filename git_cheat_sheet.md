## Git Cheat Sheet

#### Single Git Commands
Initialize a git repo in the current directory

    # git init

Add a remote called "origin"

    # git remote add origin https://github.com/your-username-here/your-repo-here.git

Add all untracked changed files to staging, ready to be committed
    
    # git add -A

Commit with a message
    
    # git commit -m "some message here"

Push from local branch "master" up to remote branch "origin"
    
    # git push origin master

Pull from remote branch "origin" down to local branch "master"
    
    # git pull origin master

Force push "master" branch to remote "origin" forcing the remote to accept your changes 
    
    # git push --force origin master
    
Force pull and reset all files to match origin. (Won't mess with files in .gitignore)    
   
    # git fetch --all
    # git reset --hard origin/master    

Removes untracked files (not those ignored). Such as those .orig files that are left after resolving conflicts
    
    # git clean -f -n    // do this command first, with "n" flag to see what would be removed
    # git clean -f       // this command actually removes the files

View remotes

    # git remote -v

View current branch you are on

    # git branch -l

Switch to a branch

    # git checkout your-branch-here

Delete a branch
    
    # git checkout other_than_branch_to_be_deleted
    // Deleting local branch
    # git branch -D branch_to_be_deleted
    // Deleting remote branch
    # git push origin --delete branch_to_be_deleted

Rebase the current branch off of some other branch (most of the time "some-other-branch" will be "master")
   
    # git branch -l                  // shows you are currently on some-branch
    # git rebase some-other-branch   // now rebase off of some-other-branch

Create and push a tag up 

    # git tag
    # git tag -a v1.0.1 -m "something here about it"
    # git push origin v1.0.1

Delete a tag

    # git tag -d v1.0.1
    # git push origin :refs/tags/v1.0.1

#### Common Git Scenarios 

Push some code changes up to github repo

    # git init
    # git remote add origin https://github.com/your-username/your-repo.git
    # git add -A
    # git commit -m "updated my package"
    # git push --force origin master

Clone fork (a fork already on your github) & setup upstream (a remote to the very original you cloned from)

    $ git config --global user.name "Your Name"
    $ git config --global user.email "your@email.com"
    $ git clone https://github.com/your-username/your-forked-package.git
    $ cd your-forked-package
    $ git remote add upstream https://github.com/authors-username/original-official-package.git
    $ git remote -v
    $ git fetch upstream
    
"Interactive rebase", squash a branch, rebase, push to github

  - First let's create the branch
  
    ```
    $ git checkout -b my-branch
    $ git add -A
    $ git commit -m "added some new feature"
    $ git merge-base my-branch master
    ```
    
  - That command will return a commit hash. Use that commit hash in constructing this next command:
  
     ```
     $ git rebase --interactive ${HASH}
     ```
     
  - Note that you should replace ${HASH} with the actual commit hash from the previous command. For example, if your merge base is abc123, you would run $ git rebase --interactive abc123. Your text editor will open with a file that lists all the commits in your branch, and in front of each commit is the word "pick". It looks something like this:
  
     ```
     pick 1fc6c95 do something
     pick 6b2481b do something else
     pick dd1475d changed some things
     pick c619268 fixing typos
     ```
     
  - For every line except the first, you want to replace the word "pick" with the word "squash". It should end up looking like this:
  
     ```
     pick 1fc6c95 do something
     squash 6b2481b do something else
     squash dd1475d changed some things
     squash c619268 fixing typos
     ```
     
  - Save and close the file, and a moment later a new file should pop up in your editor, combining all the commit messages of all the commits. Reword this commit message as you want, and then save and close that file as well. This commit message will be the commit message for the one, big commit that you are squashing all of your larger commits into. Once you've saved and closed that file, your commits have been squashed together, and you're done with this step!
  
     ```
     $ git rebase upstream/master
     ``` 
     
Setup Git to use SSH key (perhaps for Bitbucket or Github)
    
    // Go to ssh directory (or create it if it doesn't exist)
    # cd ~/.ssh

    // Generate SSH key
    # ssh-keygen -t rsa -C "enter some random label here"
    
    // Prompt "Enter file in which to save the key (/root/.ssh/somekey):"
    [Enter your key name. In this case we call it "somekey"]
 
    // Prompt "Enter passphrase (empty for no passphrase):"
    [Enter a passphrase]

    // See your public ssh key
    # cat ~/.ssh/somekey.pub
 
    // somekey.pub is your public key
    // somekey is your private key
    
    // Enter this command to see if the agent is running
    # ps -e  | grep [s]sh-agent
    [9060 ??         0:00.28 /usr/bin/ssh-agent -l]

    // If the agent isn't running, start it manually with the following command:
    # ssh-agent /bin/bash
    
    // Load your new identity into the ssh-agent management program using the ssh-add command.
    # ssh-add ~/.ssh/somekey
    [Enter passphrase for /root/.ssh/id_rsa: 
    Identity added: /root/.ssh/somekey]

    // Use the ssh-add command to list the keys that the agent is managing.
    # ssh-add -l
    [2048 7a:9c:b2:9c:8e:4e:f4:af:de:70:77:b9:52:fd:44:97 /root/.ssh/somekey (RSA)]
    
