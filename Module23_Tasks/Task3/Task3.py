import os

class Task3:
    PATH_TO_REGISTRATION_FILE = os.path.abspath(__file__).replace('Task3.py', 'registrations.txt')
    PATH_TO_GOOD_REGISTRATION_FILE = os.path.abspath(__file__).replace('Task3.py', 'registrations_good.log')
    PATH_TO_BAD_REGISTRATION_FILE = os.path.abspath(__file__).replace('Task3.py', 'registrations_bad.log')

    def get_registration_data(self):
        result = []
        with open(self.PATH_TO_REGISTRATION_FILE, 'r', encoding='utf-8') as file:
            for line in file.readlines():
                result.append(line[:-1].split(' '))
        return result
    
    def write_good_data(self, data):
        with open(self.PATH_TO_GOOD_REGISTRATION_FILE, '+a', encoding='utf-8') as good_log:
            string = ''
            for item in data:
                string += f'{item} '
            good_log.write(f'{string}\n')

    def write_bad_data(self, data):
        with open(self.PATH_TO_BAD_REGISTRATION_FILE, '+a', encoding='utf-8') as bad_log:
            string = ''
            for item in data:
                string += f'{item} '
            bad_log.write(f'{string}\n')

    def verify_registration_data(self, data):
        for reg in data:
            if(len(reg) != 3):
                self.write_bad_data(reg)
                continue
            if not reg[0].isalpha():
                self.write_bad_data(reg)
                continue
            if (reg[1].find('@') == -1 or reg[1].find('.') == -1):
                self.write_bad_data(reg)
                continue
            if not 10 < int(reg[2]) < 99:
                self.write_bad_data(reg)
                continue
            self.write_good_data(reg)
    
    def main(self):
        data = self.get_registration_data()
        self.verify_registration_data(data)
