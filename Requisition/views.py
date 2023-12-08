from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from U_Auth.models import User
from Projects.models import Project
from Requisition.models import Requisition,Requisition_Item,Service,Service_Attachment
from Core.models import Category,Product
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db.models import Count
from django.contrib import messages
from Core.views import add_product

# Create your views here.

#----------------------------------- CREATE REQUISITION -----------------------------------#

@login_required
def create_requisition(request,project_id):
    if request.method == 'POST':
        project = Project.objects.get(id=project_id)
        ip = request.META.get('REMOTE_ADDR')
        type = request.POST.get('type')

        last_requisition = Requisition.objects.last()

        if last_requisition:
            reference = f'RQ-00{last_requisition.id+1}'
        else:
           reference = f'RQ-001' 

        r = Requisition.objects.create(Added_By=request.user,Prepared_By=request.user,Added_IP=ip,Project=project,Reference=reference,Requisition_Type=type)
        Service.objects.create(Requisition=r)

        return redirect('requisition',reference=reference)

#----------------------------------- REQUISITION -----------------------------------#

@login_required
def requisition(request,reference):
    requisition = Requisition.objects.get(Reference = reference)
    categories = Category.objects.all()

    rq_items = Requisition_Item.objects.filter(Requisition=requisition).order_by('-id')
    service = Service.objects.get(Requisition=requisition)
    attachments = Service_Attachment.objects.filter(Service=service)

    context = {
        'requisition' : requisition,
        'categories' : categories,
        'rq_items' : rq_items,
        'service' : service,
        'attachments' : attachments
    }
    return render(request,'Dashboard/Requisition/requisition.html',context)

#----------------------------------- GET PRODUCTS -----------------------------------#

@csrf_exempt
def get_products(request):
    category_id = request.POST.get('category_id')
    category = Category.objects.get(id=category_id)

    products = Product.objects.filter(Category=category)

    products_data = [{
        'id': product.id, 
        'name': product.Name,
        } for product in products]
    
    return JsonResponse({'status':'success','products':products_data})

#----------------------------------- ADD PRODUCTS -----------------------------------#

@csrf_exempt
def add_requisition_item(request):
    requisition_id = request.POST.get('requisition_id')
    requisition = Requisition.objects.get(id=requisition_id)
    product_id = request.POST.get('product_id')
    product = Product.objects.get(id=product_id)
    quantity = request.POST.get('quantity')
    note = request.POST.get('note')

    if request.method == 'POST':
        Requisition_Item.objects.create(Requisition=requisition,Product=product,Quantity=quantity,Note=note)
    
        return redirect('requisition',reference=requisition.Reference)

#----------------------------------- ADD PRODUCT AND ADD TO REQUISITION -----------------------------------#

@login_required
def add_new_item(request):
    last_product = Product.objects.last()

    if last_product:
        reference = f'PRODUCT-00{last_product.id+1}'
    else:
        reference = f'PRODUCT-001'

    ip = request.META.get('REMOTE_ADDR')

    requisition_id = request.POST.get('requisition_id')
    requisition = Requisition.objects.get(id=requisition_id)

    category_id = request.POST.get('category')
    category = Category.objects.get(id=category_id)

    name = request.POST.get('name')
    unit = request.POST.get('unit')

    quantity = request.POST.get('quantity')
    note = request.POST.get('note')

    try:
        product = Product.objects.create(Added_By=request.user,Added_IP=ip,Name=name,Reference=reference,Category=category,Unit=unit)
        Requisition_Item.objects.create(Requisition=requisition,Product=product,Quantity=quantity,Note=note)
    except Exception as exception:
        messages.warning(request,exception)

    return redirect('requisition',reference=requisition.Reference)
#----------------------------------- CREATE SERVICE REQUISITION -----------------------------------#

