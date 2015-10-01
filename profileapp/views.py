from django.http import HttpResponse
from django.shortcuts import render, redirect
from profileapp.models import Item, List

# Create your views here.
def home_page(request) :
    return render(request, 'home.html')

def activity_page(request):
    return render(request, 'activity.html')

def items_to_comment(items):
    items_number = items.count();
    comment = ""
    if items_number == 0:
        comment = "yey, saatnya berlibur"
    elif items_number < 5:
        comment = "sibuk tapi santai"
    else:
        comment = "oh tidak"

    return comment

def todolist_page(request):
    lists = List.objects.filter()
    items = Item.objects.filter()
    comment = items_to_comment(items);
    return render(request, 'todolist.html', {'comment': comment, 'lists' : lists, 'items' : items})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    comment = items_to_comment(list_.item_set.all())
    return render(request, 'list.html', {'list': list_ , 'comment': comment})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/todolist/%d/' % (list_.id,))

def add_item(request,list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/todolist/%d/' % (list_.id,))
