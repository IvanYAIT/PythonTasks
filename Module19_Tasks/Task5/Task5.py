from services.user_input import call_until_valid_input

class Task5:
    @call_until_valid_input
    def get_amount_of_words():
        amount = int(input("Введите количество пар слов: "))

        if(amount <= 0):
            raise ValueError("Число должно быть больше нуля")
        
        return amount

    @call_until_valid_input
    def user_word_dict(amount_of_words):
        user_dict = dict()
        for index in range(amount_of_words):
            user_words = input(f"{index+1} пара: ").split(" - ")
            user_dict[user_words[0].lower()] = user_words[1]
        return user_dict
    
    @call_until_valid_input
    def find_word_synonym(dict_of_words):
        user_word = input("Введите слово: ")
        result = dict_of_words.get(user_word.lower())
        if(result is None):
            raise ValueError("Такого слова нет в словаре")
        return result
    
    @classmethod
    def main(cls):
        amount = cls.get_amount_of_words()
        dict_of_words = cls.user_word_dict(amount)
        word = cls.find_word_synonym(dict_of_words)
        print(f"Синоним: {word}")
        