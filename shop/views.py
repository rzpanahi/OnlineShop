from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def store(request):
    return render(request, 'store.html')
