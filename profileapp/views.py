from django.http import HttpResponse
from django.shortcuts import render, redirect
from profileapp.models import Item

# Create your views here.
def home_page(request) :
    return render(request, 'home.html')

def activity_page(request):
    return render(request, 'activity.html')

def todolist_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/todolist')

    items = Item.objects.all()
    return render(request, 'todolist.html', {'items': items})
