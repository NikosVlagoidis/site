from django.shortcuts import render


def my_homepage_view(request):
    return render(request, 'index.html')

def about_me_view(request):
    return render(request, 'about.html')
