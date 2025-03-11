from django.http import HttpResponse
from django.template import loader
from .models import Recipe

def recipes(request):
    myrecipes = Recipe.objects.all().values()
    template = loader.get_template('all_recipes.html')
    context = {
        'myrecipes': myrecipes,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    myrecipe = Recipe.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'myrecipe': myrecipe,
    }
    return HttpResponse(template.render(context, request))