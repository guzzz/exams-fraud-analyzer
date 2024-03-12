
from django.test import TestCase
from persons.models import Person


class PersonUnitTest(TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(PersonUnitTest, cls).setUpClass()
        print("======================================================================")
        print("==> INITIALIZING Person MODEL Tests...")
        print("======================================================================")

    def test_model_success(self):
        print("==> create_person SUCCESS CASE")
        person = Person(name='Bruce', surname='Wayne', age=32)
        self.assertEqual(person.surname, 'Wayne')
        print("----------------------------------------------------------------------")

    def test_model_error(self):
        print("==> create_person FAIL CASE")
        with self.assertRaises(Exception):
            person = Person(occupation='Programmer', surname='El', age=31)
        print("----------------------------------------------------------------------")
