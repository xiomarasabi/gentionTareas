from django.shortcuts import render, redirect
from .models import Tarea 
from .forms import TareaForm
# Create your views here.

def listar(request):
   tareas = Tarea.objects.all()
   return render(request,'index.html',{'tareas':tareas})

def crear(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
    
    form = TareaForm()
    return render(request,'crear.html',{'form':form })


