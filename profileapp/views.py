from django.http import HttpResponse
from django.shortcuts import render, redirect
from profileapp.models import Item

# Create your views here.
def home_page(request) :
    return render(request, 'home.html')

def activity_page(request):
    return render(request, 'activity.html')

def todolist_page(request):
    return render(request, 'todolist.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/todolist/the-only-list-in-the-world/')
