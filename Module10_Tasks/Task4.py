while True:
    userInput = input("Введите последовательность: ")
    strSequence = userInput.split(' ')
    numSequence = []
    for string in strSequence:
        try:
            number = int(string)
            numSequence.append(number)
        except:
            numSequence = None
            break
    
    if(numSequence is not None):
        break

    print("Введена неправильная последовательность")



for number in numSequence:
    if(number <= 1):
        continue
    
    if(number <= 3):
        print(number)
        continue
    
    if(number % 2 == 0):
        continue

    div = 3
    isPrime = True

    while div != number:
        if(number % div == 0):
            isPrime = False
            break

        div += 2

    if isPrime:
        print(number)