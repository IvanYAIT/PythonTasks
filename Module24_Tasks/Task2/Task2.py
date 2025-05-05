
class Student:
    def __init__(self, full_name, group_index, marks):
        self.full_name = full_name
        self.group_index = group_index
        self.marks = marks
    
    def get_average_mark(self):
        average_mark = 0
        for mark in self.marks:
            average_mark += mark
        if len(self.marks) > 0:
            return round(average_mark / len(self.marks), 2)
        else:
            return average_mark