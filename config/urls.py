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
from django.conf.urls import url
from thelibrary import views
#from api.library.v1.books.views.books_view import BooksView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/', views.index, name='index')


]
"""     url(
        r'^library/?$',
        BooksView.as_view(),
        name='books_list_view'

    ), """

""" 
    path('library/nearest/', views.nearest, name='nearest'),
    path('library/nearest/<int:lat>', views.nearest, name='nearest'),
    path('library/<str:pk>/', views.DeaDetailView.as_view(), name='detail'),
    path('create/', views.create, name='create'),

    path('library/orderByLocality',
         views.OrderByLocality.as_view(), name='orderByLocality'),
    path('library/orderByPostalCode',
         views.OrderByPostalCode.as_view(), name='orderByPostalCode') """