def service_requisition(request,requisition_id):
    requisition = Requisition.objects.get(id=requisition_id)

    if request.method == 'POST':
        try:
            req_service = Service.objects.get(Requisition=requisition)
            req_service.Title = request.POST.get('title')
            req_service.Description = request.POST.get('description')
            req_service.save()

            attachments = request.FILES.getlist('attachments')
            for attachment in attachments:
                Service_Attachment.objects.create(Service=req_service,Attachment=attachment)

            return redirect('requisitions')
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('requisition',reference=requisition.Reference)

#----------------------------------- DELETE SERVICE ATTACHMENT -----------------------------------#

def delete_attachment(request,attachment_id):
    attachment = Service_Attachment.objects.get(id=attachment_id)
    requisition = attachment.Service.Requisition
    attachment.delete()
    return redirect('requisition',reference=requisition.Reference)

#----------------------------------- DELETE REQUISITION ITEM -----------------------------------#

@login_required
def delete_requisition_item(request):
    item_id = request.POST.get('item_id')
    item = Requisition_Item.objects.get(id=item_id)
    requisition = item.Requisition
    item.delete()
    return redirect('requisition',reference=requisition.Reference)

#----------------------------------- REQUISITIONS -----------------------------------#

@login_required
def requisitions(request):
    if request.user.Job_Role == 'Purchase Manager':
        requisitions = Requisition.objects.filter(Requisition_Status='APPROVED').annotate(items=Count('requisition_item')).order_by('-id')
    else:
        requisitions = Requisition.objects.all().annotate(items=Count('requisition_item')).order_by('-id')

    projects = Project.objects.all().order_by('-id')

    context = {
        'requisitions' : requisitions,
        'projects' : projects
    }
    return render(request,'Dashboard/Requisition/requisitions.html',context)

#----------------------------------- VIEW REQUISITION -----------------------------------#

@login_required
def view_requisition(request,reference):
    requisition = Requisition.objects.get(Reference = reference)
    rq_items = Requisition_Item.objects.filter(Requisition=requisition).order_by('-id')
    service = Service.objects.get(Requisition=requisition)
    attachments = Service_Attachment.objects.filter(Service=service)

    context = {
        'requisition' : requisition,
        'rq_items' : rq_items,
        'service' : service,
        'attachments' : attachments
    }
    return render(request,'Dashboard/Requisition/requisition-view.html',context)

#----------------------------------- PRINT REQUISITION -----------------------------------#

@login_required
def print_requisition(request,reference):
    requisition = Requisition.objects.get(Reference = reference)
    rq_items = Requisition_Item.objects.filter(Requisition=requisition).order_by('-id')

    categories = []
    data = []

    for item in rq_items:
        categories.append(item.Product.Category)

    categories = list(set(categories))

    for categotry in categories:
        products = rq_items.filter(Product__Category=categotry)
        dict = {
            'category' : categotry,
            'products' : products
        }

        data.append(dict)
    
    print(dict)

    context = {
        'requisition' : requisition,
        'rq_items' : rq_items,
        'data' : data
    }
    return render(request,'Dashboard/Requisition/requisition-print.html',context)

#----------------------------------- APPROVE REQUISITION -----------------------------------#

@login_required
def approve_requisition(request,reference):
    requisition = Requisition.objects.get(Reference=reference)
    requisition.Requisition_Status = 'APPROVED'
    requisition.Approved_By = request.user
    requisition.save()
    return redirect('view-requisition',reference=requisition.Reference)

#----------------------------------- REJECT REQUISITION -----------------------------------#

@login_required
def reject_requisition(request,reference):
    requisition = Requisition.objects.get(Reference=reference)
    requisition.Requisition_Status = 'REJECTED'
    requisition.Rejected_By = request.user
    requisition.Reason = request.POST.get('reason')
    requisition.save()
    return redirect('view-requisition',reference=requisition.Reference)

#----------------------------------- CHECK REQUISITION -----------------------------------#

@login_required
def check_requisition(request,reference):
    requisition = Requisition.objects.get(Reference=reference)
    requisition.Requisition_Status = 'CHECKED'
    requisition.Checked_By = request.user
    requisition.save()
    return redirect('view-requisition',reference=requisition.Reference)