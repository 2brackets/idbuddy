from datetime import datetime
import unittest
from src.person import Person
from src.id_control import IdControl

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.valid_id = "198904041234"  
        self.id_control = IdControl(self.valid_id)
        self.person = Person(self.id_control)

    def test_get_format_date(self):
        self.assertEqual(self.person.get_format_date(), "1989 April 04")

    def test_get_age(self):
        age = self.person.get_age()
        self.assertIsInstance(age, int)
        self.assertGreaterEqual(age, 0)

    def test_determine_gender_women(self):
        id_control = IdControl("8904041244")
        person = Person(id_control)
        self.assertEqual(person.determine_gender(), "Women")

    def test_determine_gender_male(self):
        self.assertEqual(self.person.determine_gender(), "Male")

    def test_is_birthday_today(self):
        today_date = datetime.today()
        ten_years_ago = today_date.replace(year=today_date.year - 10)
        formatted_date = ten_years_ago.strftime('%Y%m%d')
        id_control = IdControl(f"{formatted_date}1234")
        person = Person(id_control)
        self.assertTrue(person.is_birthday_today())

if __name__ == '__main__':
    unittest.main()
