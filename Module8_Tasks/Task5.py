educationalGrant = None
expenses = None

while True:
    try:
        if(educationalGrant is None):
            educationalGrant = int(input("Введите ежемесячную стипендию: "))
        
        if(educationalGrant < 0):
            educationalGrant = None
            print("Cтипендия не может быть отрицательной")
            continue

        if(expenses is None):
            expenses = int(input("Введите ежемесячные расходы: "))

        if(expenses <= 0):
            expenses = None
            print("Ежемесячные расходы не может быть отрицательной или быть нулём")
            continue

        break
    except:
        print("Какие-то данные введены не правильно")

missingMoney = 0
for month in range(1, 11):
    if(educationalGrant - expenses < 0):
        print(f"{month}-й месяц: траты {expenses} рублей, не хватает {expenses - educationalGrant} рублей.")
    else:
        print(f"{month}-й месяц: траты {expenses} рублей, осталось {educationalGrant - expenses} рублей.")
    missingMoney += educationalGrant - expenses
    expenses += int(expenses * 0.03)

if(missingMoney < 0):
    print(f"Сумма денег, которую необходимо получить у родителей: {missingMoney * -1} рублей.")
else:
    print(f"Ты достаточно самостаятелен что тебе не нужны денеги от родителей и у тебя осталось {missingMoney} рублей.")