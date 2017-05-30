
#!/bin/bash
#Creator: Lyle Henkeman
# 05 May 2017
# From time to time we require new servers or simply do a clean install. Cloning repo's manually can be tedious and time consuming. Wouldn't it be nice to be able to clone them all to the newly installed host? Quite useful for quick migrations, so I wrote a quick bash script that achieves this.
# import multiple remote git repositories to local CODE dir

# settings / change this to your config
remoteHost=https://github.com/TAKEALOT
remoteUser=LyleH
remoteDir="~/tal-locust/"
remoteRepos=$(ssh -l $remoteUser $remoteHost "ls $remoteDir")
localCodeDir="${HOME}/workspace/"

# if no output from the remote ssh cmd, bail out
if [ -z "$remoteRepos" ]; then
    echo "No results from remote repo listing (via SSH)"
    exit
fi

# for each repo found remotely, check if it exists locally
# assumption: name repo = repo.git, to be saved to repo (w/o .git)
# if dir exists, skip, if not, clone the remote git repo into it
for gitRepo in $remoteRepos
do
  localRepoDir=$(echo ${localCodeDir}${gitRepo}|cut -d'.' -f1)
  if [ -d $localRepoDir ]; then 	
		echo -e "Directory $localRepoDir already exits, skipping ...\n"
	else
		cloneCmd="git clone ssh://$remoteUser@$remoteHost/$remoteDir"
		cloneCmd=$cloneCmd"$gitRepo $localRepoDir"
		
		cloneCmdRun=$($cloneCmd 2>&1)

		echo -e "Running: \n$ $cloneCmd"
		echo -e "${cloneCmdRun}\n\n"
	fi
done
