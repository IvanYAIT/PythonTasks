from services.user_input import call_until_valid_input

class Task1:
    @call_until_valid_input
    def get_restaurant_menu():
        menu = input("Доступное меню: ")
        return menu.split(";")

    def print_menu(menu):
        menu_string = ""
        for dish_index in range(len(menu)):
              menu_string += menu[dish_index]
              if(dish_index < len(menu)):
                    menu_string += ", "
        print(f"На данный момент в меню есть: {menu_string}")

    @classmethod
    def main(cls):
        menu = cls.get_restaurant_menu()
        cls.print_menu(menu)