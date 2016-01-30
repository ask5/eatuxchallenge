from django.test import TestCase
from eat.models import EarningsPage
from . import *


# Create your tests here.
class EarningsPageTestCase(TestCase):
    def test_earnings_pages(self):
        for k, v in child_earnings_meta_data.items():
            print(v['title'])
