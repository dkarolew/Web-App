from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("others/", views.others, name="others"),
    path("chart/", views.chart, name="chart"),
]
