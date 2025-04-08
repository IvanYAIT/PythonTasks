class Task2:


    def split_into_two_groups(group):
        oddIndexGroup = []
        evenIndexGroup = []
        for index in range(len(group)):
            if((index+1) % 2 == 0):
                evenIndexGroup.append(group[index])
            else:
                oddIndexGroup.append(group[index])
        return (oddIndexGroup, evenIndexGroup)
    
    @classmethod
    def main(cls):
        tournament_participants = [
            "Артемий",
            "Борис",
            "Влад",
            "Гоша",
            "Дима",
            "Евгений",
            "Женя",
            "Захар",
            "Игорь",
            "Константин",
            "Максим",
            "Никита",
            "Павел",
            "Роман"
        ]
        spliteGroup = cls.split_into_two_groups(tournament_participants)
        print(f"Первая группа:  {spliteGroup[0]}")
        print(f"Вторая группа:  {spliteGroup[1]}")