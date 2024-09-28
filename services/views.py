from django.shortcuts import render
from services.models import *
from services.serializers import *
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.db.models import Prefetch
from clients.models import *


class SubscriptionView(ReadOnlyModelViewSet):
    # ? 1
    # queryset = (
    #     Subscription.objects.all()
    #     .prefetch_related("client")
    #     .prefetch_related("client__user")
    # )

    # ? 2
    queryset = Subscription.objects.all().prefetch_related(
        Prefetch("client"), Prefetch("client__user")
    )

    serializer_class = SubscriptionSerializer
