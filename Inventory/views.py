from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Projects.models import Project
from Quotation.models import Quotation,QuotationItem
from Inventory.models import Inventory,InventoryItem
from datetime import date,datetime
from django.db.models import Sum

# Create your views here.

#----------------------------------- PROJECT INVENTORY LIST -----------------------------------#

@login_required
def project_inventory(request):
    projects = Quotation.objects.filter(Status=3)

    context = {
        'projects' : projects
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

    inventory = Inventory.objects.create(Project=project,Added_By=request.user,Reference=reference)

    for x in range(len(items)):
        i = items[x]
        q = quantity[x]

        if i and q:
            item = QuotationItem.objects.get(id=i)
            print(f'item : {item.Item.Product} /// quantity : {q}')
            InventoryItem.objects.create(Inventory=inventory,Item=item,Quantity=q)

    return redirect('inventory-view',quotation_id=quotation.id)