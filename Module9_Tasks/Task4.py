sentence = input("Введите текст: ")
maxLenght = 0

for word in sentence.split(" "):
    if(len(word) > maxLenght):
        maxLenght = len(word)

print(f"Длина самого длинного слова: {maxLenght}")