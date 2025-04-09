from services.user_input import call_until_valid_input

class Task8:
    @call_until_valid_input
    def get_user_text():
        return input("Введите сообщение: ")
    
    @call_until_valid_input
    def get_shift():
        shift = int(input("Введите сдвиг: "))

        if(shift <= 0):
            raise ValueError
        
        return shift
    
    def encrypt_text(text, shift):
        ALPHABET =  "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        result = ""
        for char in text.lower():
            if(char == " "):
                result += " "
                continue
            index = ALPHABET.index(char) + shift
            if(index >= len(ALPHABET)):
                index -= len(ALPHABET)
            result += ALPHABET[index]
        return result

    @classmethod
    def main(cls):
        text = cls.get_user_text()
        shift = cls.get_shift()
        encrypted_text = cls.encrypt_text(text, shift)
        print(f"Зашифрованное сообщение: {encrypted_text}")