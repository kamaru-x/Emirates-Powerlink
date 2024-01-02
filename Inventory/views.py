from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Projects.models import Project
from Quotation.models import Quotation,QuotationItem
from Inventory.models import InventoryItem,Inventory_Category,Inventory_In,Inventory_Out
from datetime import date,datetime
from django.db.models import Sum

# Create your views here.

#----------------------------------- PROJECT INVENTORY LIST -----------------------------------#

@login_required
def inventory(request):
    projects = Project.objects.all()
    # categories = Inventory_Category.objects.all().order_by('-id')
    categories = Inventory_Category.objects.prefetch_related('inventoryitem_set').order_by('-id')
    inv_items = InventoryItem.objects.all()

    context = {
        'projects' : projects,
        'categories' : categories,
        'inv_items' : inv_items
    }
    return render(request,'Dashboard/Inventory/inventory.html',context)

#----------------------------------- Inventory Category -----------------------------------#

def inventory_category(request):
    if request.method == 'POST':
        name = request.POST.get('category')
        Inventory_Category.objects.create(Name=name)
        return redirect('inventory')
    
#----------------------------------- Inventory IN -----------------------------------#

def inventory_in(request):
    if request.method == 'POST':
        inv_type = request.POST.get('inv-type')
        inv_item = request.POST.get('inv-item')
        category = request.POST.get('category')
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')

        print(inv_type,inv_item,category,name,quantity)

        if inv_type == 'existing':
            item = InventoryItem.objects.get(id=inv_item)
            item.Quantity += int(quantity)
            item.save()
            Inventory_In.objects.create(Item=item,Quantity=quantity)

        elif inv_type == 'new':
            ref = InventoryItem.objects.last()
            reference = f'INV00{ref.id+1}'
            category = Inventory_Category.objects.get(id=category)
            item = InventoryItem.objects.create(Name=name,Category=category,Reference=reference,Quantity=quantity)
            Inventory_In.objects.create(Item=item,Quantity=quantity)

        return redirect('inventory')

#----------------------------------- Inventory OUT -----------------------------------#

def inventory_out(request):
    if request.method == 'POST':
        project_id = request.POST.get('project')
        project = Project.objects.get(id=project_id)
        item_id = request.POST.get('item')
        item = InventoryItem.objects.get(id=item_id)
        quantity = request.POST.get('quantity')

        item.Quantity -= int(quantity)
        item.save()

        Inventory_Out.objects.create(Project=project,Item=item,Quantity=quantity)
        return redirect('inventory')

#----------------------------------- Inventory Category -----------------------------------#

@login_required
def project_inventory(request):
    projects = Quotation.objects.filter(Status=3).order_by('-id')

    context = {
        'projects' : projects,
    }
    return render(request,'Dashboard/Inventory/inventory-projects.html',context)

#----------------------------------- INVENTORY VIEW -----------------------------------#

@login_required
def inventory_view(request,quotation_id):
    quotation = Quotation.objects.get(id=quotation_id)
    items = []
    items_list = QuotationItem.objects.filter(Quotation=quotation)

    for i in items_list:
        # Use aggregate to find the sum of Quantity in Received
        received = InventoryItem.objects.filter(Item=i).aggregate(Sum('Quantity'))['Quantity__sum'] or 0

        data = {
            'Name': i.Item.Product.Name,
            'Total': i.Item.Quantity,
            'Received': received,
        }

        items.append(data)

    context = {
        'quotation' : quotation,
        'project' : quotation.Requisition.Project,
        'items' : items,
        'items_list' : items_list
    }

    return render(request,'Dashboard/Inventory/inventory-view.html',context)

#----------------------------------- ADD TO INVENTORY -----------------------------------#

@login_required
def add_to_inventory(request,quotation_id):
    quotation = Quotation.objects.get(id=quotation_id)
    project=quotation.Requisition.Project
    dt = date.today()

    items = request.POST.getlist('items[]')
    quantity = request.POST.getlist('quantity[]')

    reference = f'IN-EN-{dt}'

    inventory = InventoryItem.objects.create(Project=project,Added_By=request.user,Reference=reference)

    for x in range(len(items)):
        i = items[x]
        q = quantity[x]

        if i and q:
            item = QuotationItem.objects.get(id=i)
            print(f'item : {item.Item.Product} /// quantity : {q}')
            InventoryItem.objects.create(Inventory=inventory,Item=item,Quantity=q)

    return redirect('inventory-view',quotation_id=quotation.id)