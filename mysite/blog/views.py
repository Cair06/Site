from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import View
from .models import Company, SubCategory
from .utils import ObjectDetailMixin, ObjectCreateMixin, ObjectUpdateMixin, ObjectDeleteMixin
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin


def companies_list(request):
    companies = Company.objects.all()
    company_is_published = "card border-dark mb-3"
    company_is_not_published = "card border-warning mb-3"
    context = {
        'companies': companies,
        'company_is_published': company_is_published,
        'company_is_not_published': company_is_not_published,
    }
    return render(request, 'blog/index.html', context)


def cities_list(request):
    cities = City.objects.all()
    return render(request, 'blog/cities_list.html', context={'cities': cities})


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/categories_list.html', context={'categories': categories})


def subcategories_list(request):
    subcategories = SubCategory.objects.all()
    return render(request, 'blog/subcategories_list.html', context={'subcategories': subcategories})


class CompanyDetail(ObjectDetailMixin, View):
    model = Company
    template = 'blog/company_detail.html'

class CompanyUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model = Company
    model_form = CompanyForm
    template = 'blog/company_update_form.html'

class CityDetail(ObjectDetailMixin, View):
    model = City
    template = 'blog/city_detail.html'


class CompanyCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = CompanyForm
    template = 'blog/company_create_form.html'
    raise_exception = True

class CompanyDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = Company
    template = 'blog/company_delete_form.html'
    redirect_url = 'companies_list_url'
    raise_exception = True


class SubcategoryDetail(ObjectDetailMixin, View):
    model = SubCategory
    template = 'blog/subcategory_detail.html'


# class City

class SubCategoryCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = SubCategoryForm
    template = 'blog/subcategory_create.html'
    raise_exception = True

class SubCategoryUpdate(LoginRequiredMixin, ObjectUpdateMixin, View):
    model= SubCategory
    model_form = SubCategoryForm
    template = 'blog/subcategory_update_form.html'
    raise_exception = True

class SubcategoryDelete(LoginRequiredMixin, ObjectDeleteMixin, View):
    model = SubCategory
    template = 'blog/subcategory_delete_form.html'
    redirect_url = 'subcategories_list_url'
    raise_exception = True