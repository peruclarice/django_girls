from django.urls import path

from copyangu import views
from .views import *

urlpatterns = [
    path('home', template_home, name='home'),
    path('register', register),
    path('login/', login_user, name='login'),
]