class Task2:
    def is_prime(self, number):
        if(number <= 1):
            return False
        
        if(number <= 3):
            return True
        
        if(number % 2 == 0):
            return False

        div = 3

        while div != number:
            if(number % div == 0):
                return False

            div += 2

        return True

    def crypto(self, array):
        return [array[index] for index in range(len(array)) if self.is_prime(index)]
    
    def main(self):
        print(self.crypto(list(range(11))))