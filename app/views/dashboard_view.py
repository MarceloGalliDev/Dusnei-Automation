"""views"""
from django.shortcuts import render


def dashboard_view(request):
    """renderizando tela dashboard"""
    show_footer = False
    context = {'show_footer': show_footer}
    return render(request, 'app/dashboard.html', context)
