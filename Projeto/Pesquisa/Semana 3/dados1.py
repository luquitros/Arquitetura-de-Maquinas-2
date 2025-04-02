import requests
from bs4 import BeautifulSoup

def get_userbenchmark_data():
    url = "https://gpu.userbenchmark.com/Compare/Nvidia-RTX-4060-vs-Nvidia-RTX-3060/4143vs4105"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    
    if response.status_code != 200:
        return {"error": "Failed to fetch UserBenchmark data"}
    
    soup = BeautifulSoup(response.text, 'html.parser')
    performance = {}
    
    # Adjusted parsing logic to handle potential changes in the website structure
    rows = soup.find_all('div', class_='bench-group')  # Adjusted class name
    for row in rows:
        key_element = row.find('div', class_='name')  # Adjusted class name
        value_element = row.find('div', class_='value')  # Adjusted class name
        
        if key_element and value_element:
            key = key_element.text.strip()
            value = value_element.text.strip()
            performance[key] = value
    
    return performance

def get_passmark_data():
    url_4060 = "https://www.videocardbenchmark.net/gpu.php?gpu=GeForce+RTX+4060"
    url_3060 = "https://www.videocardbenchmark.net/gpu.php?gpu=GeForce+RTX+3060"
    
    def fetch_score(url):
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        
        if response.status_code != 200:
            return "Error fetching data"
        
        soup = BeautifulSoup(response.text, 'html.parser')
        score_element = soup.find('span', class_='orangebig')
        
        if score_element:
            return score_element.text.strip()
        else:
            return "Score not found"
    
    return {"RTX 4060": fetch_score(url_4060), "RTX 3060": fetch_score(url_3060)}

if __name__ == "__main__":
    print("UserBenchmark Data:")
    print(get_userbenchmark_data())
    
    print("\nPassMark Data:")
    print(get_passmark_data())
