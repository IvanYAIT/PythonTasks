class Task1:
    def get_sequence(self, *args : int):
        result = []
        for num in args:
            result.append(num ** 2)
        return result
    
    def generate_sequence(self, *args : int):
        for num in args:
            yield num ** 2
    
    def generate_sequence_expression(self, *args : int):
        return (num ** 2 for num in args)