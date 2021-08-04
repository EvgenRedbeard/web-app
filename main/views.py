from django.shortcuts import render

# Create your views here.
def index(request):
    databox = {
        'title': 'Main page',
    }
    return render(request, 'main/index.html', databox)

def about(request):
    return render(request, 'main/about.html')
