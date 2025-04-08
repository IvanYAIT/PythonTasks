from services.user_input import call_until_valid_input

class Task6:
    @call_until_valid_input
    def get_sequence():
        user_sequence = input("Введите что написано на табло: ")
        return user_sequence.split(" ")
    
    @call_until_valid_input
    def get_shift(sequnce_lenght):
        shift = int(input("Сдвиг: "))

        if(shift <= 0 or shift > sequnce_lenght):
            raise ValueError
        
        return shift
    
    def apply_shift_to_sequence(sequence, shift):
        result = []
        for _ in range(len(sequence)):
            result.append(0)
        for index in range(len(sequence)-1, -1, -1):
            newIndex = index + shift
            if(newIndex >= len(sequence)):
                newIndex = newIndex - len(sequence)
            
            result[newIndex] = sequence[index]
        return result
    
    @classmethod
    def main(cls):
        sequence = cls.get_sequence()
        shift = cls.get_shift(len(sequence))
        new_sequence = cls.apply_shift_to_sequence(sequence, shift)
        print(f"Изначальный список: {sequence}")
        print(f"Сдвинутый список: {new_sequence}")