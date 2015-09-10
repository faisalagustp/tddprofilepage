from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_page(request) :
    return render(request, 'home.html')

def activity_page(request):
    return render(request, 'activity.html')

def todolist_page(request):
    return render(request, 'todolist.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })
