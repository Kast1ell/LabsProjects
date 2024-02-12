import pyodbc
from POJO.Pojoes import *

names = "Chemicals", "UserProfile", "Reports", "Roles"
conn_str = 'DRIVER={SQL Server};SERVER=VIKTORIA\\SQLEXPRESS;DATABASE=HazardDB2;Trusted_Connection=yes;'


def get_all(name):
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM " + str(name))
        rows = cursor.fetchall()
        print("Getted " + name)
        for row in rows:
            print(row)
    except Exception as e:
        print("Ошибка при выполнении запроса:", e)
    finally:
        cursor.close()
        conn.close()
    return rows


def get_by_id(name, ident):
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM " + name + " WHERE id =" + str(ident))
        rows = cursor.fetchall()
        print("Getted " + str(ident))
        for row in rows:
            print(row)
    except Exception as e:
        print("Ошибка при выполнении запроса:", e)
    finally:
        cursor.close()
        conn.close()
    return rows


def get_user_by_login(login):
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM UserProfile WHERE UserLogin = '" + str(login) + "'")
        rows = cursor.fetchall()
        print("Getted " + str(login))
        for row in rows:
            print(row)
    except Exception as e:
        print("Ошибка при выполнении запроса:", e)
    finally:
        cursor.close()
        conn.close()
    return rows


def get_chemical_by_name(name):
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Chemicals WHERE ChemicalsName = '" + str(name) + "'")
        rows = cursor.fetchall()
        print("Getted " + str(name))
        for row in rows:
            print(row)
    except Exception as e:
        print("Ошибка при выполнении запроса:", e)
    finally:
        cursor.close()
        conn.close()
    return rows


def insert_user(buf):
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()
    try:
        # Создание объекта Cursor
        cursor = conn.cursor()
        # Запрос для вставки нового пользователя
        sql_query = """
            INSERT INTO UserProfile (UserLogin, UserPassword, FirstName, LastName, Phone, AccessKey)
            VALUES (?, ?, ?, ?, ?, ?)
            """
        # Выполнение запроса
        cursor.execute(sql_query, (buf.user_login, buf.user_password,
                                   buf.first_name, buf.last_name, buf.phone, buf.access_key))
        # Подтверждение транзакции
        conn.commit()
    except Exception as e:
        print("Ошибка при выполнении запроса:", e)
    finally:
        cursor.close()
        conn.close()

#insert_user(UserProfile(0, "maxi", "2202", "kuri", "Shelvi", "4440032", "2323231"))
# buf = get_by_id("UserProfile", 6)
# buf = buf[0]
# print(buf.Id, buf.UserLogin, buf.UserPassword,
      # buf.FirstName, buf.LastName, buf.Phone, buf.AccessKey)
# get_user_by_login("alex_brown")
# for name in names:
#     get_all(name)
