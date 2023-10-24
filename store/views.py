from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

def store(request):
    products=Product.objects.all()
    context={'products':products}
    return render(request,"store.html",context)

def cart(request):
    if request.user.is_authenticated:
       cart_items=Cart.objects.filter(user=request.user)
       total_price=sum(item.product.price*item.quantity for item in cart_items)
       total_quantity=sum(item.quantity for item in cart_items)
    return render(request,"cart.html",{'cart_items':cart_items,'total_price':total_price,'total_quantity':total_quantity})

def checkout(request):  
    if request.user.is_authenticated:
       cart_items=Cart.objects.filter(user=request.user)
       if request.method=='POST':
           name=request.POST.get('name')
           email=request.POST.get('email')
           address=request.POST.get('address')
           city=request.POST.get('city')
           state=request.POST.get('state')
           pincode=request.POST.get('pincode')
           phone=request.POST.get('phone')
           user=request.user
           for item in cart_items:
               order=Order(user=user,name=name,email=email,price=item.product.price,quantity=item.quantity,address=address,city=city,state=state,pincode=pincode,phone=phone)
           order.save()
           messages.success(request,"Your Order Succesfully placed.")
           Cart.objects.filter(user=request.user).delete()
           return redirect('cart')
       total_price=sum(item.product.price*item.quantity for item in cart_items)
       total_quantity=sum(item.quantity for item in cart_items)
    return render(request,"checkout.html",{'cart_items':cart_items,'total_price':total_price,'total_quantity':total_quantity})

def main(request):
    context={}
    return render(request,"main.html",context)

def signup(request):
    if request.method=='POST':
       uname=request.POST.get('username')
       email=request.POST.get('email')
       pass1=request.POST.get('pass1')
       pass2=request.POST.get('pass2')
       if pass1!=pass2:
             messages.error(request,"Your Current password and Confirm password not matched")
       elif len(pass1)<6:
            messages.error(request,"You Password should be minimum 6 characters")
       else:
           my_user=User.objects.create_user(uname,email,pass1)
           my_user.save()
           return redirect('store') 
    return render(request,'signup.html')

def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')
        user=authenticate(username=username,password=pass1)
        if user is not None:
            messages.success(request,"Succesfully Login")
            return redirect('store')
        else:
            messages.error(request,"Invalid Username and Password")
    return render(request,"index.html")

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        area=request.POST.get('area')
        contact=Contact(name=name,email=email,phone=phone,area=area)
        contact.save()
    return render(request,'contact.html')

def productview(request,myid):
    product=Product.objects.filter(id=myid)
    return render(request,"store/templates/product.html",{'product':product[0]})

def Logout(request):
    logout(request)
    return redirect('login')

def search(request):
    if request.method=='GET':
        query=request.GET.get('query')
        if query:
            products=Product.objects.filter(name__contains=query)
        elif query=='':
            return redirect('store')
            
    return render(request,'store/templates/search.html',{'products':products})
def add_to_cart(request,product_id):
    product=Product.objects.get(pk=product_id)
    if request.method=='POST':
        quantity=int(request.POST['quantity'])
        if quantity>0:
           user=request.user
           cart_item=Cart.objects.create(user=user,product=product)
           cart_item.quantity+=quantity
           cart_item.save()
           return redirect('cart')
        else:
            return redirect('store')
    return render(request,'cart.html',{product:'product'})

def remove_cart(request,product_id):
    cart_items=Cart.objects.get(id=product_id)
    cart_items.delete()
    return redirect('cart')

