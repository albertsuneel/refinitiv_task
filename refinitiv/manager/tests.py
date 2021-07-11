from django.test import TestCase
from .models import Rates, Branches, Manager


class RatesTestCase(TestCase):
    def setUp(self):
        Rates.objects.create(currency="USD", rate=30, spread=.20)
        Rates.objects.create(currency="CAD", rate=23.83, spread=0.40)

    def test_rates_model(self):
        usd = Rates.objects.get(currency="USD")
        cad = Rates.objects.get(currency="CAD")
        self.assertEqual(usd.rate, 30)
        self.assertEqual(cad.spread, 0.40)


class BranchesTestCase(TestCase):
    def setUp(self):
        Branches.objects.create(branch_id="STW", name="Seoul Branch", address_line1="9F S Tower",
                                address_line2="82 Saemunan-ro, Jongro-gu", address_line3="", city="Seoul",
                                zip="03185", country="South Korea", tel="+82264545400")

    def test_branches_model(self):
        branch = Branches.objects.get(branch_id="STW")
        self.assertEqual(branch.name, "Seoul Branch")
        self.assertEqual(branch.country, "South Korea")
        self.assertEqual(branch.zip, "03185")


class ManagerTestCase(TestCase):
    def setUp(self):
        Manager.objects.create(name="Suneel", email="albertsuneel420@gmail.com", password="admin@123")

    def test_manager_model(self):
        manager = Manager.objects.get(email="albertsuneel420@gmail.com")
        self.assertEqual(manager.name, "Suneel")
        self.assertEqual(manager.password, "admin@123")
