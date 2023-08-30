"""views"""
from django.shortcuts import render


def home_view(request):
    """renderizando tela home"""
    return render(request, 'app/home.html')
