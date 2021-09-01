from django.db import models


class Coins(models.Model):
    """Store coins"""

    number_of_coins = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    remaning_coins = models.IntegerField(default=0)

    class Meta:
        db_table = "coins"

    def __str__(self):
        return "{}".format(self.number_of_coins)


class Bid(models.Model):
    """Store bidding details"""

    user_id = models.IntegerField()
    number_of_tokens = models.IntegerField()
    bidding_price = models.DecimalField(max_digits=19, decimal_places=4)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        choices=([("active", "active"), ("inactive", "inactive")]),
        default="active",
        max_length=10,
    )
    is_assigned = models.BooleanField(default=False)
    coin = models.ForeignKey(Coins, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = "bidding_detail"

    def __str__(self):
        return "{}".format(self.user_id)
