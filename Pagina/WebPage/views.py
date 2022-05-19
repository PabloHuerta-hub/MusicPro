from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request,'index.html')


def contact(request):
    return render(request,'contact.html')


def blog(request):
    return render(request,'blog.html')

def product(request):
    url = "http://127.0.0.1:8000/api/productos/"
    response = requests.get(url, auth = ('admin', '1234'))
    producto = response.json()
    return render(request,'product.html', context={'producto':producto})

def about(request):
    return render(request,'about.html')