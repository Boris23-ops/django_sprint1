from django.shortcuts import render


def about(request):
    '''вкладка О проекте'''
    template = 'pages/about.html'
    return render(request, template)


def rules(request):
    '''вкладка Наши правила'''
    template = 'pages/rules.html'
    return render(request, template)
