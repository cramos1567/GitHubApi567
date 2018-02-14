import requests
import json

def getUserCommits(userID):
    if not isinstance(userID,str):
        return "InvalidInput"

    if userID == "":
        return "InvalidInput"
    
    theStr = "User: " + userID + '\n'

    getRepos = requests.get("https://api.github.com/users/" + userID + "/repos")
    print(str(getRepos))
    if str(getRepos) != "<Response [200]>":
        return "Invalid Username"

    listOfRepos = []
    for r in getRepos.json():
        listOfRepos += [r['name']]
    #print(listOfRepos)

    listOfCommits = []
    for r in listOfRepos:
        getCommits = requests.get("https://api.github.com/repos/" + userID + "/" + r + "/commits")
        if str(getCommits) != "<Response [200]>":
            return "Invalid Repo"
        listOfCommits += [len(getCommits.json())]
    #print(listOfCommits)

    for r in range(0, len(listOfRepos)):
        theStr += "Repo: " + listOfRepos[r] + " Number of commits: " + str(listOfCommits[r]) + '\n'
    return theStr 

if __name__ == '__main__':
    print(getUserCommits("cramos1567"))
    print(getUserCommits("crramos1567"))
