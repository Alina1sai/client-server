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

## Поиск записей по оборудованию и пользователю
def get_schedule(equipment_type):
    get_registered_users_on_equipment_query= f"SELECT u.surname, u.name, u.middlename, e.type, s.started_at, s.finished_at " \
                                             f"FROM {SCHEDULE_TABLE} as s " \
                                             f"JOIN {EQUIPMENT_TABLE} as e on s.equipment_id = e.id " \
                                             f"JOIN {USERS_TABLE} as u on s.user_id = u.id " \
                                             f"WHERE e.type = '{equipment_type}'"

    with mydb.cursor() as cursor:
        cursor.execute(get_registered_users_on_equipment_query)
    result = cursor.fetchall()
    schedule = []
    for row in result:
        schedule.append([row[0], row[1], row[2], row[3], row[4].strftime('%m/%d/%Y, %H:%M:%S'), row[5].strftime('%m/%d/%Y, %H:%M:%S')])
    return "\n".join(map(str, schedule))