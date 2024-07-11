from rest_framework.views import APIView
from ..serializers import UserSerializerWithoutPass
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404


class View(APIView):
    def post(self, request):
        user = get_object_or_404(User, username=request.data["username"])
        if not user.check_password(request.data['password']):
            return Response({"detail": "Not found!"}, status.HTTP_404_NOT_FOUND)
        seralizer = UserSerializerWithoutPass(instance=user,)
        return Response({"user": seralizer.data})
