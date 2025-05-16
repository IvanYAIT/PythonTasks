class Task4:
    def decrypt(self, string : str):
        letter_amount = {}
        letters = list(filter(lambda char : char.lower().isalpha(), string))
        for letter in letters:
            letter = letter.lower()
            if letter_amount.get(letter):
                letter_amount[letter] += 1
            else:
                letter_amount[letter] = 1
        unique_letters = list(filter(lambda letter : letter == 1, letter_amount.values()))
        return len(unique_letters)
