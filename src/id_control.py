from datetime import datetime

class IdControl(object):
    def __init__(self, person_id) -> None:
        self.error_message = None
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
        if length not in [10, 12]:
            self.error_message = 'ID must be 10 or 12 digits long.'
            return False
        return True

    def _modify_person_id(self, id: str) -> int:
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
        return int(self.person_id[8:12])