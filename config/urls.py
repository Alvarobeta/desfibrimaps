"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from desfibrimaps.views import Deas
from desfibrimaps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('devices/', views.index, name='index'),
    path('devices/nearest/', views.nearest, name='nearest'),
    path('devices/nearest/<int:lat>', views.nearest, name='nearest'),
    path('devices/<str:pk>/', views.DeaDetailView.as_view(), name='detail'),
    path('create/', views.create, name='create'),

    path('devices/orderByLocality',
         views.OrderByLocality.as_view(), name='orderByLocality'),
    path('devices/orderByPostalCode',
         views.OrderByPostalCode.as_view(), name='orderByPostalCode')
]