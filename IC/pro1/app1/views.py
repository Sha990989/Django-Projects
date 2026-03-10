from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def cr(request):
    return HttpResponse("I am CR of IC batch")

def lr(request):
    return HttpResponse("<h1>I am LR of IC batch</h1")

def fun_t1(request):
    template=loader.get_template('t1.html')
    return HttpResponse(template.render())

def fun_t2(request):
    template=loader.get_template('t2.html')
    return HttpResponse(template.render())

def index(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())
