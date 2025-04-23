import os

class Task4:
    PATH_TO_FIRST_TOUR_FILE = os.path.abspath(__file__).replace("Task4.py", "first_tour.txt")
    PATH_TO_SECOND_TOUR_FILE = os.path.abspath(__file__).replace("Task4.py", "second_tour.txt")

    def get_data_from_first_tour(self):
        with open(self.PATH_TO_FIRST_TOUR_FILE, 'r') as file:
            passing_points = file.readline()
            participants = []
            for line in file:
                participants.append(line.split(" "))
        return int(passing_points), participants
    
    def find_winners(self, passing_points, participants):
        result = {}
        for participant in participants:
            if(passing_points < int(participant[2])):
                full_name = f"{participant[1][0:1]}. {participant[0]}"
                result[full_name] = int(participant[2])
        result = dict(sorted(result.items(), key=lambda item : item[1], reverse=True))
        return result
    
    def write_winner_to_file(self, winners):
        with open(self.PATH_TO_SECOND_TOUR_FILE, "w+") as file:
            index = 1
            for winner in winners.keys():
                string = f"{index}) {winner} {winners[winner]}\n"
                file.writelines(string)
                index += 1

    def main(self):
        passing_points, participants = self.get_data_from_first_tour()
        winners = self.find_winners(passing_points, participants)
        self.write_winner_to_file(winners)
        