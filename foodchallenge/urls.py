from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('select/<int:challenge_id>/', views.select, name='select'),
    path('admin/', admin.site.urls),
]