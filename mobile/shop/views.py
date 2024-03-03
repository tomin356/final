from itertools import product

from django.shortcuts import render,redirect
from shop.models import Card,Product,Category,Cart,Order,Account
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def home(request):
    card=Card.objects.all()
    return render(request,'home.html',{'card':card})
def new(request):
    return render(request,'new.html')
def category(request):
    b=Category.objects.all()
    return render(request,'product.html',{'b':b})
def products(request,p):
    c = Category.objects.get(title=p)
    p = Product.objects.filter(category=c)
    return render(request, 'more.html', {'p': p})
@login_required
def viewmore(request,p):
    d=Product.objects.get(title=p)
    return render(request,'viewmore.html',{'d':d})

def sale(request):
    s=Card.objects.all()
    return render(request,'sale.html',{'card':s})
def search(request):
    q=""
    product=None
    if(request.method=="POST"):
        q=request.POST['q']
        if q:
            product=Product.objects.filter(Q(title__icontains=q)|Q(description__icontains=q))

    return render(request,'search.html',{'p':product,'query':q})
def register(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        if (p == cp):
            b = User.objects.create_user(username=u, password=p, email=e)
            b.save()
            return redirect('shop:login')
        else:
            return HttpResponse("password not matching")
    return render(request, 'register.html')
def userlogin(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('shop:home')
        else:
            messages.error(request,"invalid credentials")

    return render(request,'login.html')
@login_required
def cart(request):
    u=request.user
    total=0
    try:
        cart=Cart.objects.filter(user=u)
        for i in cart:
            total=i.quantity*i.product.price+total
    except:
        pass
    return render(request,'cart.html',{'c':cart,'total':total})
@login_required
def addtocart(request,p):
    d=Product.objects.get(title=p)
    u=request.user
    try:
        cart=Cart.objects.get(user=u,product=d)
        if(cart.quantity<cart.product.stock):
          cart.quantity+=1
        cart.save()
    except:
        cart=Cart.objects.create(product=d,user=u,quantity=1)
        cart.save()
    return redirect('shop:cart')
@login_required
def minusquantity(request,p):
    d = Product.objects.get(title=p)
    u = request.user
    try:
        cart = Cart.objects.get(user=u, product=d)
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
        else:
            cart.delete()
    except:
        pass
    return redirect('shop:cart')
@login_required
def deletequantity(request,p):
    d = Product.objects.get(title=p)
    u = request.user
    try:
        cart = Cart.objects.get(user=u, product=d)

        cart.delete()
    except:
        pass
    return redirect('shop:cart')
@login_required
def orderform(request):
    if (request.method == "POST"):
        a = request.POST['a']
        p = request.POST['p']
        n = request.POST['ac']
        u=request.user
        cart=Cart.objects.filter(user=u)

#accntil ninu place order kodukumbo money kureyn
        total=0
        for i in cart:
            total=i.quantity*i.product.price+total
# check whether user has sufficient amount or not
        ac=Account.objects.get(accntno=n)
        if(ac.amount>=total):
            ac.amount=ac.amount-total
            ac.save()

            for i in cart:#creates record in order table for each objects in cart table for the current user
                o=Order.objects.create(user=u,product=i.product,adress=a,phone=p,noofitems=i.quantity,order_status="paid")
                o.save()
                i.product.stock=i.product.stock-i.quantity#product tableil ninu count kurayan naml order cheyta sadanatintai
                i.product.save()
            cart.delete()#clears the cart items from the current user
            msg="Order Placed Succesfully"
            return render(request,'orderdetail1.html',{'m':msg})
        else:
            msg="Insuffucient Amount In User Account. You Cannot Place Order"
            return render(request, 'orderdetail2.html', {'m': msg})
    return render(request,'order.html')
@login_required
def orderview(request):
    u=request.user
    o=Order.objects.filter(user=u)
    return render(request,'orderview.html',{'o':o})
@login_required
def userlogout(request):
    logout(request)
    return userlogin(request)
def contact(request):
    return render(request,'contact.html')
