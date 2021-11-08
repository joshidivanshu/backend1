from django.shortcuts import render, redirect
from django.views import View
from django.http.response import HttpResponse
import json
from rest_framework.views import APIView

# Create your views here.


class NameView(APIView):
    def get(self, request):
        name = request.GET.get('name','')
        if not name:
            return HttpResponse(json.dumps("Please provide name query parameter!"))
        return HttpResponse(json.dumps(("Happy Birthday, "+str(name)+"!")))

