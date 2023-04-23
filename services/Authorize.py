from settings import AUTHORIZED_USERS_TABLE, USERS_TABLE, mydb

# Сервис для авторизации пользователя, пользователь вводит логин и пароль, после чего происходит поиск записи в бд,
# по этому логину и паролю, если запись есть, то применяется метод add_authorized_users() где добавляется запись с авторизованными
# пользователями


def authorize(login, password):
    authorize_query = f"SELECT * FROM {USERS_TABLE} WHERE login = '{login}' AND password = '{password}'"
    with mydb.cursor() as cursor:
        cursor.execute(authorize_query)
        result = cursor.fetchone()
        if (result is not None):
            user_id = result[0]
            mydb.commit()
            add_authorized_users(user_id)
            return True
        else:
            return False


def add_authorized_users(user_id):
    add_authorized_users_query = f"INSERT INTO {AUTHORIZED_USERS_TABLE}(user_id) VALUES(%s)"
    with mydb.cursor() as cursor:
        cursor.execute(add_authorized_users_query, user_id)
        mydb.commit()
