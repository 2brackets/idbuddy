from datetime import datetime

class IdControl(object):
    def __init__(self, person_id: str, swedish_id: bool) -> None:
        self.error_message = None
        self.swedish_id = swedish_id
        self.person_id_valid = self._validate_person_id(person_id)
        if self.person_id_valid:
            self.person_id = self._modify_person_id(person_id)
        else:
            self.person_id = None

    def _validate_person_id(self, id: str) -> bool:
        if not id.isdigit():
            self.error_message = 'ID can only contain numbers'
            return False
        length = len(id)
        if length not in [6, 8] and not self.swedish_id:
            self.error_message = 'Date must be 6 or 8 digits long.'
        if length not in [10, 12] and self.swedish_id:
            self.error_message = 'ID must be 10 or 12 digits long.'
            return False
        if length == 6:
            date_str = id
            century = '19'
        elif length == 8:
            date_str = id
            century = ''    
        elif length == 10:
            date_str = id[:6]
            century = '19'  
        else:
            date_str = id[:8]
            century = ''  
        try:
            birth_date = datetime.strptime(century + date_str, '%Y%m%d') 
        except ValueError:
            self.error_message = 'This is not a valid ID (invalid date).'
            return False
        return True

    def _modify_person_id(self, id: str) -> int:
        if not self.swedish_id:
            id = f'{id}0000'
        if len(id) == 10:
            first_two_digits = int(id[:2])
            year_now = datetime.now().year % 100
            if first_two_digits > year_now:
                return f"19{id}"
            else:
                return f"20{id}"
        else:
            return id
            
    def get_birthday(self) -> int:
        return int(self.person_id[:8])
    
    def get_last_four(self) -> int:
        if self.swedish_id:
            return int(self.person_id[8:12])
        else:
            return None