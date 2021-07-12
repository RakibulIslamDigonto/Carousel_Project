from django.urls import path
from .import views

app_name = 'Carosel_App'

urlpatterns = [
    #path('', views.feature, name='feature'),
    path('', views.slider, name='slider')
]
