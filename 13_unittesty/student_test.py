import unittest
from student import Student

class TestStudent(unittest.TestCase):
    def test_email_change(self):
        # given
        anna = Student('anna', 'snow', 4.6)
        expected_email = 'anna.snow@uam.com'
        self.assertEqual(anna.email, expected_email)
        # when "kiedy anna zmieniła nazwisko"
        anna.last = 'summer'
        new_expected_email = 'anna.summer@uam.com'
        # then
        self.assertEqual(anna.email, new_expected_email)

    def test_fullname(self):
        anna = Student('anna', 'snow', 4.6)
        expected_fullname = 'Anna Snow'
        self.assertEqual(anna.fullname, expected_fullname)

        anna.last = 'summer'
        new_expected_fullname = 'Anna Summer'

        self.assertEqual(anna.fullname, new_expected_fullname)

    def test_grant_scholarship(self):
        anna = Student('anna', 'snow', 4.6)
        anna.grant_scholarship()
        self.assertEqual(anna.scholarship, True)

        anna.student_avg = 3.6
        anna.grant_scholarship()
        self.assertEqual(anna.scholarship, False)

    def test_grant_schoolarship(self):
        anna = Student('anna', 'snow', 4.6)
        adam = Student('adam', 'kowalski', 3.5)

        self.assertIsNone(anna.scholarship)

        anna.grant_scholarship()
        self.assertTrue(anna.scholarship)

        adam.grant_scholarship()
        self.assertFalse(adam.scholarship)