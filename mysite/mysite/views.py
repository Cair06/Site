from django.shortcuts import redirect

def redirect_blog(request):
    return redirect('companies_list_url', permanent=True)