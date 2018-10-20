from datetime import datetime

from django.contrib import messages
from django.shortcuts import redirect, render, reverse

from .forms import ToDo
from .models import TodoList


def home(request):
    if request.method == 'GET':
        todo_list = TodoList.objects.filter(deleted_at=None)
        return render(request, 'todo/home.html', {'tasks': todo_list})
    return render(request, "Bad Request")


def create(request):
    if request.method == 'GET':
        form = ToDo()
        return render(request, 'todo/create.html', {'form': form})
    elif request.method == 'POST':
        todo_task = TodoList()
        todo_task.title = request.POST.get('title')
        todo_task.description = request.POST.get('description')
        todo_task.todo_time = request.POST.get('todo_time')
        todo_task.status = request.POST.get('status')
        try:
            todo_task.save()
            messages.success(request, "TO DO task created")
        except Exception as e:
            messages.warning(request, "Task is not created")
            print(e)
        return redirect(reverse('home'))
    return render(request, "Bad Request")


def update(request, id):
    if request.method == 'GET':
        task = TodoList.objects.filter(id=id)[0]
        data = {'title': task.title, 'description': task.description, 'status': task.status,
                'todo_time': task.todo_time}
        form = ToDo(initial=data)
        return render(request, 'todo/update.html', {'form': form})
    elif request.method == 'POST':
        form = ToDo(request.POST)
        if form.is_valid():
            task = TodoList.objects.get(id=id)
            task.title = form.cleaned_data.get('title')
            task.description = form.cleaned_data.get('description')
            task.status = form.cleaned_data.get('status')
            task.todo_time = form.cleaned_data.get('todo_time')
            try:
                task.save()
                messages.success(request, 'Your task info has been updated ')
            except Exception as e:
                print(e)
            return redirect(reverse('home'))
        else:
            task = TodoList.objects.filter(id=id)[0]
            data = {'title': task.title, 'description': task.description, 'status': task.status,
                    'todo_time': task.todo_time}
            form = ToDo(initial=data)
            messages.warning(request, 'Please enter valid data for edited fields')
            return render(request, 'todo/update.html', {'form': form})
    return render(request, "Bad Request")


def delete(request, id):
    if request.method == 'GET':
        task = TodoList.objects.get(id=id)
        task.deleted_at = datetime.now()
        try:
            task.save()
            messages.success(request, 'Your task has been deleted')
        except Exception as e:
            print(e)
            messages.warning(request, 'Something went wrong')
        return redirect(reverse('home'))
    return render(request, "Bad Request")


def get_task(request, id):
    if request.method == 'GET':
        task = []
        try:
            task = TodoList.objects.filter(id=id, deleted_at=None)
        except Exception as e:
            print(e)
        return render(request, 'todo/task.html', {'tasks': task})
    return render(request, "Bad Request")
