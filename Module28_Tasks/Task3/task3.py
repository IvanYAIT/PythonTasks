class Date():
    day = None
    month = None
    year = None

    __month_days = {
        1: 31, 2: 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
        }
    
    @classmethod
    def is_valid(cls, str_date : str):
        splited_str = str_date.split('-')
        date = []
        try:
            for string in splited_str:
                date.append(int(string))
        except:
            return False
        if 1 > date[1] or date[1] > 12:
            return False
        if date[2] < 0:
            return False
        if 0 > date[0] or date[0] > cls.__month_days[date[1]]:
            return False
        return True

    @classmethod
    def from_string(cls, str_date : str):
        splited_str = str_date.split('-')
        if not cls.is_valid(str_date):
            return
        
        cls.day = int(splited_str[0])
        cls.month = int(splited_str[1])
        cls.year = int(splited_str[2])
        return cls()
    
    def __str__(self):
        return f'День: {self.day} Месяц: {self.month} Год: {self.year}'
