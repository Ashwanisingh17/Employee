from mysite.apps import MysiteConfig
from mysite import views
from django.urls import path

app_name = MysiteConfig.name


urlpatterns = [
    path('', views.home, name='home' ),
   
]
