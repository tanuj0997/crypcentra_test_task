
from rest_framework import serializers
from datetime import datetime
from django.utils import timezone

from crypcentra.api.models import Coins, Bid


class BidPostSerializer(serializers.ModelSerializer):
    """
    Create user bid.
    """

    def create(self, data):
        instance = super().create(data)
        return instance

    def validate_number_of_tokens(self, number_of_tokens):
        timestamp =  timezone.now()

        try:
            coin = Coins.objects.get(id=self.initial_data["coin_id"])

            if not (timestamp >= coin.start_time and timestamp <= coin.end_time):
                raise serializers.ValidationError("Bid ended! Unable to bid for coin")

            if number_of_tokens <= 0 :
                raise serializers.ValidationError("Oops:Can bid with minimum one token")

            return number_of_tokens
        except Exception as e:
            raise serializers.ValidationError("Bid ended! Unable to bid for coin")

    class Meta:
        model = Bid
        exclude = ('timestamp',)


class GetBidSerializer(serializers.ModelSerializer):
    """
    Fetch all bids.
    """

    class Meta:
        model = Coins
        fields = "__all__"
