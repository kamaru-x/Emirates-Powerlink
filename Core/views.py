from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from Core.models import Category
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#----------------------------------- DASHBOARD -----------------------------------#

@login_required
def dashboard(request):
    page = 'dashboard'

    context = {
        'page' : page
    }
    return render(request,'Dashboard/Core/dashboard.html',context)

#----------------------------------- CHECK CATEGORY DUPLICATION -----------------------------------#

@csrf_exempt
def c_c_d(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        try:
            Category.objects.get(Name=name)
            status = 'failed'
        except:
            status = 'success'
    return JsonResponse({'status':status})

#----------------------------------- CATEGORY ADD -----------------------------------#

@login_required
def add_category(request):
    last_category = Category.objects.last()

    if last_category:
        reference = f'CAT-00{last_category.id+1}'
    else:
        reference = f'CAT-001'

    ip = request.META.get('REMOTE_ADDR')

    if request.method == 'POST':
        name = request.POST.get('name')
        note = request.POST.get('note')

        try:
            Category.objects.create(Added_By=request.user,Added_IP=ip,Name=name,Reference=reference,Note=note)
            messages.success(request,f'New category "{name}" created successfully ... !')
            return redirect('categories')
        
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('add-category')

    context = {
        'reference' : reference
    }

    return render(request,'Dashboard/Masters/category-add.html',context)

#----------------------------------- CATEGORY LIST -----------------------------------#

@login_required
def categories(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        category.delete()
        return redirect('categories')

    context = {
        'categories' : categories
    }
    return render(request,'Dashboard/Masters/categories.html',context)

#----------------------------------- CATEGORY EDIT -----------------------------------#

@login_required
def edit_category(request,category_id):
    category = Category.objects.get(Reference=category_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        note = request.POST.get('note')

        try:
            category.Name = name
            category.Note = note
            category.save()

            messages.success(request,'Category edited successfully ...! ')
            return redirect('categories')
        
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('edit-category' , category_id = category.Reference)

    context = {
        'category' : category
    }
    return render(request,'Dashboard/Masters/category-edit.html',context)