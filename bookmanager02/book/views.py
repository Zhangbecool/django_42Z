from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
            'log': '都有网特',
            'name': 'zhangbecool',
            
            }
    return render(request, 'book/index.html', context)
