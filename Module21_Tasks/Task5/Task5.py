class Task5:
    def unpack_array(self, array):
        result = []
        for item in array:
            if isinstance(item, list):
                result.extend(self.unpack_array(item))
            else:
                result.append(item)
        return result
    
    def main(self):
        array = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], 
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
        unpacked_array = self.unpack_array(array)
        print(unpacked_array)