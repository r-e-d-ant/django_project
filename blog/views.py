from django.shortcuts import render
from django.http import HttpResponse

# Views
def home(request):
	HttpResponse('<h1>Hello, World! This is a home page<h1/>')
