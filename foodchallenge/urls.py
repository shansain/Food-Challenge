from core import views
from django.contrib import admin
from django.urls import path, include
from core.views import signup
urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('select/<int:challenge_id>/', views.select, name='select'),
    path('admin/', admin.site.urls),
    path('accounts/signup/', signup, name='signup'),
    path('accounts/', include("django.contrib.auth.urls")),
]

