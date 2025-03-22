print("Замечательные числа в диапазоне двузначных:")
for number in range(1000):
    strNumber = str(number)
    if(len(strNumber) != 2):
        continue

    helper = 1

    for char in list(strNumber):
        helper *= int(char)
    helper *=3
    
    if(helper == number):
        print(number)