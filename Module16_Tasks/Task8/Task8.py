from services.user_input import call_until_valid_input

class Task8:
    def __init__(self):
        pass

    @call_until_valid_input
    def get_amount_numbers(self):
        numbers_amount = int(input("Кол-во чисел: "))
        
        if(numbers_amount <= 0):
            raise ValueError

        return numbers_amount
    
    @call_until_valid_input
    def get_sequence(self, numbers_amount):
        result = []
        for _ in range(numbers_amount):
            user_number = int(input("Число: "))
            result.append(user_number)
        return result
    
    def is_numbere_symmetrical(self, number):
        leftPart = ""
        rightPart = ""
        word = str(number)
        for char_index in range(len(word)//2):
            leftPart += word[char_index]

        mid_index_of_word = len(word)//2 if len(word) % 2 != 0 else (len(word)//2)-1
        for char_index in range(len(word)-1, mid_index_of_word, -1):
            rightPart += word[char_index]

        return leftPart == rightPart

    def try_find_missing_number(self, left_part, right_part):
        counter = 0
        for char_index in range(len(right_part)):
            if(left_part[char_index] != right_part[char_index]):
                break
            counter += 1
        else:
            if(counter == len(right_part)):
                answer = []
                for left_char in range(counter, len(left_part)):
                    answer.append(int(left_part[left_char]))
                return answer
        return []

    def get_missing_numbers(self, sequence):
        number_str = ""
        for num in sequence:
            number_str += str(num)
        
        if(self.is_numbere_symmetrical(number_str)):
            return []
        
        answer = []
        helper = 1
        while True:
            left_part = ""
            right_part = ""
            if(helper == len(number_str)):
                for num_index in range(len(number_str)-1):
                    answer.append(int(number_str[num_index]))
                return answer[::-1]

            for number_index in range(len(number_str)):
                if(number_index < helper):
                    left_part += number_str[number_index]
                else:
                    right_part += number_str[number_index]
            
            if(len(left_part) < len(right_part)):
                helper += 1
                continue

            left_part = left_part[::-1]
            answer = self.try_find_missing_number(left_part, right_part)
            if(answer != []):
                return answer
                
            left_part_without_mid_num = ""
            for str_i in range(1, len(left_part)):
                left_part_without_mid_num += left_part[str_i]
                
            answer = self.try_find_missing_number(left_part_without_mid_num, right_part)
            if(answer != []):
                return answer

            helper += 1
    
    def main(self):
        numbers_amount = self.get_amount_numbers()
        sequence = self.get_sequence(numbers_amount)
        result = self.get_missing_numbers(sequence)
        print(f"Нужно приписать чисел:  {len(result)}")
        print(f"Сами числа: {result}")
