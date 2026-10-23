
import unittest
from app.app import app


class TestITSMAPI(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_health_endpoint(self):
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "healthy")

    def test_home_endpoint(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json()["application"],
            "ITSM Ticket API"
        )

    def test_tickets_endpoint(self):
        response = self.client.get("/tickets")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 2)


if __name__ == "__main__":
    unittest.main()