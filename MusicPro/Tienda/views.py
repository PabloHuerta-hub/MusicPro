from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
def index(request):
    return render(request,'index.html')


def contact(request):
    return render(request,'contact.html')


def blog(request):
    return render(request,'blog.html')

def product(request):
    return render(request,'product.html')

def about(request):
    return render(request,'about.html')