from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.views import generic

from inventory.models import Company


def company_view(request):
    company_list = Company.objects.all()
    template = loader.get_template('inventory/index.html')
    context = {
        'company_list': company_list
    }
    return HttpResponse(template.render(context, request))


def inventory_view(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    return HttpResponse("You're looking at the inventory of %s" % company.name)


