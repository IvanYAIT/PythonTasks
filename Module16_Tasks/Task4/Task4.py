from services.user_input import call_until_valid_input

class Task4:

    @call_until_valid_input
    def get_command():
        command = input("Гость пришел или ушел? ").lower()
        if(command != "пришел" and command != "ушел" and command != "пора спать"):
            raise ValueError
        return command
    
    @call_until_valid_input
    def get_guest_name():
        return input("Имя гостя: ")
    
    def try_add_guest(guests, guest_name):
        if(len(guests) >= 6):
            print(f"Прости, {guest_name}, но мест нет.")
            return guests
        else:
            guests.append(guest_name)
            print(f"Привет, {guest_name}!")
            return guests
        
    def try_remove_guest(guests, guest_name):
        name_in_chars = guest_name.lower()
        name = name_in_chars[0].upper()
        for char_index in range(1, len(name_in_chars)):
            name += name_in_chars[char_index].lower()

        try:
            guests.remove(name)
            print(f"Пока, {name}!")
            return guests
        except:
            print("Такого гостя нет")
            return guests


    @classmethod
    def main(cls):
        guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
        while True:
            print(f"Сейчас на вечеринке {len(guests)} человек: {guests}")
            command = cls.get_command()

            if(command == "пора спать"):
                print("Вечеринка закончилась, все легли спать.")
                break
            
            guest_name = cls.get_guest_name()
            if(command == "пришел"):
                guests = cls.try_add_guest(guests, guest_name)
            elif (command == "ушел"):
                guests = cls.try_remove_guest(guests, guest_name)

