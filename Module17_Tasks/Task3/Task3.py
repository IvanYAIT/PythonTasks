import random as rnd

class Task3:
    def create_team():
        TEAM_SIZE  = 20
        result = []
        for _ in range(TEAM_SIZE):
            result.append(round(rnd.random() + rnd.randint(5, 10), 2))
        
        return result
    
    def find_winners(team1, team2):
        result = []
        for index in range(len(team1)):
            if(team1[index] >= team2[index]):
                result.append(team1[index])
            else:
                result.append(team2[index])
        return result
    
    @classmethod
    def main(cls):
        team1 = cls.create_team()
        team2 = cls.create_team()
        winners = cls.find_winners(team1, team2)
        print(f"Первая команда: {team1}")
        print(f"Вторая команда: {team2}")
        print(f"Победители тура: {winners}")