class Task1:
    def get_four_letters_words(self, text: str):
        result = []
        for word in text.split(' '):
            current_word = ''
            counter = 0
            for letter in word:
                if letter.isalpha():
                    counter += 1
                    current_word += letter
            if counter == 4:
                result.append(current_word)
        return result