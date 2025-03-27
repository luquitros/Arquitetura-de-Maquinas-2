import requests
from bs4 import BeautifulSoup

url = "https://gpu.userbenchmark.com/"  # Página de benchmarks de GPUs
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Coletar os nomes das GPUs e seus benchmarks
gpus = soup.find_all('span', class_='content')
for gpu in gpus[:10]:  # Exibir apenas as 10 primeiras GPUs
    print(gpu.text)

    