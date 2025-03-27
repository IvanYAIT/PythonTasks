while True:
    try:
        studentsCount = int(input("Введите количество учеников: "))
    except:
        print("Это не число")
    else:
        break

grades = {3:0 ,
          4:0,
          5:0}
for grade in range(studentsCount):
    while True:
        try:
            inputGrade = int(input("Введите оценку: "))
        except:
            print("Это не число")
        else:
            if(inputGrade >= 3 and inputGrade <= 5):
                break
            else:
                print("Это число не оценка")
    
    for key in grades.keys():
        if(key == inputGrade):
            grades[key] += 1

sorted_grades = sorted(grades.items(), key=lambda item: item[1],reverse=True)
print(f"Больше всего {sorted_grades[0][0]} в классе")