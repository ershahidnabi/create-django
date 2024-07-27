
from django.urls import path
from . import views

urlpatterns = [
    path('', views.HOME, name="home_page" ),
    path('apage/', views.About, name="about-page" )
 

]
