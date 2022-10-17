from django.test import TestCase

from .models import User


class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            first_name="developer",
            last_name="test",
            email="developer@gmail.com",
            username="testdeveloper",
            address="Local address",
            phone_number="+91 9990009999",
            lat=89.1111,
            lon=60.2222,
        )

    def test_first_name_label(self):
        """
        test user first name label
        """
        user = User.objects.filter(id=1).first()
        field_label = user._meta.get_field("first_name").verbose_name
        self.assertEqual(field_label, "first name")

    def test_first_name_max_length(self):
        """
        test user first name max length
        """
        user = User.objects.filter(id=1).first()
        max_length = user._meta.get_field("first_name").max_length
        self.assertEqual(max_length, 150)

    def test_last_name_label(self):
        """
        test user last name label
        """
        user = User.objects.filter(id=1).first()
        field_label = user._meta.get_field("last_name").verbose_name
        self.assertEqual(field_label, "last name")

    def test_last_name_max_length(self):
        """
        test user last name max length
        """
        user = User.objects.filter(id=1).first()
        max_length = user._meta.get_field("last_name").max_length
        self.assertEqual(max_length, 150)

    def test_email_label(self):
        """
        test user email label
        """
        user = User.objects.filter(id=1).first()
        field_label = user._meta.get_field("email").verbose_name
        self.assertEqual(field_label, "email address")

    def test_username_label(self):
        """
        test user username label
        """
        user = User.objects.filter(id=1).first()
        field_label = user._meta.get_field("username").verbose_name
        self.assertEqual(field_label, "username")

    def test_username_max_length(self):
        """
        test user username max length
        """
        user = User.objects.filter(id=1).first()
        max_length = user._meta.get_field("username").max_length
        self.assertEqual(max_length, 150)

    def test_address_label(self):
        """
        test user address label
        """
        user = User.objects.filter(id=1).first()
        field_label = user._meta.get_field("address").verbose_name
        self.assertEqual(field_label, "address")

    def test_address_max_length(self):
        """
        test user address max length
        """
        user = User.objects.filter(id=1).first()
        max_length = user._meta.get_field("address").max_length
        self.assertEqual(max_length, 500)

    def test_phone_number_label(self):
        """
        test user phone number label
        """
        user = User.objects.filter(id=1).first()
        field_label = user._meta.get_field("phone_number").verbose_name
        self.assertEqual(field_label, "phone number")

    def test_phone_number_max_length(self):
        """
        test user phone number max length
        """
        user = User.objects.filter(id=1).first()
        max_length = user._meta.get_field("phone_number").max_length
        self.assertEqual(max_length, 128)

    def test_latitude_label(self):
        """
        test user latitude label
        """
        user = User.objects.filter(id=1).first()
        field_label = user._meta.get_field("lat").verbose_name
        self.assertEqual(field_label, "lat")

    def test_logitude_label(self):
        """
        test user longitude label
        """
        user = User.objects.filter(id=1).first()
        field_label = user._meta.get_field("lon").verbose_name
        self.assertEqual(field_label, "lon")
