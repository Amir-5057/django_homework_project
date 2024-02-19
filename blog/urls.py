from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/',
         category_page_view, name='category'),
    path('about_cooking/', about_cooking_page_views, name='about_cooking'),
    path('recipe/', recipe_page_views, name='recipe'),
    path('types_cooking/', types_cooking_page_views, name='types_cooking'),
    #path('recepte/<int:recepte_id>/',
         #recepte_detail_page_view, name='recepte_detail')


]
