from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from Core.models import Category,Sub_Category,Sub_In_Category,Product
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from U_Auth.models import User
from Projects.models import Project
from Requisition.models import Requisition
from Quotation.models import Quotation
from django.db.models import Count

# Create your views here.

#----------------------------------- DASHBOARD -----------------------------------#

@login_required
def dashboard(request):
    page = 'dashboard'
    products = Product.objects.all()
    projects = Project.objects.all()
    requisitions = Requisition.objects.all()
    quotations = Quotation.objects.all()

    context = {
        'page' : page,
        'products' : products.count(),
        'projects' : projects.count(),
        'requisitions' : requisitions.count(),
        'quotations' : quotations.count(),
        'recent_requisitions' : requisitions.order_by('-id')[:3]
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
    categories = Category.objects.all().annotate(
        products_count=Count('product'),
        subcategories_count=Count('sub_category')
    ).order_by('-id')

    context = {
        'categories' : categories
    }
    return render(request,'Dashboard/Masters/categories.html',context)

#----------------------------------- CATEGORY DELETE -----------------------------------#

@login_required
def delete_category(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Category.objects.get(id=category_id)
        category.delete()
        messages.warning(request,'Category Deleted Successfully ... !')
        return redirect('categories')
#----------------------------------- CATEGORY VIEW -----------------------------------#

@login_required
def view_category(request,category_id):
    category = Category.objects.get(Reference=category_id)
    categories = Sub_Category.objects.filter(Category=category).annotate(
        categories_count=Count('sub_in_category'),
        products_count=Count('product'),
    ).order_by('-id')

    products = Product.objects.filter(Category=category)

    context = {
        'category' : category,
        'categories' : categories,
        'products' : products
    }
    return render(request,'Dashboard/Masters/category-view.html',context)

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

#----------------------------------- SUB CATEGORIES -----------------------------------#

@login_required
def sub_categories(request):
    categories = Sub_Category.objects.annotate(
        categories_count=Count('sub_in_category'),
        products_count=Count('product')
    ).order_by('-id')

    context = {
        'categories' : categories
    }
    return render(request,'Dashboard/Masters/sub-categories.html',context)

#----------------------------------- ADD SUB CATEGORY -----------------------------------#

@login_required
def add_sub_category(request):
    categories = Category.objects.all().order_by('-id')
    last_category = Sub_Category.objects.last()

    if last_category:
        reference = f'SCAT-00{last_category.id+1}'
    else:
        reference = f'SCAT-001'

    if request.method == 'POST':
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)

        name = request.POST.get('name')
        ref = request.POST.get('ref')
        note = request.POST.get('note')

        try:
            Sub_Category.objects.create(Category=category,Name=name,Reference=ref,Note=note)
            messages.success(request,'New Sub Category Created ... !')
            return redirect('sub-categories')
        
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('add-sub-category')

    context = {
        'categories' : categories,
        'reference' : reference
    }
    return render(request,'Dashboard/Masters/sub-category-add.html',context)

#----------------------------------- EDIT SUB CATEGORY -----------------------------------#

@login_required
def edit_sub_category(request,scid):
    categories = Category.objects.all()
    sub_category = Sub_Category.objects.get(Reference=scid)

    if request.method == 'POST':
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)

        sub_category.Name = request.POST.get('name')
        sub_category.Category = category
        sub_category.Note = request.POST.get('note')

        sub_category.save()
        messages.success(request,'Sub Category Edited successfully ... !')

        return redirect('sub-categories')

    context = {
        'categories' : categories,
        'category' : sub_category
    }

    return render(request,'Dashboard/Masters/sub-category-edit.html',context)

#----------------------------------- VIEW SUB CATEGORY -----------------------------------#

@login_required
def view_sub_category(request,scid):
    category = Sub_Category.objects.get(Reference=scid)
    categories = Sub_In_Category.objects.filter(Sub_Category=category).annotate(
        products_count=Count('product')
    ).order_by('-id')

    products = Product.objects.filter(Sub_Category=category)

    context = {
        'category' : category,
        'categories' : categories,
        'products' : products
    }
    return render(request,'Dashboard/Masters/sub-category-view.html',context)

#----------------------------------- DELETE SUB CATEGORY -----------------------------------#

