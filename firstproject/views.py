from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("My 1st project on django")
def demo(request):
    return HttpResponse("Hurray!")