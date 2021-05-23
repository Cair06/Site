from django.shortcuts import render


def companies_list(request):
	n = ['Alex','Masha','Tom']
	context={
		'names': n,
	}
	return render(request, 'blog/index.html', context)