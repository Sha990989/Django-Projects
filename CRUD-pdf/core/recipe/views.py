# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe

def recipes(request):
    if request.method == 'POST':
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        Recipe.objects.create(
            recipe_image=recipe_image,
            recipe_name=recipe_name,
            recipe_description=recipe_description,
        )
        return redirect('/')

    queryset = Recipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains=request.GET.get('search'))

    context = {'recipes': queryset}
    return render(request, 'recipes.html', context)


def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    recipe.delete()
    return redirect('/')


def update_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if request.method == 'POST':
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        recipe.recipe_name = recipe_name
        recipe.recipe_description = recipe_description
        if recipe_image:
            recipe.recipe_image = recipe_image
        recipe.save()
        return redirect('/')

    context = {'recipe': recipe}
    return render(request, 'update_recipe.html', context)

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def generate_pdf(request):
    template = get_template('pdf_template.html')
    html = template.render({'title': 'My PDF', 'message': 'Hello from Django PDF'})
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="report.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

from django.shortcuts import render
def home(request):
    return render(request, 'home.html')
