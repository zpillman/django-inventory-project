"""django_inventory URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from inventory import views

app_name = 'inventory'
urlpatterns = [
    # ex: /inventory/
    path('', views.company_view, name='index'),
    # ex: /inventory/1
    path('<int:company_id>/', views.inventory_view, name='inventory_view'),
    path('<int:company_id>/part/<int:part_id>/', views.edit_part_view, name='edit_part_view'),
    path('<int:company_id>/product/<int:product_id>/', views.edit_product_view, name='edit_product_view')
]

