from django.shortcuts import render

# Landing page: links to every exercise entry point.
LINKS = [
    {'id': 'ex00', 'name': 'index', 'desc': 'a simple non-django page', 'url': '/ex00/'},
    {'id': 'ex01', 'name': 'templates', 'desc': 'django templates & static', 'url': '/ex01/templates/'},
    {'id': 'ex01', 'name': 'django', 'desc': 'a proper django page', 'url': '/ex01/django/'},
    {'id': 'ex01', 'name': 'display', 'desc': 'template inheritance', 'url': '/ex01/display/'},
    {'id': 'ex02', 'name': 'form', 'desc': 'a form with history', 'url': '/ex02/'},
    {'id': 'ex03', 'name': 'shades', 'desc': 'fifty shades of bic', 'url': '/ex03/'},
]


def home(request):
    return render(request, 'index.html', {'links': LINKS})
