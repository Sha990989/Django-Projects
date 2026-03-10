from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def java(request):
    temp='''
<html><body bgcolor=red>
<h1>Welcome to Java Programming</h1>
<marquee>We are from IC batch </marquee>
</body></html>
'''
    return HttpResponse(temp)

