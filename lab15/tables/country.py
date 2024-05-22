
from bs4 import BeautifulSoup
import requests

url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE%D0%BA%D1%80%D0%B0%D1%82%D0%BD%D1%8B%D1%85_%D1%87%D0%B5%D0%BC%D0%BF%D0%B8%D0%BE%D0%BD%D0%BE%D0%B2_%D0%9E%D0%BB%D0%B8%D0%BC%D0%BF%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D1%85_%D0%B8%D0%B3%D1%80'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table', {'class': 'wikitable'})
rows = table.find_all('tr')


countries = []  # Список для стран


for row in rows:
    cells = row.find_all('td')
    if len(cells) > 0:
        country = cells[1].text.strip()
        countries.append(country)
        

print(countries)

