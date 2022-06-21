from django.urls import path
from . import views
from .dash_apps.test_apps import plot

urlpatterns = [
    path('scatterplot/', views.scatter_plot, name="worker.scatter_plot"),
]


