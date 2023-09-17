import requests 

username = 'amzn'
url = f"https://api.github.com/users/{username}/followers"

access_token = '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'
headers = {'Authorization': 'Bearer ' + access_token,
           'X-GitHub-Api-Version': '2022-11-28'}

page = 1
follower_list = []

while True:

    url_page = f"{url}?page={page}"
    response = requests.get(url, headers=headers)
    print(response.status_code)

    followers = response.json()
    if (len(followers)) == 0:
        break

    follower_list.append(followers)
    page += 1
    print(url_page)
    print(page)