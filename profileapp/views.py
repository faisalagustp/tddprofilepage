from django.core.exceptions import ValidationError
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
    boxtype = ""
    if items_number == 0:
        comment = "yey, saatnya berlibur"
        boxtype = "success"
    elif items_number < 5:
        comment = "sibuk tapi santai"
        boxtype = "warning"
    else:
        comment = "oh tidak"
        boxtype = "danger"

    result = [comment,boxtype]
    return result

def todolist_page(request):
    lists = List.objects.filter()
    items = Item.objects.filter()
    result = items_to_comment(items);
    boxtype = result[1]
    comment = result[0]

    return render(request, 'todolist.html', {'comment': comment, 'lists' : lists, 'items' : items, 'boxtype' : boxtype })

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    result = items_to_comment(list_.item_set.all())
    boxtype = result[1]
    comment = result[0]
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'], list=list_)
        return redirect('/todolist/%d/' % (list_.id,))
    return render(request, 'list.html', {'list': list_ , 'comment': comment, 'boxtype' : boxtype})

def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'todolist.html', {"error": error})
    return redirect('/todolist/%d/' % (list_.id,))
