import json

from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from auth_user.models import Account

#The login view
@api_view(['POST',])
@permission_classes([AllowAny])
def login_view(request):
    data = json.loads(request.body)
    email = data['email']
    password = data['password']
    try:
        user = Account.objects.get(email=email)
    except:
        return Response({"error": "Account with this email does'nt exist."}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        authorize = authenticate(email=email, password=password)
        if authorize == None:
            raise Exception("Incorrect password")
    except Exception as error:
        return Response({"error": "Incorrect password"}, status=status.HTTP_401_UNAUTHORIZED)
    
    if authorize:
        data = {}
        if user.is_active:
            data['email'] = user.email
            data['is_logged'] = 'True'
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Verification is pending.'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return ValidationError({"error": "Account does'nt exist."})
