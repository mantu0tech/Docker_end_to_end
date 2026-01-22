from django.shortcuts import render, redirect
from my_to_do_list_app.models import ToDoList
from my_to_do_list_app.forms import ToDoListForm
from django.core.exceptions import ObjectDoesNotExist


def to_do_list_view(request):
    to_do_list = ToDoList.objects.all().order_by('-id')
    return render(request, 'user_interface/to-do-list.html', {'task_list':to_do_list})

def to_do_create_view(request):
    if request.method == "POST":
        to_do_form = ToDoListForm(request.POST)
        if to_do_form.is_valid():
            to_do_form.save()
            to_do_form = ToDoListForm()
            return redirect('to_do_list')
    else:
        to_do_form = ToDoListForm()
    return render(request, 'user_interface/to-do-add.html', {'form':to_do_form})


def to_do_update_view(request, slug):
    try:
        if ToDoList.objects.get(slug=slug):
            to_do_update = ToDoList.objects.get(slug=slug)
            if request.method == 'POST':
                to_do_form = ToDoListForm(request.POST, instance=to_do_update)
                if to_do_form.is_valid():
                    to_do_form.save()
                    return redirect('to_do_list')
            else:
                to_do_form = ToDoListForm(instance=to_do_update)
                return render(request, 'user_interface/to-do-update.html', {'form':to_do_form,'to_do_update': to_do_update})
        else:
            to_do_update = ToDoList.objects.get(slug=slug)
    except ObjectDoesNotExist:
            exception_error = ObjectDoesNotExist('404 Not Found!')
            return render(request, 'user_interface/to-do-update.html', {'exception_error':exception_error})
         

def to_do_delete_view(request, slug):
    task = ToDoList.objects.get(slug=slug)
    task.delete()
    return redirect('to_do_list')