width = None
height = None

while True:
    try:
        if(width is None):
            width = int(input("Ширина рамки: "))

        if(width <= 0):
            width = None
            print("Ширина должны быть больше нуля")
            continue
        
        if(height is None):
            height = int(input("Высота рамки: "))

        if(height <= 0):
            height = None
            print("Высота должны быть больше нуля")
            continue

        break
    except:
        print("Некоторые данные введены неправильно")

for rowNumber in range(height):
    row = '|' + ' ' * width + '|'
    if(rowNumber == 0 or rowNumber == height-1):
        row = '|' + '-' * width + '|'
    
    print(row)