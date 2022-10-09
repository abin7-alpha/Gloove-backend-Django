from rest_framework import serializers

from auth_user.models import Account

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['email']
