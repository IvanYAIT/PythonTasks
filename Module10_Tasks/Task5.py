while True:
    userInput = input("Введите последовательность натуральных чисел: ")
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

currentNumber = 0
sumOfNumber = 0
for number in strSequence:
    currnetSum = 0
    for num in number:
        currnetSum += int(num)
    
    if(currnetSum > sumOfNumber):
        sumOfNumber = currnetSum
        currentNumber = int(number)

print(f"число {currentNumber} имеет самую большую сумму цифр - {sumOfNumber}")