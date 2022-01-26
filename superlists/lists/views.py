from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Item, List


# Create your views here.
def home_page(request):
    return render(request, 'lists/home.html')


def view_list(request, pk):
    list_ = List.objects.get(pk=pk)
    return render(request, 'lists/list.html', {
        'list': list_
    })


def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')


def add_item(request, pk):
    list_ = List.objects.get(pk=pk)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/list/{list_.id}/')
