from rest_framework import serializers

from auth_user.models import Account

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['first_name','last_name','email', 'password']
        extra_kwargs = {
                'password': {'write_only': True}
        }

    def save_staff(self):
        account = Account(
                    email=self.validated_data['email'],
                    first_name=self.validated_data['first_name'],
                    last_name=self.validated_data['last_name'],
                    is_staff=True
                )

        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        return account
    
    def save_customer(self):
        account = Account(
                    email=self.validated_data['email'],
                    first_name=self.validated_data['first_name'],
                    last_name=self.validated_data['last_name'],
                )

        password = self.validated_data['password']
        account.set_password(password)
        account.save()
        return account
