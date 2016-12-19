from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Category, Entry


def portfolio_index(request):
    return render(request, 'portfolio_index.html', {'categories': Category.objects.all()} )


def category_list(request, category_slug):
    categoryof = Category.objects.filter(slug=category_slug)
    entries = Entry.objects.filter(category=categoryof)
    try:
        name_of_category = categoryof[0].title
    except :
        name_of_category = "NOT FOUND"
    return render(request,'category_detail.html', {'entries':entries,'Category_name':name_of_category})


def entry_detail(request,category_slug,entry_slug):
    entry = Entry.objects.get(slug=entry_slug)
    return render(request, 'entry_detail.html', {'entry': entry})
