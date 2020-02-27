from core import views
from django.contrib import admin
from django.urls import path, include
from core.views import SignUpClientView, SignUpBusinessView


urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('select/<int:challenge_id>/', views.select, name='select'),
    path('admin/', admin.site.urls),
    path('business-sign_up/', SignUpBusinessView.as_view(), name="business_create"),
    path('client-sign_up/', SignUpClientView.as_view(), name="client_create"),
    path('profile/<int:client>', views.profile, name="profile"),
    path('about_me/', views.about_me, name="about_me"),
    path('accounts/', include("django.contrib.auth.urls")),
]
