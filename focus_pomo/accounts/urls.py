<<<<<<< HEAD
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

=======
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
>>>>>>> 6f35e699ff10e261826416ea7ca6d108e01df272

app_name = 'accounts'

urlpatterns = [
<<<<<<< HEAD
    path('sign_up', views.SignUp.as_view(), name='sign_up'),
=======
    path('sign_up/', views.SignUp.as_view(), name='sign_up'),
>>>>>>> 6f35e699ff10e261826416ea7ca6d108e01df272
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
