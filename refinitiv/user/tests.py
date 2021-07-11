from django.test import TestCase
from datetime import datetime
from.models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(transaction_id="sdsdss877s990s", timestamp=datetime.now(), name="Suneel", position="Buy", currency="USD",
                            fx_rate_hq=30.1, fx_rate_spread=0.02, amount=5218,branch_id="UCL",  comments="---",
                            status=1)

    def test_user_model(self):
        data = User.objects.get(transaction_id="sdsdss877s990s")
        self.assertEqual(data.name, "Suneel")
        self.assertEqual(data.branch_id, "UCL")
        self.assertEqual(data.position, "Buy")
        self.assertEqual(data.amount, str(5218))

