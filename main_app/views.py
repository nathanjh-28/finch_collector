from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

class Finch:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

finches = [
    Finch('moishe', 'breed1', 'this is moishes descrip', 2),
    Finch('cocoa', 'breed2', 'this is cocoas descrip', 3),
    Finch('steve finch', 'breed3', 'this is steves descrip',4),
]


def home(request):
    return HttpResponse('<h1>Hello （・⊝・）</h1>')

def about(request):
    return render(request,'about.html')

def index(request):
    context = {
        'finches': finches,
    }
    return render(request, 'index.html', context)