from django.urls import reverse
from rest_framework.test import APIClient, APITestCase


class NationalIdCheckApiTests(APITestCase):
    def setUp(self) -> None:
        self.url = reverse("nid_api:check")
        self.client = APIClient()
        self.payload = {"id_number": "28607281100541"}

    def test_desired_scenario(self):
        resp = self.client.post(self.url, self.payload, format="json")
        self.assertEqual(resp.status_code, 200)

        expected = {
            "status": "Valid",
            "info": {
                "birth_date": "28-07-1986",
                "birth_governorate": "Damietta",
                "gender": "Female",
            },
        }
        self.assertEqual(resp.json(), expected)
