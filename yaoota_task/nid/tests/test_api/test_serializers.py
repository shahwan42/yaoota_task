from django.test import SimpleTestCase, tag
from rest_framework.exceptions import ValidationError

from yaoota_task.nid.api.serializers import NationalIdSerializer


@tag("nids")
class NationalIdSerializerTests(SimpleTestCase):
    def setUp(self) -> None:
        self.payload = {"id_number": "29307181300441"}

    def test_valid_data(self):
        serializer = NationalIdSerializer(data=self.payload)
        self.assertTrue(serializer.is_valid(raise_exception=True))

    def test_nid_contains_letters(self):
        self.payload["id_number"] = "2930718130044a"
        serializer = NationalIdSerializer(data=self.payload)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertEqual(serializer.errors["id_number"][0], "Digits only")

    def test_invalid_millennium(self):
        self.payload["id_number"] = "49307181300447"
        serializer = NationalIdSerializer(data=self.payload)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertEqual(serializer.errors["id_number"][0], "Invalid")

    def test_invalid_year(self):
        self.payload["id_number"] = "39307181300441"
        serializer = NationalIdSerializer(data=self.payload)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertEqual(serializer.errors["id_number"][0], "Invalid")

    def test_invalid_month(self):
        self.payload["id_number"] = "29315181300441"
        serializer = NationalIdSerializer(data=self.payload)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertEqual(serializer.errors["id_number"][0], "Invalid")

    def test_invalid_day(self):
        # Totally invalid day
        self.payload["id_number"] = "29304881300441"
        serializer = NationalIdSerializer(data=self.payload)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertEqual(serializer.errors["id_number"][0], "Invalid")

        # invalid for the month
        self.payload["id_number"] = "29304311300441"
        serializer = NationalIdSerializer(data=self.payload)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertEqual(serializer.errors["id_number"][0], "Invalid")

        # invalid in a non-leap year
        self.payload["id_number"] = "29402291300441"
        serializer = NationalIdSerializer(data=self.payload)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertEqual(serializer.errors["id_number"][0], "Invalid")

    def test_invalid_governorate(self):
        self.payload["id_number"] = "29307181000441"
        serializer = NationalIdSerializer(data=self.payload)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertEqual(serializer.errors["id_number"][0], "Invalid")

    def test_invalid_gender(self):
        self.payload["id_number"] = "29307181300401"
        serializer = NationalIdSerializer(data=self.payload)
        with self.assertRaises(ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertEqual(serializer.errors["id_number"][0], "Invalid")
