from rest_framework import serializers
from fund.models import Fund

class FundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = ["id", "name", "manager", "description", "net_asset_value", "created_date", "performance"]


class FundListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fund
        fields = ["id", "name", "manager", "created_date"]
