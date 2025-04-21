class Task4:
    def advanced_sum(self, *array):
        result = 0
        for num in array:
            if isinstance(num, list):
                result += self.advanced_sum(num)
            else:
                result += num
        return result
    
    def main(self):
        array = [[1, 2, [3]], [1], 3]
        print(self.advanced_sum(1, 2, 3, 4, 5))