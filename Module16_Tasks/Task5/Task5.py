from services.user_input import call_until_valid_input

class Task5:
    @call_until_valid_input
    def get_amount_of_songs():
        song_amount = int(input("Сколько песен выбрать? "))
        
        if(song_amount <= 0):
            raise ValueError

        return song_amount
    
    @call_until_valid_input
    def get_songs(songs, song_amount):
        result = []
        isAdded = False
        for index in range(song_amount):
            user_song = input(f"Название {index+1} песни: ")
            for song in songs:
                if(song[0].lower() == user_song.lower()):
                    result.append(song)
                    isAdded = True
                    break
            
            if(not isAdded):
                print("Такой песни нет")
            isAdded = False
        
        return result
    
    def count_songs_duration(songs):
        result = 0
        for song in songs:
            result += song[1]
        return round(result, 2)

    @classmethod
    def main(cls):
        violator_songs = [
            ['World in My Eyes', 4.86],
            ['Sweetest Perfection', 4.43],
            ['Personal Jesus', 4.56],
            ['Halo', 4.9],
            ['Waiting for the Night', 6.07],
            ['Enjoy the Silence', 4.20],
            ['Policy of Truth', 4.76],
            ['Blue Dress', 4.29],
            ['Clean', 5.83]]
        song_amount = cls.get_amount_of_songs()
        user_songs = cls.get_songs(violator_songs, song_amount)

        songs_duration = cls.count_songs_duration(user_songs)
        print(f"\nОбщее время звучания песен: {songs_duration}")
