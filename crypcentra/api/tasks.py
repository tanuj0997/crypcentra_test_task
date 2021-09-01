from django.db import transaction
from crypcentra.celery import app
from .models import Bid


@app.task
def assign_token_to_user():
    bids = Bid.objects.all().order_by("-bidding_price", "timestamp")

    if bids:
        coin = bids.first().coin
        number_of_coins = coin.number_of_coins

        with transaction.atomic():
            for bid in bids:
                if bid.number_of_tokens <= number_of_coins:
                    bid.is_assigned = True
                    bid.save()
                    number_of_coins = number_of_coins - bid.number_of_tokens

            coin.remaning_coins = number_of_coins
            coin.save()