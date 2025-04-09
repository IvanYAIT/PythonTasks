from services.user_input import call_until_valid_input

class Task4:
    @call_until_valid_input
    def get_amount_of_films_to_add():
        user_number = int(input("Сколько фильмов хотите добавить? "))

        if(user_number <= 0):
            raise ValueError
        
        return user_number
    
    def add_films_to_favorite(exist_films, amount_of_films):
        result = []
        is_added = False
        for _ in range(amount_of_films):
            film_to_add = input("Введите название фильма: ")
            for favorite_film in result:
                if(film_to_add.lower() == favorite_film.lower()):
                    is_added = True

            if(is_added):
                is_added = False
                print(f"Фильм {film_to_add} уже добавлен")
                continue

            for film in exist_films:
                if(film.lower() == film_to_add.lower()):
                    result.append(film_to_add)
                    is_added = True
                    break
            if(not is_added):
                print(f"Ошибка: фильма {film_to_add} у нас нет :(")
            else:
                is_added = False
        return result
    
    def print_favorite_films(favorite_films):
        favorite_films_str = ""
        for film in favorite_films:
            favorite_films_str += film
            if(film != favorite_films[len(favorite_films)-1]):
                favorite_films_str += ", "
        print(f"Ваш список любимых фильмов: {favorite_films_str}")

    @classmethod
    def main(cls):
        films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
        amount_of_films_to_add = cls.get_amount_of_films_to_add()
        favorite_films = cls.add_films_to_favorite(films, amount_of_films_to_add)
        cls.print_favorite_films(favorite_films) 