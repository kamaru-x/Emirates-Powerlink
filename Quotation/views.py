from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Requisition.models import Requisition,Requisition_Item
from Quotation.models import Quotation,QuotationItem,LPO
from django.contrib import messages
from datetime import datetime,date
# Create your views here.

#----------------------------------- QUOTATION COMPARISON -----------------------------------#

@login_required
def compare(request,reference):
    requisition = Requisition.objects.get(Reference = reference)
    quotations = Quotation.objects.filter(Requisition=requisition)
    context = {
        'requisition' : requisition,
        'quotations' : quotations
    }
    return render(request,'Dashboard/Quotation/comparison.html',context)

#----------------------------------- RECEIVE QUOTATION -----------------------------------#

@login_required
def receive_quotation(request,reference):
    requisition = Requisition.objects.get(Reference = reference)
    rq_items = Requisition_Item.objects.filter(Requisition=requisition).order_by('-id')
    
    last_quotation = Quotation.objects.last()

    if last_quotation:
        ref = f'QUO-{last_quotation.id+1}'
    else:
        ref = f'REF-001'

    if request.method == 'POST':
        vendor = request.POST.get('vendor')
        note = request.POST.get('note')
        brands = request.POST.getlist('brand[]')
        price = request.POST.getlist('price[]')
        net = request.POST.getlist('net[]')

        quotation = Quotation.objects.create(Requisition=requisition,Vendor=vendor,Note=note,Reference=ref)

        for i in range(len(rq_items)):
            rqi = rq_items[i]
            b = brands[i] or None
            p = price[i] or 0.00
            n = net[i] or 0.00

            print(f'RQI : {rqi} , Brand : {b} , Price : {p} , Net : {n}')

            try:
                QuotationItem.objects.create(Quotation=quotation,Item=rqi,Brand=b,Price=p,Net=n)
            except Exception as exception:
                messages.warning(request,exception)
                return redirect('compare' , reference=requisition.Reference)

            try:
                quotation.Sub_Total += float(n)
                quotation.save()
            except Exception as exception:
                messages.warning(request,exception)
                return redirect('compare' , reference=requisition.Reference)

        return redirect('compare' , reference=requisition.Reference)

    context = {
        'requisition' : requisition,
        'rq_items' : rq_items
    }

    return render(request,'Dashboard/Quotation/quotation-receive.html',context)

#----------------------------------- ACCEPT QUOTATION -----------------------------------#

@login_required
def accept_quotation(request):
    quotation_id = request.POST.get('quotation_id')
    quotation = Quotation.objects.get(id=quotation_id)
    quotation.Status = 2
    quotation.save()

    requisition = quotation.Requisition
    Quotation.objects.filter(Requisition=requisition).exclude(id=quotation_id).update(Status=0)

    return redirect('compare' , reference=requisition.Reference)

#----------------------------------- APPROVED QUOTATIONS -----------------------------------#

@login_required
def quotations(request):
    quotations = Quotation.objects.filter(Status = 2)

    context = {
        'quotations' : quotations
    }
    return render(request,'Dashboard/Quotation/quotations.html',context)

#----------------------------------- VIEW QUOTATION -----------------------------------#

@login_required
def view_quotation(request,reference):
    quotation = Quotation.objects.get(Reference = reference)
    items = QuotationItem.objects.filter(Quotation=quotation)

    context = {
        'quotation' : quotation,
        'items' : items
    }
    return render(request,'Dashboard/Quotation/quotation-view.html',context)

#----------------------------------- CONVERT TO LPO -----------------------------------#

@login_required
def convert_to_lpo(request,reference):
    quotation = Quotation.objects.get(Reference=reference)

    quotation.Status = 3
    quotation.LPO_Date = date.today()
    quotation.save()

    last_lpo = LPO.objects.last()

    if last_lpo:
        ref = f'LPO-00{last_lpo.id+1}'
    else:
        ref = f'LPO-001'

    LPO.objects.create(Quotation=quotation,Reference=ref)

    return redirect('lpos')

#----------------------------------- LPOS -----------------------------------#

@login_required
def lpos(request):
    # lpos = Quotation.objects.filter(Status=3)

    lpos = LPO.objects.all()

    context = {
        'lpos' : lpos
    }
    return render(request,'Dashboard/LPO/lpos.html',context)

#----------------------------------- LPO -----------------------------------#

@login_required
def print_lpo(request,reference):
    lpo = LPO.objects.get(Reference=reference)
    items = QuotationItem.objects.filter(Quotation=lpo.Quotation).exclude(Net=0)

    categories = []
    data = []

    for item in items:
        categories.append(item.Item.Product.Category)

    categories = list(set(categories))

    for categotry in categories:
        products = items.filter(Item__Product__Category=categotry)
        dict = {
            'category' : categotry,
            'products' : products
        }

        data.append(dict)

    context = {
        'lpo' : lpo,
        'data' : data
    }
    return render(request,'Dashboard/LPO/lpo.html',context)

#----------------------------------- EDIT LPO -----------------------------------#

@login_required
def edit_lpo(request,id):
    lpo = LPO.objects.get(id=id)
    quotation = lpo.Quotation
    items = QuotationItem.objects.filter(Quotation=quotation)

    if request.method == 'POST':
        pass

    context = {
        'lpo' : lpo,
        'quotation' : quotation,
        'items' : items
    }
    return render(request,'Dashboard/LPO/lpo-edit.html',context)