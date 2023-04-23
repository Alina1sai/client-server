from settings import EQUIPMENT_TABLE, mydb

## Добавление оборудования, в качестве параметра поступает тип оборудования
def add_equipment(type):
    add_equipment_query = f"INSERT INTO {EQUIPMENT_TABLE}(type) VALUES(%s);"
    with mydb.cursor() as cursor:
        cursor.execute(add_equipment_query, type)
        mydb.commit()


