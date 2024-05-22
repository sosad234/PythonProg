import psycopg2

# Подключение к базе данных
conn = psycopg2.connect(
    dbname="mydatabase",
    user="myuser",
    password="mypassword",
    host="localhost"
)

# Создание курсора
cur = conn.cursor()

# Выполнение SQL-запроса
cur.execute("SELECT * FROM mytable")

# Получение результатов запроса
rows = cur.fetchall()
for row in rows:
    print(row)

# Закрытие курсора и соединения
cur.close()
conn.close()

