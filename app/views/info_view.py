from django.shortcuts import render


def info_view(request):
    """renderizando tela home"""
    show_footer = True
    context = {'show_footer': show_footer}
    return render(request, 'app/info.html', context)
