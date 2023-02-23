from rest_framework import serializers
from .models import StkPushResponse

class STKPushResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StkPushResponse
        fields = '__all__'
