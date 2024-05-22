# Отчет.
## Задание
Реализуйте парсер с использованием Selenium для сбора данных с веб-страницы. Это может быть:
онлайн-каталог
интернет-магазин
энциклопедия и т.д.
Основное требование: чтобы ресурсы не повторялись внутри группы, т.е. все должны парсить разные сайты.

Создайте таблицы БД и заполните их данными, полученными с помощью парсера. У вас должно быть минимум 2 таблицы. При заполнении в запросах используйте именованные плейсхолдеры драйвера вашей СУБД.
Напишите запросы для выборки данных из БД с использованием PyPika Query Builder. У вас должно быть:
2 запроса с JOIN
3 запроса с расчётом статистики/группировкой/агрегирующими функциями
Оформите отчёт в README.md. Отчёт должен содержать:
Условия задач
Описание проделанной работы
Скриншоты результатов
Ссылки на используемые материалы

## Код 
```python
import pandas as pd
import wikipedia as wp
import sqlite3

# Получаем HTML-страницу из Википедии
html = wp.page("List_of_video_games_considered_the_best").html().encode("UTF-8")

try:
    df = pd.read_html(html)[1]  # Пытаемся получить вторую таблицу
except IndexError:
    df = pd.read_html(html)[0]  # Если второй таблицы нет, берем первую

# Берем первые 300 строк
df = df.iloc[:300, :]

# Создаем таблицы
games_df = df.iloc[:, [0, 2]].rename(columns=lambda x: x.replace(']', '').replace('[', '').strip())  # Название и жанр
games_df.columns = ['name', 'genre']  # Переименовываем столбцы

platforms_df = df.iloc[:, [0, 1, 3]].rename(columns=lambda x: x.replace(']', '').replace('[', '').strip())  # Название, издатель, платформа
platforms_df.columns = ['name', 'publisher', 'platform']  # Переименовываем столбцы

# Создаем соединение с базой данных SQLite
conn = sqlite3.connect("games.db")

# Создаем таблицы
games_df.to_sql("games", conn, if_exists="replace", index=False)
platforms_df.to_sql("platforms", conn, if_exists="replace", index=False)

# Закрываем соединение
conn.close()

print("Таблицы созданы успешно!")


from pypika import Query, Table, Case, functions as fn

# Подключение к базе данных
conn = sqlite3.connect("games.db")
cursor = conn.cursor()

games = Table("games")
platforms = Table("platforms")

# 1. Запрос с JOIN для получения названий игр, жанров и издателей
query = (
    Query.from_(games)
    .join(platforms)
    .on(games.name == platforms.name)
    .select(games.name, games.genre, platforms.publisher)
)
cursor.execute(str(query))
print("Названия игр, жанры и издатели:")
for row in cursor.fetchall():
    print(row)

# 2. Запрос с группировкой и подсчетом количества игр для каждого жанра
query = (
    Query.from_(games)
    .select(games.genre, fn.Count(games.name).as_("game_count"))
    .groupby(games.genre)
)
cursor.execute(str(query))
print("\nКоличество игр по жанрам:")
for row in cursor.fetchall():
    print(row)

# Закрытие соединения с базой данных
conn.close()
```

## Результат 

```Таблицы созданы успешно!
Названия игр, жанры и издатели:
(1971, 'Strategy', 'The Oregon Trail')
(1972, 'Sports', 'Pong')
(1977, 'Top-down shooter', 'Combat')
(1977, 'Top-down shooter', 'Zork')
(1977, 'Adventure', 'Combat')
(1977, 'Adventure', 'Zork')
(1978, "Shoot 'em up", 'Space Invaders')
(1979, "Shoot 'em up", 'Asteroids')
(1980, 'Action-adventure', 'Adventure')
(1980, 'Action-adventure', 'Battlezone')
(1980, 'Action-adventure', 'Missile Command')
(1980, 'Action-adventure', 'Pac-Man')
(1980, 'Vehicle simulation', 'Adventure')
(1980, 'Vehicle simulation', 'Battlezone')
(1980, 'Vehicle simulation', 'Missile Command')
(1980, 'Vehicle simulation', 'Pac-Man')
(1980, "Shoot 'em up", 'Adventure')
(1980, "Shoot 'em up", 'Battlezone')
(1980, "Shoot 'em up", 'Missile Command')
(1980, "Shoot 'em up", 'Pac-Man')
(1980, 'Maze', 'Adventure')
(1980, 'Maze', 'Battlezone')
(1980, 'Maze', 'Missile Command')
...
('Top-down shooter', 3)
('Tower defense', 1)
('Turn-based strategy', 7)
('Vehicle simulation', 2)
```

файл games.db там таблицы можете посмотреть 

## Список источников 
1. https://en.wikipedia.org/wiki/List_of_video_games_considered_the_best
2. https://habr.com/ru/articles/513218/