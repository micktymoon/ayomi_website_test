from django.urls import path, include
from django.conf.urls import url
from ayomi_website.authentication import views as auth_views
from django.contrib.auth import views

urlpatterns = [
    path('inscription/', auth_views.signup, name="signup"),
    path('', views.LoginView.as_view(), name='login'),
    url('^', include('django.contrib.auth.urls')),
    path('moncompte/', auth_views.account_view, name="account"),
    path('change_email/', auth_views.change_email, name='change_email'),
]
