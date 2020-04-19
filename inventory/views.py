from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic

from inventory.models import Company, Part, Product


def company_view(request):
    company_list = Company.objects.all()
    template = loader.get_template('inventory/index.html')
    context = {
        'company_list': company_list
    }
    return HttpResponse(template.render(context, request))


def inventory_view(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    parts_list = Part.objects.filter(company_id=company_id)
    products_list = Product.objects.filter(company_id=company_id)
    template = loader.get_template('inventory/inventory.html')
    context = {
        'company': company,
        'parts_list': parts_list,
        'products_list': products_list
    }
    return HttpResponse(template.render(context, request))


def edit_part_view(request, company_id, part_id):
    company = get_object_or_404(Company, pk=company_id)
    part = get_object_or_404(Part, pk=part_id)
    template = loader.get_template('inventory/edit_part.html')
    context = {
        'company': company,
        'part': part
    }
    return HttpResponse(template.render(context, request))


def edit_product_view(request, company_id, product_id):
    company = get_object_or_404(Company, pk=company_id)
    product = get_object_or_404(Product, pk=product_id)
    template = loader.get_template('inventory/edit_product.html')
    context = {
        'company': company,
        'product': product
    }
    return HttpResponse(template.render(context, request))

