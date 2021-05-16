from typing_extensions import ParamSpec
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.http import HttpResponse
from .models import Product, Orders, OrderUpdate
import json

# Create your views here.
def index(request):
    products = Product.objects.all()
    params = {'products':products}
    return render(request, 'shop/index.html', params)

def searchMatch(item, query):
    query = query.lower()
    if query in item.product_name.lower() or query in item.product_desc.lower() or query in item.category.lower() or query in item.sub_category.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    productsTemp = Product.objects.all()
    products = [item for item in productsTemp if searchMatch(item, query)]
    if len(products) == 0 or len(query) == 0:
        params = {'msg': "This product could not be found."}
    else:
        params = {'products':products, 'msg': ""}
    
    return render(request, 'shop/index.html', params)

def viewByCategory(request):
    allProds = []
    allCat = Product.objects.values('category')
    cats = {item['category'] for item in allCat}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        allProds.append([prod, n])
    params = {'allProds': allProds}
    return render(request, 'shop/category.html', params)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def cancelOrder(request):
    if request.method=="POST":
        orderId= request.POST.get('orderId', '')
        email=request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            amount = order[0].amount
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc, 'time':item.timestamp})
                    response = json.dumps([updates, order[0].items_json, amount, orderId] , default=str)
                order.delete()
                update.delete()
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, 'shop/cancelOrder.html')


def tracker(request):
    if request.method=="POST":
        orderId= request.POST.get('orderId', '')
        email=request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            amount = order[0].amount
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc, 'time':item.timestamp})
                    response = json.dumps([updates, order[0].items_json, amount] , default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request, 'shop/tracker.html')

def productView(request, id):
    product = Product.objects.filter(id = id)
    return render(request, 'shop/viewproduct.html', {'product': product[0]})

def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        amount = request.POST.get('amount', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('add1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('add2', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')

        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone, amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="Order has been placed.")
        update.save()
        thank=True
        id=order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})
    return render(request, 'shop/checkout.html')

def cart(request):
    return render(request, 'shop/cart.html')