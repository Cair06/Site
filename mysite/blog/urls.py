from django.urls import path
from .views import *

urlpatterns = [
	path('', companies_list, name='companies_list_url'),
	path('categories/', categories_list, name='categories_list_url'),
	path('cities/', cities_list, name='cities_list_url'),
	path('city/<int:pk>/', CityDetail.as_view(), name='city_detail_url'),
	path('company/<int:pk>/', CompanyDetail.as_view(), name='company_detail_url'),
	path('company/<int:pk>/update/', CompanyUpdate.as_view(), name='company_update_url'),
	path('company/create/', CompanyCreate.as_view(), name='company_create_url'),
	path('subcategories/', subcategories_list, name='subcategories_list_url'),
	path('subcategory/<int:pk>/', SubcategoryDetail.as_view(), name='subcategory_detail_url'),
	path('subcategory/create/', SubCategoryCreate.as_view(), name='subcategory_create_url'),
	path('subcategory/<int:pk>/update/', SubCategoryUpdate.as_view(), name='subcategory_update_url'),

]