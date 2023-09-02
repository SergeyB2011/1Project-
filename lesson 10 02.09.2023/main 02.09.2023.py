import sqlite3
connection = None
try:
    connection = sqlite3.connect("student.sl3", 5)
    cur = connection.cursor()
    #cur.execute("CREATE TABLE S2011(id INT PRIMARY KEY, name VARCHAR(20), age INT,avg_grade FLOAT)")
    #cur.execute("INSERT INTO S2011 (id, name, ade, avg_grade) VALUES(1, 'Temnenko Illia', 12, 12)")
    #cur.execute("INSERT INTO S2011 (id, name, ade, avg_grade) VALUES(2, 'Bigun Serhii', 12, 12)")
    #cur.execute("INSERT INTO S2011 (id, name, ade, avg_grade) VALUES(3, 'Lisnevskiy Bronislav', 13, 12)")
    #cur.execute("INSERT INTO S2011 (id, name, ade, avg_grade) VALUES(4, 'Sameliuk Mykyta', 14, 12)")
    #cur.execute("INSERT INTO S2011 (id, name, ade, avg_grade) VALUES(5, 'Ilchyshyn Vladislav', 15, 12)")
    #cur.execute("INSERT INTO S2011 (id, name, ade, avg_grade) VALUES(6, 'Zviahintsev Andrii', 14, 12)")
    #cur.execute("INSERT INTO S2011 (id, name, ade, avg_grade) VALUES(7, 'Sabarin Georgii', 12, 12)")
    cur.execute("SELECT id, name, ade,avg_grade FROM S2011")
    #print(connection)
    #print(cur)
    #connection.commit()
    res = cur.fetchall()
    print(res)
except Exception as ex:
    print(ex)
finally:
    connection.close()