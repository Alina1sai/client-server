from settings import SCHEDULE_TABLE, USERS_TABLE, EQUIPMENT_TABLE, mydb


# Регистрация пользователя на оборудование, если оно свободно
def register_user_to_equipment(user_id, equipment_id, started_at, finished_at):
    if check_free_equipment(started_at, finished_at):
        register_user_to_equipment_query = f"INSERT INTO {SCHEDULE_TABLE} " \
                                           f"(user_id, equipment_id, started_at, finished_at)" \
                                           f" VALUES (%s, %s, %s, %s)"
        with mydb.cursor() as cursor:
            cursor.execute(register_user_to_equipment_query, (user_id, equipment_id, started_at, finished_at))
            mydb.commit()
        return True
    else:
        return False

# Поиск занятого оборудования
def check_free_equipment(started_at, finished_at):
    check_free_equipment_query = f"SELECT count(*) FROM " \
                                 f"{SCHEDULE_TABLE} WHERE started_at >= '{started_at}' AND started_at <= '{finished_at}' " \
                                 f"OR finished_at >= '{started_at}' AND finished_at <= '{finished_at}'"
    with mydb.cursor() as cursor:
        cursor.execute(check_free_equipment_query)
        result = cursor.fetchone()[0]
        if result:
            return False
        else:
            return True
