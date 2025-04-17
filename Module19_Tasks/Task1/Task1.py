from services.user_input import call_until_valid_input

class Task1:
    @call_until_valid_input
    def get_songs_amount():
        amount = int(input("Сколько песен выбрать? "))

        if(amount <= 0):
            raise ValueError("Количество песен не может быть меньше 0")
        
        return amount
    
    @call_until_valid_input
    def get_songs_lenght(songs_amount, songs):
        result = 0
        for index in range(songs_amount):
            user_song = input(f"Название {index+1} песни: ")
            if(songs.get(user_song) is None):
                print("Такой песни нет")
                continue
            result += songs[user_song]
        return round(result, 2)

    @classmethod
    def main(cls):
        violator_songs = {
            'World in My Eyes': 4.86,
            'Sweetest Perfection': 4.43,
            'Personal Jesus': 4.56,
            'Halo': 4.9,
            'Waiting for the Night': 6.07,
            'Enjoy the Silence': 4.20,
            'Policy of Truth': 4.76,
            'Blue Dress': 4.29,
            'Clean': 5.83
        }
        amount = cls.get_songs_amount()
        songs_lenght = cls.get_songs_lenght(amount, violator_songs)
        print(f"Общее время звучания песен: {songs_lenght}")