import requests 

username = 'amzn'
api_base_url = f'https://api.github.com/users/{username}'

r = requests.get(api_base_url)
print(r.status_code)

dados = r.json()

print(f"Nome do usuário: {dados['name']}")
print(f"Nome do usuário: {dados['login']}")
print(f"Nome do usuário: {dados['created_at']}")
print(f"Nome do usuário: {dados['public_repos']}")