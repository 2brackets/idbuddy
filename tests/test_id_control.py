import unittest
from src.id_control import IdControl

class TestIdControl(unittest.TestCase):

    def test_validate_person_id_valid_12(self):
        valid_id = "198904041234"
        id_control = IdControl(valid_id)
        self.assertTrue(id_control.person_id_valid)

    def test_validate_person_id_valid_10(self):
        valid_id = "8904041234"
        id_control = IdControl(valid_id)
        self.assertTrue(id_control.person_id_valid)

    def test_validate_person_id_invalid(self):
        invalid_id = "123456"
        id_control = IdControl(invalid_id)
        self.assertFalse(id_control.person_id_valid)

    def test_get_birthday_10(self):
        valid_id = "8904041234"
        id_control = IdControl(valid_id)
        self.assertEqual(id_control.get_birthday(), 19890404)

    def test_get_birthday_12(self):
        valid_id = "198904041234"
        id_control = IdControl(valid_id)
        self.assertEqual(id_control.get_birthday(), 19890404)

    def test_born_in_the_21st_century(self):
        valid_id = "1504041234"
        id_control = IdControl(valid_id)
        self.assertEqual(id_control.get_birthday(), 20150404)

    def test_get_last_four(self):
        valid_id = "198904041234"
        id_control = IdControl(valid_id)
        self.assertEqual(id_control.get_last_four(), 1234)

if __name__ == '__main__':
    unittest.main()
