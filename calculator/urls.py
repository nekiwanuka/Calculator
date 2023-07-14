from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'calculator'

urlpatterns = [
    path('', views.calculator, name='calculator'),
    path('calculate/', views.calculate, name='calculate'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)