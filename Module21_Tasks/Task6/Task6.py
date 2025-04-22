class Task6:
    def split_array(self, array):
        reference_element = array[len(array)-1]
        result = [[],[],[]]
        for item in array:
            if(item < reference_element):
                result[0].append(item)
            elif (item > reference_element):
                result[2].append(item)
            else:
                result[1].append(item)
        return result

    def fast_sort(self, array):
        splited_array = self.split_array(array)
        result = []
        if(len(splited_array[0]) > 0):
            result.extend(self.fast_sort(splited_array[0]))

        result.extend(splited_array[1])
        
        if(len(splited_array[2]) > 0):
            result.extend(self.fast_sort(splited_array[2]))
        return result
    
    def main(self):
        array = [5, 8, 9, 4, 2, 9, 1, 8]
        sorted_array = self.fast_sort(array)
        print(sorted_array)