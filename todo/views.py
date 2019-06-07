from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST

#from .forms import TodoForm
from .forms import ModelTodoForm
from .models import Todo
# Create your views here.
 
def home(request):
    items = Todo.objects.order_by('tid') 
    #form = TodoForm()
   # context = {'data': items, 'form':form}
    mtodoform = ModelTodoForm()
    context = {'data': items, 'form':mtodoform}
    return render(request,'todo/home.html',context)

@require_POST
def addTodo(request):
    # form = TodoForm(request.POST)   
    # if form.is_valid():
    #       todoItem = Todo(tid=form.cleaned_data['index'],content=form.cleaned_data['content'])
    #       todoItem.save()

    mtodoform = ModelTodoForm(request.POST)
    if mtodoform.is_valid():
         mtodoform.save()
    return redirect('home')


def completedTodo(request,todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.iscomplete = True
    todo.save()
    return redirect('home')

def deleteCompleted(request):
    Todo.objects.filter(iscomplete__exact=True).delete()
    return redirect('home')

def deleteAll(request):
    Todo.objects.all().delete() 
    return redirect('home')

     

