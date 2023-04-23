import socketserver

from Services.Authorize import authorize
from Services.EquipmentService import get_equipments, add_equipment, get_equipment_by_type
from Services.ScheduleService import get_schedule, register_user_to_equipment


class EquipmentHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Подключился новый клиент
        print(f'Client connected: {self.client_address}')

        # Обрабатываем сообщения от клиента
        while True:
            # Получаем сообщение от клиента
            message = self.request.recv(1024).decode().strip()

            # Проверяем, что сообщение не пустое
            if message:
                # Разбиваем сообщение на команду и аргументы
                command, *args = message.split()

                # Выполняем команду
                response = self.execute_command(command, args)

                # Отправляем ответ клиенту
                self.request.sendall(response.encode())

            else:
                # Клиент отключился
                print(f'Client disconnected: {self.client_address}')
                break

    def execute_command(self, command, args):
        # Обработка команды

        if command == 'get_equipment_list':
            # Обработка команды get_equipment_list
            return get_equipments()

        elif command == 'add_equipment':
            # Обработка команды add_equipment
            equipment_type = args[0]
            add_equipment(equipment_type)
            return f'Оборудование {equipment_type} добавлено'

        elif command == 'get_equipment_by_type':
            # Обработка команды get_equipment_by_type
            equipment_type = input()
            return get_equipment_by_type(equipment_type)

        elif command == 'get_schedule':
            # Обработка команды get_schedule
            equipment_type = input()
            return get_schedule(equipment_type)

        elif command == 'register':
            # Обработка команды register
            user_id, equipment_id, start_time, end_time = args
            if register_user_to_equipment(user_id, equipment_id, start_time, end_time):
                return f'Оборудование забронировано с {start_time} до {end_time}'
            else:
                return 'Оборудование занято'

        else:
            # Неизвестная команда
            return 'Неизвестная команда'

if __name__ == '__main__':
    # Создаем сервер
    host = 'localhost'
    port = 12345
    server = socketserver.TCPServer((host, port), EquipmentHandler)

    # Запускаем сервер
    print(f'Server started on {host}:{port}')
    server.serve_forever()
