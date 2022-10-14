from django.urls import path
from .views import *


urlpatterns = [
    path('', mainPage, name='home'),
    path('news/', list_news, name='news'),
    path('about/', about, name='about'),
    path('categories/<int:categories_id>/', categories, name='categories'),
]