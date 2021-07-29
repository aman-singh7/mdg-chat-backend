import json
import random

from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class DemoView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        content = {'message': 'Hello! This is a Demo!'}
        return Response(content)


def new(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        salt = '-' + str(random.random())[2:]
        
        username = name + salt
        password = str(random.random())[2:]
        content = {'username': username,
                   'password': password}
        
        User.objects.create_user(username=username, email=username + '@example.com', password=password)
        return HttpResponse(json.dumps(content))
