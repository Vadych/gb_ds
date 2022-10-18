import re

class Date:
    
    @staticmethod
    def is_leap_year(year):
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
        

    @staticmethod
    def valid_date(day, month, year):
        if month < 1 or month > 12:
            return False
        if day < 1:
            return False
        if day > 31 and month in (1, 3, 5, 7, 8, 10, 12):
            return False
        if day > 30 and month in (4, 6, 9, 11):
            return False
        if month == 2 and day > 29 and Date.is_leap_year(year):
            return False
        if month == 2 and day > 28 and not Date.is_leap_year(year):
            return False
        return True

            
    @classmethod
    def str_to_date(cls, date):
        try:
            d, m, y = re.findall(r'(\d\d?)[-\./](\d\d?)[-\./](\d{1,4})', date)[0]
        except IndexError:
            raise ValueError
        return int(d), int(m), int(y)
                    
    def __init__(self, date):
        date_set = Date.str_to_date(date)
        if not Date.valid_date(*date_set):
            raise ValueError
        self.day, self.month, self.year = date_set
        
    def __str__(self):
        return f'{self.day:02d}-{self.month:02d}-{self.year:04d}'
        
        

dat = Date('29-2-2020')

print(dat)