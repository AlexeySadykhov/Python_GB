import sys
import sqlite3
from sqlite3 import Error


def item_exists(array):
    last_el = array[0]
    for item in array:
        last_el = item
        if item:
            return True
    if not last_el:
        return False


def connect_to_db(path):
    try:
        connect = sqlite3.connect(path)
        return connect
    except Error as e:
        print(f"The error '{e}' occurred.")
        sys.exit(1)


def select_request(connect, request):
    cursor = connect.cursor()
    try:
        cursor.execute(request)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred.")
        sys.exit(1)


def change_request(connect, request):
    cursor = connect.cursor()
    try:
        cursor.execute(request)
        connect.commit()
    except Error as e:
        print(f"The error '{e}' occurred.")
        sys.exit(1)


def insert_query(vals):
    query = """INSERT INTO 
                   contacts([Фамилия], 
                            [Имя], 
                            [Отчество],
                            [Организация],
                            [Мобильный телефон],
                            [Домашний телефон],
                            [Рабочий телефон]) 
                VALUES"""
    vls = str(tuple(vals)).replace("None", "NULL")
    return f"{query}{vls};"


create_query = """CREATE TABLE contacts(
                      [Фамилия] TEXT,
                      [Имя] TEXT, 
                      [Отчество] TEXT, 
                      [Организация] TEXT, 
                      [Мобильный телефон] TEXT, 
                      [Домашний телефон] TEXT, 
                      [Рабочий телефон] TEXT);"""
