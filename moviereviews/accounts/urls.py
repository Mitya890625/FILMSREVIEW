from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('signupaccount/', views.signupaccount,
        name='signupaccount'),
    path('logout/', views.logoutaccount,
        name='logoutaccount'),
    path('login/', csrf_exempt(views.loginaccount),
        name='loginaccount'),
]