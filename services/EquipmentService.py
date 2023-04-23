from settings import EQUIPMENT_TABLE, mydb

## Добавление оборудования, в качестве параметра поступает тип оборудования
def add_equipment(type):
    add_equipment_query = f"INSERT INTO {EQUIPMENT_TABLE}(type) VALUES(%s);"
    with mydb.cursor() as cursor:
        cursor.execute(add_equipment_query, type)
        mydb.commit()

## Вывод всего оборудования
def get_equipments():
    get_equipment_query = f"SELECT * FROM {EQUIPMENT_TABLE}"
    with mydb.cursor() as cursor:
        cursor.execute(get_equipment_query)
        result = cursor.fetchall()
        return "\n".join(map(str, result))

