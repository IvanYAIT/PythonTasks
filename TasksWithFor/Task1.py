passengerIds = []

for passengers in range(11):
    while True:
        try:
            id = int(input("Введите номер пассажира: "))
        except:
            print("Это не число")
        else:
            break
    passengerIds.append(id)

correctPassengersCount = 0
for id in passengerIds:
    if(id >= 0 and id%2 == 0):
        correctPassengersCount += 1

print(f"Количество корректных номеров: {correctPassengersCount}")