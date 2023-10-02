from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request=request, template_name='recipes/pages/home.html')


def recipe(request, id):
    return render(request=request, template_name='recipes/pages/home.html')
