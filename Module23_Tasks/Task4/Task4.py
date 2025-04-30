import os
from services.user_input import call_until_valid_input

class Task4:
    PATH_TO_CHAT_FILE = os.path.abspath(__file__).replace('Task4.py', 'chat.txt')

    @call_until_valid_input
    def get_command(self):
        command = int(input())

        if not 0 < command < 5:
            raise ValueError('Такой команды нет')
        
        return command
    
    @call_until_valid_input
    def get_username(self):
        return input('Введите имя пользователя: ')

    @call_until_valid_input
    def get_message(self, user_name):
        msg = input()
        return f'{user_name}: {msg}'

    def print_chat(self):
        try:
            with open(self.PATH_TO_CHAT_FILE, 'r') as file:
                for line in file.readlines():
                    print(line)
        except:
            print('Чат пустой')
    
    def add_message_to_chat(self, message):
        with open(self.PATH_TO_CHAT_FILE, '+a') as file:
            file.write(f'{message}\n')

    def main(self):
        username = self.get_username()
        while True:
            print('1 - Сменить пользователя\n', 
                  '2 - Посмотреть историю сообщений\n',
                  '3 - Написать сообщение\n',
                  '4 - Выход')
            
            command = self.get_command()

            if command == 4:
                return
            elif command == 1:
                username = self.get_username()
            elif command == 2:
                self.print_chat()
            elif command == 3:
                message = self.get_message(username)
                self.add_message_to_chat(message)