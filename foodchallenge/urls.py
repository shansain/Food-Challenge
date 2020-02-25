from core import views
from django.contrib import admin
from django.urls import path, include
from core.views import SignUpClientView, SignUpBusinessView

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('select/<int:challenge_id>/', views.select, name='select'),
    path('admin/', admin.site.urls),
    path('businessSignUp/', SignUpBusinessView.as_view(), name="business-create"),
    path('clientSignUp/', SignUpClientView.as_view(), name="client-create"),
    # path('accounts/signup/', signup, name='signup'),
    path('accounts/', include("django.contrib.auth.urls")),
]
