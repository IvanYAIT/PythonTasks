while True:
    userInput = input("Введите заполненость стоил: ")
    stables = userInput.split()
    for stable in stables:
        if(stable == "a" or stable == "b"):
            continue
        
        stables = None
        break

    if(stables is not None and len(stables) == 10):
        break

    print("Введина неправильная команда")

milkPerDay = 0

for stableNumber in range(len(stables)):
    if(stables[stableNumber] == "b"):
        milkPerDay += (stableNumber+1)*2

print(f"В день производится {milkPerDay} литров молока")