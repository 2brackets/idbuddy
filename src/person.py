from datetime import datetime
from src.id_control import IdControl

class Person(object):
    def __init__(self, id_control: IdControl) -> None:
        self.id_control = id_control

    @property
    def birthday(self) -> str:
        return str(self.id_control.get_birthday())
    
    @property
    def last_four(self) -> int:
        return str(self.id_control.get_last_four())

    def get_age(self) -> int:
        birth_date = datetime.strptime(self.birthday, "%Y%m%d")
        today = datetime.today()
        age = today.year - birth_date.year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age

    def get_format_date(self) -> str:
        date_obj = datetime.strptime(self.birthday, "%Y%m%d")
        formatted_date = date_obj.strftime("%Y %B %d")
        return formatted_date

    def determine_gender(self) -> str:
        third_digit = int(self.last_four[2]) 
        if third_digit % 2 == 0:
            return "Women"
        else:
            return "Male"

    def is_birthday_today(self) -> bool:
        birth_date = datetime.strptime(self.birthday, "%Y%m%d") 
        today = datetime.today()
        return today.month == birth_date.month and today.day == birth_date.day

            

        
        