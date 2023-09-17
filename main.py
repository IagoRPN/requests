import requests 

username = 'amzn'
api_base_url = f'https://api.github.com/users/{username}'

r = requests.get(api_base_url)
print(r.status_code)
print(r.json())
print(r.url)