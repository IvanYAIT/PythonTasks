bankDeposit =  int(input("Вклад в банке: "))
percent = int(input("Процент: "))
depositThreshold = int(input("Порог вклада: "))
years = 0
newDeposit = bankDeposit

while (bankDeposit < depositThreshold):
    newDeposit += int(bankDeposit * (percent/100))
    years += 1
    print(f"{years} год. {bankDeposit} + {percent}% = {newDeposit}")
    bankDeposit = newDeposit

print(f"Кол-во лет для достижения порога: {str(years)}")