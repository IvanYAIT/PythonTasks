from services.user_input import call_until_valid_input

class Task6:
    @call_until_valid_input
    def get_command(self):
        command = int(input())

        if(command < 0 and command >4):
            raise ValueError("Такой команды нет")
        
        return command
    
    @call_until_valid_input
    def get_surname(self):
        return input("Введите фамилию для поиска: ")

    @call_until_valid_input
    def get_person(self):
        person = input("Введите имя и фамилию нового контакта (через пробел): ")
        result = tuple(person.split(" "))
        if(len(result) != 2):
            raise ValueError
        return result
    
    @call_until_valid_input
    def get_phone_number(self):
        result = int(input("Введите номер телефона: "))
        if(result <= 0):
            raise ValueError("Номер телефона должен быть больше 0")
        return result

    def add_contact(self, contacts):
        person = self.get_person()
        if(contacts.get(person) is not None):
            print("Такой человек уже есть в контактах.")
            return
        
        phone_number = self.get_phone_number()
        contacts[person] = phone_number

    def find_contact(self, contacts):
        surname = self.get_surname()
        for person in contacts.keys():
            if(person[1] == surname):
                print(f"{person[0]} {person[1]} {contacts[person]}")

    def main(self):
        contacts = dict()
        while True:
            print("Введите номер действия:\n 1. Добавить контакт\n 2. Найти человека\n 3. Выход")
            command = self.get_command()
            if(command == 1):
                self.add_contact(contacts)
            elif(command == 2):
                self.find_contact(contacts)
            elif(command == 3):
                return
            print(f"Текущий словарь контактов:  {contacts}")
