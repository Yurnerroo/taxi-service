from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Car, Manufacturer


class ModelsTests(TestCase):
    def test_car_model_str(self):
        manufacturer = Manufacturer(name="Lexus", country="Japan")
        car = Car(model="MXA", manufacturer=manufacturer)
        self.assertEqual(str(car), "MXA")

    def test_driver_model_value(self):
        username = "Yura"
        password = "12345AAA"
        first_name = "Yurii"
        last_name = "Zdanevych"
        license_number = "AAA12345"

        driver = get_user_model().objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            license_number=license_number
        )

        self.assertEqual(driver.username, username)
        self.assertTrue(driver.check_password(password))
        self.assertEqual(driver.license_number, "AAA12345")

    def test_manufacturer_str(self):
        manufacturer = Manufacturer(name="Lexus", country="Japan")

        self.assertEqual(str(manufacturer), "Lexus Japan")
