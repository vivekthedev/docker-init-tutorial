from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse("<style> body{background-color:lightblue;}</style><h1>Hello, User</h1> <h2> Welcome to my application</h2>")
