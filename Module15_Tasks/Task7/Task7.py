from services.user_input import call_until_valid_input

class Task7:
    @call_until_valid_input
    def get_user_word():
        return input("Введите слово: ")
    
    def is_word_palindrome(word):
        leftPart = ""
        rightPart = ""
        for char_index in range(len(word)//2):
            leftPart += word[char_index]

        mid_index_of_word = len(word)//2 if len(word) % 2 != 0 else (len(word)//2)-1
        for char_index in range(len(word)-1, mid_index_of_word, -1):
            rightPart += word[char_index]

        return leftPart == rightPart
    
    @classmethod
    def main(cls):
        word = cls.get_user_word()
        if(cls.is_word_palindrome(word)):
            print("Слово является палиндромом")
        else:
            print("Слово не является палиндромом")