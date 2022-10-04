from ast import Mod
from django.shortcuts import redirect, render
from validTodo.forms import ModelForm

from validTodo.models import TodoModel

# Create your views here.


def allTodos(req):
    data = TodoModel.objects.all()
    return render(req, 'todo/index.html', {'todos': data})


def addTodo(req):
    form = ModelForm()
    if req.method == 'POST':
        form = ModelForm(req.POST)
        if form.is_valid:
            form.save()
            return redirect('all-todos')
    return render(req, 'todo/addTodo.html', {'form': form})


def updateTodo(req, id):
    todo = TodoModel.objects.get(id=id)
    updateForm = ModelForm(instance=todo)
    if req.method == 'POST':
        updateForm = ModelForm(req.POST, instance=todo)
        if updateForm.is_valid():
            updateForm.save()
            return redirect('all-todos')
    return render(req, 'todo/updateTodo.html', {'todo': todo, 'updateForm': updateForm})


def deleteTodo(req, id):
    todo = TodoModel.objects.get(id=id)
    todo.delete()
    return redirect('all-todos')
