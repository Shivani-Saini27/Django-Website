from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'does': "Milk, green tea, pulses"
    }
    return render(request, 'home.html', context)
    #return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page") 

def projects(request):
    return HttpResponse("my work") 

def blog(request):
    #return HttpResponse("checkout my blogs here") 
    return render(request, 'blog.html')

def contacts(request):
    return render(request, 'contacts.html')
    #return HttpResponse("details to reachout to me") 

def todo(request):
    return render(request, 'todo.html')
