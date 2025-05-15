class Task3:
    def can_be_poly(self, string : str):
        if len(string) <= 1:
            return False

        letters_count = {}
        for letter in string:
            if letters_count.get(letter):
                letters_count[letter] += 1
            else:
                letters_count[letter] = 1
        
        countere = 0
        for value in letters_count.values():
            if value % 2 != 0:
                countere += 1
            if countere > 1:
                return False
        return True
    