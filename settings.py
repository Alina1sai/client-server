from getpass import getpass

import pymysql


# Конфигурация приложения

# Названия таблиц в бд

AUTHORIZED_USERS_TABLE = 'authorized_users'
EQUIPMENT_TABLE = 'equipments'
SCHEDULE_TABLE = 'schedules'
USERS_TABLE = 'users'

# бд

mydb = pymysql.connect(
    host="localhost",
    user="admin",
    password="qwerty1",
    database='biolab',
)
