
import requests
params = {'q': 'prajwal magishettar', 'page': 1}
response = requests.get('https://google.com/search', params=params)
print(response.url)  # Shows full URL with params
