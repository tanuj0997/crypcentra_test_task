from django.shortcuts import render
from django.views.generic.base import TemplateView

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Bid, Coins
from .serializers import BidPostSerializer, GetBidSerializer
from .tasks import assign_token_to_user


class BidView(APIView):
    """
    Create and get bids.
    """

    def post(self, request):
        serializer = BidPostSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response_data = {"message": "Successfuly apply for token"}

            return Response(response_data, status.HTTP_201_CREATED)

    def get(self, request):

        bids = Bid.objects.prefetch_related().all()
        serializer = GetBidSerializer(bids, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class Index(TemplateView):
    """
    Show bid list on index page.
    """

    def get(self, request, *args, **kwargs):
        bids = Bid.objects.order_by("-bidding_price", "timestamp")
        coins = Coins.objects.all()
        context = {"bids": bids,"coins":coins}
        return render(request, "index.html", context=context)
