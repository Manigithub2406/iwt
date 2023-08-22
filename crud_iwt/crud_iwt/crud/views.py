from django.shortcuts import render,redirect
from .forms import studentform
from .models import student
# Create your views here.
def create(request):
    f=studentform()
    if request.method=='POST':
        f=studentform(request.POST)
        if f.is_valid():
            f.save()
            return redirect('show')
    return render(request,'firsttemplate/home.html',{'f':f})

def show(request):
    objs=student.objects.all()
    return render(request,'firsttemplate/show.html',{'objs':objs})

def update(request,pk):
    obj=student.objects.get(id=pk)
    f=studentform(instance=obj)
    if request.method=='POST':
        f=studentform(request.POST,instance=obj)
        if f.is_valid():
            f.save()
            return redirect('show')
    return render(request,'firsttemplate/update.html',{'f':f})

def delete(request,pk):
    obj=student.objects.get(id=pk)
    if request.method=='POST':
        obj.delete()
        return redirect('show')
    
    return render(request,'firsttemplate/delete.html',{'obj':obj})

