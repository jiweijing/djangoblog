from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def has_perm(request):
    return HttpResponse(status=200)
