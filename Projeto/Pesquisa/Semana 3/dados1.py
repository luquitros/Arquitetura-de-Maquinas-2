import requests
from bs4 import BeautifulSoup

def get_userbenchmark_data():
    url = "https://gpu.userbenchmark.com/Compare/Nvidia-RTX-4060-vs-Nvidia-RTX-3060/4143vs4105"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, 'html.parser')
    
    performance = {}
    for row in soup.find_all('div', class_='value-cell'):  # Pode precisar de ajustes
        key = row.find_previous_sibling('div').text.strip()
        value = row.text.strip()
        performance[key] = value
    
    return performance

def get_passmark_data():
    url_4060 = "https://www.videocardbenchmark.net/gpu.php?gpu=GeForce+RTX+4060"
    url_3060 = "https://www.videocardbenchmark.net/gpu.php?gpu=GeForce+RTX+3060"
    
    def fetch_score(url):
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(response.text, 'html.parser')
        score = soup.find('span', class_='orangebig').text.strip()
        return score
    
    return {"RTX 4060": fetch_score(url_4060), "RTX 3060": fetch_score(url_3060)}

if __name__ == "__main__":
    print("UserBenchmark Data:")
    print(get_userbenchmark_data())
    
    print("\nPassMark Data:")
    print(get_passmark_data())
