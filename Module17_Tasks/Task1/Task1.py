from services.user_input import call_until_valid_input

class Task1:
    

    @call_until_valid_input
    def get_user_text():
        return input("Введите текст: ")
    
    def find_all_vowels(text):
        VOWELS = ['а', 'о', 'э', 'е', "и", 'ы', 'у', 'ё', 'ю', 'я']
        result= []

        for char in text:
            for vowel in VOWELS:
                if(char.lower() == vowel):
                    result.append(char)
        return result

    @classmethod
    def main(cls):
        text = cls.get_user_text()
        text_vowels = cls.find_all_vowels(text)

        print(f"Список гласных букв: {text_vowels}")
        print(f"Длина списка:  {len(text_vowels)}")
