from django.shortcuts import render,redirect
from .forms import EntryForm
from .models import entry
# Create your views here.
def insert(request):
    if request.method=="POST":
        obj=EntryForm(request.POST)
        obj.save()
        return redirect('disp')
    else:
        form=EntryForm()
        return render(request,'home.html',{'form':form})

def disp(request):
    objs=entry.objects.all().order_by('-date')
    form=EntryForm()
    return render(request,'home.html',{'objs':objs,'form':form})

def delete(request,id):
    obj=entry.objects.get(id=id)
    obj.delete()
    return redirect('disp')

def edit(request,id):
    obj=entry.objects.get(id=id)
    editid=id
    objs=entry.objects.all().order_by('-date')
    if request.method=="POST":
        obj=EntryForm(request.POST,instance=obj)
        obj.save()
        return redirect('disp')
    else:
        form=EntryForm(instance=obj)
    return render(request,'home.html',{'forme':form,'edit_id':editid,'objs':objs})
