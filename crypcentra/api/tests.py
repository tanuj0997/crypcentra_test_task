from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import datetime, timedelta
from django.utils import timezone

from .models import Coins, Bid


class BidApiTest(APITestCase):
    """
    APITest : for testing API endpoints
    """

    def setUp(self):

        self.date = timezone.now()

        self.coin = Coins.objects.create(
            number_of_coins=10, start_time=self.date, end_time=self.date + timedelta(hours = 2)
        )
        self.bid_data = {
            "user_id": 1,
            "number_of_tokens": 10,
            "bidding_price": 10,
            "coin_id": self.coin.id,
        }

    def test_create_bid(self):
        url = reverse("biding")
        data = self.bid_data
        response = self.client.post(url, data,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_bid_list(self):
        url = reverse("biding")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)