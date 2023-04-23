from settings import SCHEDULE_TABLE,USERS_TABLE, EQUIPMENT_TABLE, mydb


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