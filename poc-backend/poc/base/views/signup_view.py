from rest_framework.views import APIView
from django.contrib.auth.models import User
from ..serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status


class View(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data["username"])
            user.set_password(request.data["password"])
            user.save()
            return Response({"user": serializer.data})
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
