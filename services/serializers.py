from rest_framework import serializers
from .models import *


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    # plan = PlanSerializer()

    client_name = serializers.CharField(source="client.company_name")
    email = serializers.CharField(source="client.user.email")

    class Meta:
        model = Subscription
        fields = ["id", "plan_id", "client_name", "email"]
