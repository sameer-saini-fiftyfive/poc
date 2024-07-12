from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from ..serializers import UserSerializerWithoutPass
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404


class BearerTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'


class View(APIView):
    authentication_classes = [BearerTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        token = Token.objects.get(key=request.auth)
        user = get_object_or_404(User, username=token.user.username)
        serializer = UserSerializerWithoutPass(instance=user)
        return Response({"message": "This is home data!!", "user": serializer.data})
