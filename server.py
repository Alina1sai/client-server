import socketserver

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

        if command == 'login':
            # Обработка команды login
            username = args[0]
            return f'Добро пожаловать, {username}!'

        elif command == 'get_equipment_list':
            # Обработка команды get_equipment_list
            return 'Список оборудования'

        elif command == 'add_equipment':
            # Обработка команды add_equipment
            equipment_name = args[0]
            return f'Оборудование {equipment_name} добавлено'

        elif command == 'get_schedule':
            # Обработка команды get_schedule
            equipment_name = args[0]
            return f'Расписание оборудования {equipment_name}'

        elif command == 'book_equipment':
            # Обработка команды book_equipment
            equipment_name, start_time, end_time = args
            return f'Оборудование {equipment_name} забронировано с {start_time} до {end_time}'

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
