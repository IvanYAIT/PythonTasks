acceptedPersonCount = 0

for person in range(1, 11):
    personWord = input(f"{person}-й человек выкрикнул: ").lower()
    if(personWord == "карамба"):
        acceptedPersonCount += 1

print(f"На борт попало {acceptedPersonCount} человек")