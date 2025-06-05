from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='aboutUs'),
    path('track/', views.tracker, name='trackingStatus'),
    path('contact/', views.contact, name='contact'),
    path('productview', views.prodView, name='productView'),
    path('checkout', views.checkout, name='checkout'),
    path('search', views.search, name='search')
]
