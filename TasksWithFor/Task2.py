annualIncome = 0

for month in range(12):
    while True:
        try:
            annualIncome += int(input(f"Введите {month+1} месяца зарплату: "))
        except:
            print("Это не число")
        else:
            break

averageAnnualSalary = annualIncome//12
print(f"средняя зарплата за год: {averageAnnualSalary}")