import requests
from bs4 import BeautifulSoup
import sqlite3

# Получаем HTML-содержимое страницы
url = "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE%D0%BA%D1%80%D0%B0%D1%82%D0%BD%D1%8B%D1%85_%D1%87%D0%B5%D0%BC%D0%BF%D0%B8%D0%BE%D0%BD%D0%BE%D0%B2_%D0%9E%D0%BB%D0%B8%D0%BC%D0%BF%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D1%85_%D0%B8%D0%B3%D1%80"
response = requests.get(url)
html_content = response.content

# Парсим HTML-содержимое с помощью BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")
table = soup.find("table", {"class": "wikitable"})

# Создаем базу данных SQLite и таблицы
conn = sqlite3.connect("olympics2.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS athletes (
                athlete_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            )""")

c.execute("""CREATE TABLE IF NOT EXISTS countries (
                country_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            )""")

c.execute("""CREATE TABLE IF NOT EXISTS sports (
                sport_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            )""")

# Заполняем таблицы данными из HTML-таблицы
for row in table.find_all("tr")[1:]:
    cells = row.find_all("td")
    if cells:
        athlete_name = cells[0].text.strip()
        country_name = cells[1].text.strip()
        sport_name = cells[2].text.strip()

        # Добавляем спортсмена в таблицу athletes
        c.execute("INSERT INTO athletes (name) VALUES (?)", (athlete_name,))
        athlete_id = c.lastrowid

        # Добавляем страну в таблицу countries
        c.execute("INSERT OR IGNORE INTO countries (name) VALUES (?)", (country_name,))
        c.execute("SELECT country_id FROM countries WHERE name = ?", (country_name,))
        country_id = c.fetchone()[0]

        # Добавляем вид спорта в таблицу sports
        c.execute("INSERT OR IGNORE INTO sports (name) VALUES (?)", (sport_name,))
        c.execute("SELECT sport_id FROM sports WHERE name = ?", (sport_name,))
        sport_id = c.fetchone()[0]

        # Связываем спортсмена со страной и видом спорта через внешние ключи
        # (этот шаг не выполняется в данном примере)

conn.commit()
conn.close()