from django.test import TestCase
from django.contrib.messages import get_messages
from django.shortcuts import reverse
from django.contrib.auth.models import User


class TestCheckoutViews(TestCase):
    """
    Test that the checkout works properly
    """  


def test_the_checkout_page_url_exists(self):
        """
        Test that the checkout page URL exists
        """
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 302)

    def test_nothing_in_bag_error(self):
        """
        Test that an error message is shown when nothing is in the shopping bag
        """
        response = self.client.get('/checkout/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(
            str(messages[0]), "Your bag is empty")