from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import User

# Create your views here.
def Form(request):
    return render(request,'index.html')

def show(request):
    return render(request,'show.html')  

def send(request):
    if request.method == 'POST':
        ID = request.POST['ID']
        Pass = request.POST['Pass']
        User(ID = ID).save()

        msg="Data Stored Successfully"
        return render(request,"index.html",{'msg':msg})
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")   


def delete(request):
    ID = request.GET['ID']
    User.objects.filter(ID=ID).delete()
    return HttpResponseRedirect("show")

def edit(request):
    ID = request.GET['id']

    for data in User.objects.filter(ID=ID):
        
        return render(request,"edit.html",{'ID':ID})

def RecordEdited(request):
    if request.method == 'POST':
        ID = request.POST['ID']
    
        User.objects.filter(ID=ID).update()
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")        