class Task1:
    def get_students_age(students):
        result = []
        for student_id in students.keys():
            result.append((student_id, students[student_id]["age"]))
        return result
    
    def get_students_interests_and_surnames_len(students):
        students_interests = []
        surnames_len = 0
        for student_id in students.keys():
            students_interests.extend(students[student_id]["interests"])
            surnames_len += len(students[student_id]["surname"])
        return students_interests, surnames_len
    
    @classmethod
    def main(cls):
        students = {
            1: {
                'name': 'Bob',
                'surname': 'Vazovski',
                'age': 23,
                'interests': ['biology, swimming']
            },
            2: {
                'name': 'Rob',
                'surname': 'Stepanov',
                'age': 24,
                'interests': ['math', 'computer games', 'running']
            },
            3: {
                'name': 'Alexander',
                'surname': 'Krug',
                'age': 22,
                'interests': ['languages', 'health food']
            }
        }
        students_age = cls.get_students_age(students)
        students_interests, students_surnames_len = cls.get_students_interests_and_surnames_len(students)
        print(f'Список пар "ID студента - Возраст": {students_age}')
        print(f"Полный список интересов всех студентов: {students_interests}")
        print(f"Общая длина всех фамилий студентов: {students_surnames_len}")