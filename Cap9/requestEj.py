import requests

response = requests.get('https://api.github.com')
print(response.status_code)
print("-----------------------------------------------------")
print(response.content)
print("-----------------------------------------------------")
print(response.text)
print("-----------------------------------------------------")
print(response.json())

print(response.headers)

# get con parametros
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)

# Inspeccionando el resultado
json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')  # Python 3.6+

# get con lista de tuplas
res = requests.get(
'https://api.github.com/search/repositories',
params=[('q', 'requests+language:python')],
)
print(res)

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)

json_response = response.json()
repository = json_response['items'][0]
print(f'Text matches: {repository["text_matches"]}')

requests.post('https://httpbin.org/post', data={'key':'value'})
requests.put('https://httpbin.org/put', data={'key':'value'})
requests.delete('https://httpbin.org/delete')
requests.head('https://httpbin.org/get')
requests.patch('https://httpbin.org/patch', data={'key':'value'})
requests.options('https://httpbin.org/get')

requests.post('https://httpbin.org/post', data={'key':'value'})

requests.get('https://api.github.com', timeout=1)
requests.get('https://api.github.com', timeout=3.05)