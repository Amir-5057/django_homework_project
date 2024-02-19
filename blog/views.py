from django.shortcuts import render
from .models import *

def index(request):
    receptes = Recept.objects.all()
    categories = Category.objects.all()


    context = {
        'title': 'Тутор по кулинарии',
        'receptes': receptes,
        'categories': categories

    }

    return render(request, 'main_page.html', context)





def category_page_view(request, category_id):
    receptes = Recept.objects.filter(category=category_id)
    trends = Recept.objects.all().order_by('-views')

    context = {
        'title': f'Категория:{Category.objects.get(id=category_id).title}',
        'receptes': receptes,
        'trends': trends

        }

    return render(request, 'category_page.html', context)





def about_cooking_page_views(request):
    context = {
        'title': 'Об кулинарий'
    }

    return render(request, 'about_cooking.html', context)


def recipe_page_views(request):
    context = {
        'title': 'Рецепт'
    }

    return render(request, 'recipe.html', context)


def types_cooking_page_views(request):
    context = {
        'title': 'Виды кулинарии'
    }
    return render(request, 'types_cooking.html', context)



# def recepte_detail_page_view(request, recepte_id):
#     recepte = Recept.objects.get(id=recepte_id),
#     breaking_news = Recept.objects.all().order_by('-created_at')
#
#     context = {
#         'title': f"Кухня: {recepte.title}",
#         'recept': recepte,
#         'breaking_news': breaking_news
#     }
#     return render(request, 'recepte_detail.html', context)
# # Create your views here.
