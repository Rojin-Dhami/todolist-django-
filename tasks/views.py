from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    if request.method == "POST":
        new_task = request.POST.get('title')
        if new_task:
            Task.objects.create(user=request.user, title=new_task)
        return redirect('task_list')
    return render(request, 'tasks/list.html', {'tasks': tasks})

@login_required
def delete_task(request, pk):
    Task.objects.get(id=pk, user=request.user).delete()
    return redirect('task_list')