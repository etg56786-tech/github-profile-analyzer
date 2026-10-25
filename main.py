import requests

username = input("What is the username you would like to analyze?: ")

url = f"https://api.github.com/users/{username}"
url2 = f"https://api.github.com/users/{username}/repos"
data = requests.get(url)
repositories_data = requests.get(url2)

print(data.status_code)
profile = data.json()
profile_ex = repositories_data.json()

if data.status_code == 200 and repositories_data.status_code == 200:
    print(f"Github Username = {profile['login']}\n")
    print(f"Github Repositories = {profile['public_repos']}\n")
    for reposit in profile_ex:
        desc = reposit["description"] 
        print(f"Name: {reposit['name']}")
        print(f"Programming Language: {reposit['language']}")
        print(f"Stars: {reposit['stargazers_count']} (Give it a try regardless!)")
        if desc is not None:
            print(f"Description: {reposit['description']}")
        else:
            print(f"Description was not specified\n")
elif data.status_code != 200:
    print("The provided username does not exist!")
elif repositories_data.status_code != 200:
    print("No repositories to view")
