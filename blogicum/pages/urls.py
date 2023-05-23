from django.urls import path
from pages import views
from pages.apps import PagesConfig

app_name = PagesConfig.name

urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
]
