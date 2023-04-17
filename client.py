import socket

def connect_to_server():
    # Создаем сокет и подключаемся к серверу
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 12345
    client_socket.connect((host, port))
    return client_socket

def send_message(client_socket, message):
    # Отправляем сообщение на сервер
    message = message.encode()
    client_socket.send(message)

def receive_message(client_socket):
    # Получаем ответ от сервера
    message = client_socket.recv(1024)
    return message.decode()

def main():
    # Подключаемся к серверу
    client_socket = connect_to_server()

    # Запрашиваем имя пользователя
    username = input('Введите имя пользователя: ')
    send_message(client_socket, f'login {username}')

    # Основной цикл клиента
    while True:
        # Запрашиваем команду у пользователя
        command = input('Введите команду: ')

        # Отправляем команду на сервер
        send_message(client_socket, command)

        # Получаем ответ от сервера и выводим на экран
        response = receive_message(client_socket)
        print(response)

        # Если получили сообщение о выходе, закрываем соединение
        if response == 'Вы вышли из системы':
            client_socket.close()
            break

if __name__ == '__main__':
    main()

