from django.urls import path

from . import views

app_name = 'prisons'
urlpatterns = [
    path('', views.search, name='search'),
    path('<int:prison_pk>/<slug:name>/', views.prison, name="prison"),
]