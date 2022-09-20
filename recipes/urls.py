from django.contrib import admin
from django.urls import path

from . import views

app_name = 'recipes'
urlpatterns = [
    path('', views.site.RecipeListViewHome.as_view(), name='home'),
    path('recipes/category/<int:category_id>/',
         views.site.RecipeListViewCategory.as_view(), name='category'),
    path('recipes/<int:id>/', views.site.RecipeDetail.as_view(), name='recipe'),

]
