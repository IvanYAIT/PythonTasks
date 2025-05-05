class Matrix:
    data = []
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def add(self, matrix):
        matrix_data = matrix.data
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.data[i][j] += matrix_data[i][j]
    
    def substract(self, matrix):
        matrix_data = matrix.data
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.data[i][j] -= matrix_data[i][j]
    
    def multiply(self, matrix):
        matrix_data = matrix.data
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                self.data[i][j] *= matrix_data[i][j]

    def transpositions(self):
        result = []
        for i in range(self.height):
            result.append([])
            for j in range(self.width):
                result[i].append(0)

        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                result[j][i] = self.data[i][j]
        self.data = result

    def print_matrix(self):
        for i in range(len(self.data)):
            string = ''
            for j in range(len(self.data[i])):
                string += f'{self.data[i][j]} '
            print(string)