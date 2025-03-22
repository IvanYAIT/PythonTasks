
hours = 1
tasks = 0
wifeCalls = 0

while (hours <= 8):
    print("Час " + str(hours))
    tasks += abs(int(input("Сколько задач решит Максим?")))
    if(wifeCalls == 0):
        wifeCalls = abs(int(input("Звонит жена. Взять трубку?")))
    hours += 1

result = "За день Максим выполнил %d задач." % tasks
if(wifeCalls > 0):
    result += " Нужно зайти в магазин."

print(result)