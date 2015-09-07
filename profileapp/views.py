from django.shortcuts import render

# Create your views here.
def home_page(request) :
    return render(request, 'home.html')

def activity_page(request):
    return render(request, 'activity.html')
