import json

from auth_user.api.serializers.registration_serializer import RegistrationSerializer
from auth_user.utils import Util
from auth_user.models import Account

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.conf import settings

import jwt

"""register_user function starts the registration process and send email for verifiying
   if the user is valid or not.
"""
def register_user(serializer, response_msg, is_staff, current_site):
    response_data = {}
    try:
        if serializer.is_valid() and not serializer.errors:
            account = None
            if is_staff:
                account = serializer.save_staff()
            else:
                account = serializer.save_customer()

            user = Account.objects.get(email=account.email)
            token = str(RefreshToken.for_user(user))

            relative_link = reverse('email_verify')
            absurl = 'http://'+ current_site + relative_link + '?token=' + token
            user_name = account.first_name + account.last_name
            email_body = 'hi' + user_name + 'Use link below to verify your name \n' + absurl
            data = {
                    'email_body': email_body, 
                    'email_subject': 'Verify your email', 
                    'email': account.email
                    }

            #Calls the send_mail method from util and util sends the email.
            Util.send_email(data)

            response_data['email'] = account.email
            response_data['response'] = response_msg
    except:
        error_data = serializer.errors
        response_data = error_data["email"]
    
    return(response_data)

"""This is the user registration view"""
@api_view(['POST',])
@permission_classes([AllowAny,])
def registration_view(request):
    data = json.loads(request.body)
    serializer = RegistrationSerializer(
                    data=data,
                )
    
    current_site = get_current_site(request).domain

    response_data = {}
    
    #For appropriate user registration, whether it is staff or customer
    if data["is_staff"] == 'True':
        msg = "New staff registration has started verify your email in order to use the app"
        is_staff = True
        response_data = register_user(serializer, msg, is_staff, current_site)

    elif data["is_staff"]  != 'True':
        msg = "New customer registration has started verify your email in order to use the app"
        is_staff = False
        response_data = register_user(serializer, msg, is_staff, current_site)
        
    return Response(response_data, status=status.HTTP_200_OK)

"""Registration view sends an email, in that email there is a link contains our 
   current site url with "email_verify" path linked with verify_email view and a temporary 
   refresh token (http://127.0.0.1:8000/api/auth_user/email_verify?token=dsfjljfl...etc.) 
   all integrated together as one url. Clicking that link directly leads to calling verify_email 
   thus gets the user registration completed."""
@api_view(['GET',])
@permission_classes([AllowAny,])
def verify_email(request):
    token = request.GET.get('token')
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
        user = Account.objects.get(id=payload['user_id'])
        user.is_active = True
        user.save()
        return Response({'success': 'email_verified succesfully'}, status=status.HTTP_200_OK)

    except jwt.ExpiredSignatureError as identifier:
        return Response({'error': 'Activation expired'}, status=status.HTTP_400_BAD_REQUEST)

    except jwt.exceptions.DecodeError as identifier:
        return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
