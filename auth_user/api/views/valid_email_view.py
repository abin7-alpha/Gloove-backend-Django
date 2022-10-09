import json

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from auth_user.api.serializers.email_serializer import EmailSerializer

"""This view is for live verification of email."""
@api_view(['GET',])
@permission_classes([AllowAny])
def is_valid_email(request):
    data = json.loads(request.body)
    serializer = EmailSerializer(data=data)
    if serializer.is_valid():
        return Response({"error": "Account with this email does not exists."}, status=status.HTTP_404_NOT_FOUND)
    else:
        error = serializer.errors
        return Response({"success": error}, status=status.HTTP_200_OK)
