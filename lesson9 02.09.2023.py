import sqlite3

connection = None
try:
    connection = sqlite3.connect("students1.sl3", 5)
    cur = connection.cursor()
    # 1
    # cur.execute("CREATE TABLE S2011(id INT PRIMARY KEY, name VARCHAR(20), age INT, avg_grade FLOAT)")
    # connection.commit()
    # print(connection)
    # print(cur)
    # 2
    # cur.execute("INSERT INTO S2011 (id, name, age, avg_grade) VALUES(1, 'Temnenko Illia', 12, 12)")
    # cur.execute("INSERT INTO S2011 (id, name, age, avg_grade) VALUES(2, 'Bigun Serhii', 12, 9.5)")
    # cur.execute("INSERT INTO S2011 (id, name, age, avg_grade) VALUES(3, 'Lisnevskiy Bronislav', 13, 12)")
    # cur.execute("INSERT INTO S2011 (id, name, age, avg_grade) VALUES(4, 'Sameliuk Mykyta', 14, 10.5)")
    # cur.execute("INSERT INTO S2011 (id, name, age, avg_grade) VALUES(5, 'Ilchyshyn Vladyslav', 15, 12)")
    # cur.execute("INSERT INTO S2011 (id, name, age, avg_grade) VALUES(6, 'Zviahintsev Andrii', 14, 12)")
    # cur.execute("INSERT INTO S2011 (id, name, age, avg_grade) VALUES(7, 'Sabarin Georhii', 15, 11)")
    # connection.commit()
    # 3
    # cur.execute("SELECT id, name, age, avg_grade FROM S2011")
    # 4
    # cur.execute("SELECT id, name, age, avg_grade FROM S2011 WHERE age = 12")
    # 5
    cur.execute("SELECT name FROM S2011 WHERE age = 12")
    connection.commit()
    res = cur.fetchall()
    print(res)
except Exception as ex:
    print(ex)
finally:
    connection.close()
