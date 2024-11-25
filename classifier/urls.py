from django.urls import path
from . import views

urlpatterns = [
    path('optimize/', views.optimize_sgd, name='optimize'),
]