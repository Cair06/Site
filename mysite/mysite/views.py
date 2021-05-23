from django.http import HttpResponse



def companies_list(request):
	return HttpResponse('<h1>Hello WOrld</h1>')