from django.test import TestCase

# Create your tests here.

from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):
    """test from page 25 of TDD with Python"""

    def root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)