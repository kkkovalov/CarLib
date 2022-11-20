from django.urls import path
from cardbAPI import views

urlpatterns = [
    path('manufacturer/', views.manufacturerApi)
]
