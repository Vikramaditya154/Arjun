from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def darling(requset):
    return HttpResponse('<h1><marquee>Love u darling</marquee></h1>')
def srujana(request):
    return HttpResponse('<h1>srujana tinnava ra,vadilestunnava</h1>')
def harshad(request):
    return HttpResponse('<center><h1>Today mock is gone </h1></center>')
def Brother(request):
    return HttpResponse('<h1>HAPPY BROTHERS DAY ANNAYA</h1>')
