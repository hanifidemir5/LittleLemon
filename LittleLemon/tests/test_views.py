from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="Noodle", price=2.75,inventory=5)
        MenuItem.objects.create(title="Soup", price=1.75,inventory=15)

    def test_getall(self):
        item1 = MenuItem.objects.get(title="Noodle")
        item2 = MenuItem.objects.get(title="Soup")
        item1str = item1.get_item()
        item2str = item2.get_item()
        self.assertEqual(item1str,"Noodle : 2.75")
        self.assertEqual(item2str,"Soup : 1.75")