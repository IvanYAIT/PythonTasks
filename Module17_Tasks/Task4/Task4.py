class Task4:
    def copy_string(string):
        return string[:]
    
    def reverse_string(string):
        return string[::-1]

    @classmethod
    def main(cls):
        alphabet = 'abcdefg'
        print(f"1: {cls.copy_string(alphabet)}")
        print(f"2: {cls.reverse_string(alphabet)}")
        print(f"3: {alphabet[::2]}")
        print(f"4: {alphabet[1::2]}")
        print(f"5: {alphabet[:1:]}")
        print(f"6: {alphabet[:len(alphabet)-2:-1]}")
        print(f"7: {alphabet[3:4:]}")
        print(f"8: {alphabet[len(alphabet)-3::]}")
        print(f"9: {alphabet[3:5:]}")
        print(f"10: {alphabet[4:2:-1]}")