@login_required
def delete_sub_category(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Sub_Category.objects.get(id=category_id)

        category.delete()
        messages.warning(request,'Sub Category Deleted Successfully ... !')

        return redirect('sub-categories')

#----------------------------------- SUB IN CATEGORIES -----------------------------------#
    
@login_required
def sub_in_categories(request):
    categories = Sub_In_Category.objects.annotate(
        products_count=Count('product')
    ).order_by('-id')

    context = {
        'categories' : categories
    }
    return render(request,'Dashboard/Masters/sub-in-categories.html',context)

#----------------------------------- GET SUB CATEGORIES -----------------------------------#

@csrf_exempt
def get_sub_categories(request):
    if request.method == 'POST':
        cat_id = request.POST.get('cat-id')
        category = Category.objects.get(id=cat_id)

        sub_categories = Sub_Category.objects.filter(Category=category)
        sub_categories_data = list(sub_categories.values())

        return JsonResponse({'status':'success','sub_categories':sub_categories_data})

#----------------------------------- ADD SUB IN CATEGORY -----------------------------------#

@login_required
def add_sub_in_category(request):
    categories = Category.objects.all().order_by('-id')
    last_category = Sub_In_Category.objects.last()

    if last_category:
        reference = f'SICAT-00{last_category.id+1}'
    else:
        reference = f'SICAT-001'

    if request.method == 'POST':
        sub_category_id = request.POST.get('sub_category')
        sub_category = Sub_Category.objects.get(id=sub_category_id)

        ref = request.POST.get('ref')
        name = request.POST.get('name')
        note = request.POST.get('note')

        try:
            Sub_In_Category.objects.create(Sub_Category=sub_category,Name=name,Reference=ref,Note=note)
            messages.success(request,'Sub In Category created successfully ... !')
            return redirect('sub-in-categories')
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('add-sub-in-category')

    context = {
        'categories' : categories,
        'reference' : reference,
    }
    return render(request,'Dashboard/Masters/sub-in-category-add.html',context)

#----------------------------------- ADD SUB IN CATEGORY -----------------------------------#

@login_required
def edit_sub_in_category(request,sicid):
    category = Sub_In_Category.objects.get(Reference=sicid)
    categories = Category.objects.all()

    if request.method == 'POST':
        sub_category_id = request.POST.get('sub_category')
        sub_category = Sub_Category.objects.get(id=sub_category_id)

        category.Sub_Category = sub_category
        category.Name = request.POST.get('name')
        category.Note = request.POST.get('note')

        category.save()
        messages.success(request,'Sub In Category Edited Successfully ... !')
        return redirect('sub-in-categories')
    
    context = {
        "category" : category,
        'categories' : categories
    }
    return render(request,'Dashboard/Masters/sub-in-category-edit.html',context)

#----------------------------------- VIEW SUB IN CATEGORY -----------------------------------#

@login_required
def view_sub_in_category(request,sicid):
    category = Sub_In_Category.objects.get(Reference=sicid)
    products = Product.objects.filter(Sub_In_Category=category)

    context = {
        'category' : category,
        'products' : products
    }
    return render(request,'Dashboard/Masters/sub-in-category-view.html',context)

#----------------------------------- DELETE SUB IN CATEGORY -----------------------------------#

@login_required
def delete_sub_in_category(request):
    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        category = Sub_In_Category.objects.get(id=category_id)

        category.delete()
        messages.warning(request,'Sub In Category Deleted Successfully ... !')

        return redirect('sub-in-categories')

#----------------------------------- CHECK USER DUPLICATION -----------------------------------#

@csrf_exempt
def c_u_d(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            User.objects.get(username=username)
            status = 'failed'
        except:
            status = 'success'
    return JsonResponse({'status':status})

#----------------------------------- STAFF ADD -----------------------------------#

@login_required
def add_staff(request):
    last_staff = User.objects.last()
    
    if last_staff:
        reference = f'STAFF-00{last_staff.id}'
    else:
        reference = f'STAFF-001'

    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        job_role = request.POST.get('job_role')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')

        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.create(username=username,first_name=name,Staff_ID=reference,Image=image,Job_Role=job_role,Mobile=mobile,email=email)
            user.set_password(password)
            user.save()

            messages.success(request,f'New staff "{name}" added successfully ...!')
            return redirect('staffs')
        
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('add-staff')

    context = {
        'reference' : reference
    }

    return render(request,'Dashboard/Masters/staff-add.html',context)

#----------------------------------- STAFF LIST -----------------------------------#

@login_required
def staffs(request):
    staffs = User.objects.exclude(is_superuser=True).order_by('-id')

    if request.method == 'POST':
        staff_id = request.POST.get('staff_id')
        
        try:
            staff = User.objects.get(id=staff_id)
            staff.is_active = False
            staff.save()
        except Exception as exception:
            messages.warning(request,exception)

        return redirect('staffs')

    context = {
        'staffs' : staffs
    }
    return render(request,'Dashboard/Masters/staffs.html',context)

#----------------------------------- VIEW STAFF -----------------------------------#

@login_required
def staff_details(request,username):
    staff = User.objects.get(username=username)

    context = {
        'staff' : staff
    }

    return render(request,'Dashboard/Masters/staff-view.html',context)

#----------------------------------- EDIT STAFF -----------------------------------#

@login_required
def edit_staff(request,username):
    staff = User.objects.get(username=username)

    if request.method == 'POST':
        if len(request.FILES) > 0:
            staff.Image = request.FILES.get('image')

        try:
            staff.first_name = request.POST.get('name')
            staff.Job_Role = request.POST.get('job_role')
            staff.Mobile = request.POST.get('mobile')
            staff.email = request.POST.get('email')
            staff.save()

            messages.success(request,'Staff details edited successfully ... !')
            return redirect('staffs')

        except Exception as exception:
            messages.warning(request,exception)
            return redirect('edit-staff' , username=staff.username)

    context = {
        'staff' : staff
    }

    return render(request,'Dashboard/Masters/staff-edit.html',context)

#----------------------------------- PRODUCTS -----------------------------------#

@login_required
def products(request):
    products = Product.objects.all().order_by('-id')

    context = {
        'products' : products
    }
    return render(request,'Dashboard/Masters/products.html',context)

#----------------------------------- DELETE PRODUCT -----------------------------------#

@login_required
def delete_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)
        product.delete()
        messages.warning(request,'Product Deleted Successfully ... !')
        return redirect('products')

#----------------------------------- GET SUB IN CATEGORY -----------------------------------#

@csrf_exempt
def get_sub_in_categories(request):
    if request.method == 'POST':
        cat_id = request.POST.get('cat-id')
        category = Sub_Category.objects.get(id=cat_id)

        categories = Sub_In_Category.objects.filter(Sub_Category=category)
        categories_data = list(categories.values())

        return JsonResponse({'status':'success','sub_in_categories':categories_data})

#----------------------------------- ADD PRODUCT -----------------------------------#

@login_required
def add_product(request):
    categories = Category.objects.all()
    last_product = Product.objects.last()

    if last_product:
        reference = f'PRODUCT-00{last_product.id+1}'
    else:
        reference = f'PRODUCT-001'

    ip = request.META.get('REMOTE_ADDR')

    if request.method == 'POST':
        category_id = request.POST.get('category')
        sub_category_id = request.POST.get('sub_category')
        sub_in_category_id = request.POST.get('sub_in_category')

        category = Category.objects.get(id=category_id)

        try:
            sub_category = Sub_Category.objects.get(id=sub_category_id)
        except:
            sub_category = None

        try:
            sub_in_category = Sub_In_Category.objects.get(id=sub_in_category_id)
        except:
            sub_in_category = None

        name = request.POST.get('name')
        unit = request.POST.get('unit')
        note = request.POST.get('note')

        try:
            Product.objects.create(Added_By=request.user,Added_IP=ip,Name=name,Reference=reference,Category=category,Sub_Category=sub_category,Sub_In_Category=sub_in_category,Unit=unit,Note=note)
            messages.success(request,f'New product "{name}" added successfully ... !')
            return redirect('products')
        
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('add-product')

    context = {
        'categories' : categories,
        'reference' : reference
    }
    return render(request,'Dashboard/Masters/product-add.html',context)

#----------------------------------- EDIT PRODUCT -----------------------------------#

@login_required
def edit_product(request,product_id):
    product = Product.objects.get(Reference=product_id)
    categories = Category.objects.all()

    if request.method == 'POST':
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)

        sub_category_id = request.POST.get('sub_category')
        sub_in_category_id = request.POST.get('sub_in_category')

        try:
            sub_category = Sub_Category.objects.get(id=sub_category_id)
        except:
            sub_category = None

        try:
            sub_in_category = Sub_In_Category.objects.get(id=sub_in_category_id)
        except:
            sub_in_category = None

        try:
            product.Category = category
            product.Sub_Category = sub_category
            product.Sub_In_Category = sub_in_category
            product.Name = request.POST.get('name')
            product.Unit = request.POST.get('unit')
            product.Note = request.POST.get('note')
            product.save()

            messages.success(request,f'Product edited successfully ... !')
            return redirect('products')
        
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('edit-product',product_id=product.Reference)

    context = {
        'product' : product,
        'categories' : categories
    }
    return render(request,'Dashboard/Masters/product-edit.html',context)