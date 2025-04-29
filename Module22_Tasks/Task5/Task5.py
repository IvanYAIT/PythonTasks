import os

class Task5:
    PATH_TO_TEXT_FILE = os.path.abspath(__file__).replace("Task5.py", "text.txt")
    PATH_TO_ANALYSIS_FILE = os.path.abspath(__file__).replace("Task5.py", "analysis.txt")
    ALPHABET = "qazwsxedcrfvtgbyhnujmikolp"

    def get_text_from_file(self):
        result = []
        with open(self.PATH_TO_TEXT_FILE, "r") as file:
            result = file.read()
        return result
    
    def count_letters(self, text):
        result = {}
        for char in text:
            for alphabet_char in self.ALPHABET:
                if(char.lower() == alphabet_char):
                    if result.get(char.lower()):
                        result[char.lower()] += 1
                    else:
                        result[char.lower()] = 1
                    break
        return result
    
    def get_analysis_from_text(self, letters):
        result = {}
        text_lenght = 0
        for amount in letters.values():
            text_lenght += amount
        for char in letters.keys():
            char_percentage = letters[char]/text_lenght
            result[char] = round(char_percentage, 3)
        result = dict(sorted(result.items(), key=lambda item : item[1], reverse=True))
        return result

    def write_analysis_to_file(self, analysis):
        with open(self.PATH_TO_ANALYSIS_FILE, "w+") as file:
            for char in analysis.keys():
                string = f"{char} {analysis[char]}\n"
                file.write(string)

    def main(self):
        text = self.get_text_from_file()
        letters = self.count_letters(text)
        analysis = self.get_analysis_from_text(letters)
        self.write_analysis_to_file(analysis)