from django.urls import reverse
from django.shortcuts import render, redirect

from customer.models import userregistration, userlogin, kitchen, menucategory, menuitem, order, orderitem, delivery, \
    payment, coupon, review, notification, ingredient


# Create your views here.
def changepassword(request):
    uname=request.session['username']
    if request.method == 'POST':
        currentpass = request.POST.get('t1', '')
        newpass = request.POST.get('t2', '')
        confirmpass = request.POST.get('t3', '')

        ucheck = userlogin.objects.filter(username=uname).values()
        for a in ucheck:
            u = a['username']
            p = a['password']
            if u == uname and currentpass == p:
                if newpass == confirmpass:
                    userlogin.objects.filter(username=uname).update(password=newpass)
                    base_url=reverse('logcheck')
                    msg='password has been changed successfully'
                    return redirect(base_url,msg=msg)
                else:
                    return render(request, 'change.html',{'msg': 'both the usename and password are incorrect'})
            else:
                return render(request, 'change.html',{'msg': 'invalid username'})
    return render(request, 'change.html')

def showindex(request):
    return render(request,'index.html',)

def owner_home(request):
    return render(request, "owner_home.html")

def customer_home(request):
    return render(request, "customer_home.html")


def insertuserregistration(request):
    if request.method=="POST":
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5= request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        userregistration.objects.create(name=s1,email=s2,password=s3,contact=s4,city=s5,address=s6,role=s7)
        userlogin.objects.create(username=s2, password=s3, type=s7)
        return redirect('logcheck')
    return render(request,"userregistration.html")

def logcheck(request):
    if request.method=="POST":
        username=request.POST.get('name')
        password = request.POST.get('password')
        count=userlogin.objects.filter(username=username).count()
        if count>=1:
            udata=userlogin.objects.get(username=username)
            request.session['username'] = username
            upass=udata.password
            utype=udata.type
            if upass==password:
                if utype.lower() in ['customer']:
                    return render(request,'customer_home.html')
                else:
                    return render(request,'owner_home.html')
            else:
                return render(request,'login.html',{'msg':'invalid password'})
        else:
            return render(request, 'login.html', {'msg': 'invalid username'})

    return render(request,'login.html')



def logout(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect('showindex')

def showuserregistration(request):
    userdict=userregistration.objects.all()
    return render(request,"userregistration.html",{"userdict":userdict})

def deluserregistration(request,pk):
    id = userregistration.objects.get(id=pk)
    id.delete()
    userdict = userregistration.objects.all()
    return render(request, "viewuserregistration.html", {"userdict": userdict})

def insertuserlogin(request):
    if request.method=="POST":
        s1=request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        userlogin.objects.create(username=s1,password=s2,type=s3,)
        return render(request,"userlogin.html")
    return render(request,"userlogin.html")

def showuserlogin(request):
    userdict=userlogin.objects.all()
    return render(request,"viewuserlogin.html",{"userdict":userdict})

def deluserlogin(request,pk):
    id = userlogin.objects.get(id=pk)
    id.delete()
    userdict = userlogin.objects.all()
    return render(request, "viewuserlogin.html", {"userdict": userdict})

def insertkitchen(request):
    if request.method=="POST":
        s1=request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s8 = request.POST.get("t8")
        s9 = request.FILES.get("t9")
        kitchen.objects.create(owner=s1,kitchen_name=s2,cuisine_type=s3,location=s4,contact=s5,license_number=s6,rating=s7,status=s8,logo=s9)
        request.session['kname'] = s2
        return redirect('insertmenucategory')
    return render(request,"kitchen.html")

def showkitchen(request):
    userdict=kitchen.objects.all()
    return render(request,"viewkitchen.html",{"userdict":userdict})

def delkitchen(request,pk):
    id = kitchen.objects.get(id=pk)
    id.delete()
    userdict = kitchen.objects.all()
    return render(request, "viewkitchen.html", {"userdict": userdict})

def insertmenucategory(request):
    kname = request.session.get('kname', '')
    kitchen_list = kitchen.objects.all()
    if request.method=="POST":
        s1=request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        menucategory.objects.create(kitchen=s1,category_name=s2,description=s3,display_order=s4,status=s5)
        request.session['catname'] = s2
        if 'kname' in request.session:
            del request.session['kname']
        return redirect('insertmenuitem')
    return render(request,"menucategory.html", {'kname': kname, 'kitchen_list': kitchen_list})

def showmenucategory(request):
    kitchen_name = request.GET.get('kitchen')
    if kitchen_name:
        userdict = menucategory.objects.filter(kitchen=kitchen_name)
    else:
        userdict = menucategory.objects.all()
    return render(request,"viewmenucategory.html",{"userdict":userdict})

def delmenucategory(request,pk):
    id = menucategory.objects.get(id=pk)
    id.delete()
    userdict = menucategory.objects.all()
    return render(request, "viewmenucategory.html", {"userdict": userdict})


def insertmenuitem(request):
    catname = request.session.get('catname', '')
    category_list = menucategory.objects.all()
    if request.method=="POST":
        s1=request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s8 = request.POST.get("t8")
        s9 = request.POST.get("t9")
        s10 = request.FILES.get("t10")
        s11 = request.POST.get("t11")
        menuitem.objects.create(menuitem=s1,category=s2,item_name=s3,description=s4,price=s5,discount_price=s6,preparation_time=s7,veg_non_veg=s8,spice_level=s9,photo=s10,availability=s11)
        if 'catname' in request.session:
            del request.session['catname']
        return render(request,"menuitem.html", {'category_list': category_list})
    return render(request,"menuitem.html", {'catname': catname, 'category_list': category_list})

def showmenuitem(request):
    category_name = request.GET.get('category')
    if category_name:
        userdict = menuitem.objects.filter(category=category_name)
    else:
        userdict = menuitem.objects.all()
    return render(request,"viewmenuitem.html",{"userdict":userdict})

def delmenuitem(request,pk):
    id = menuitem.objects.get(id=pk)
    id.delete()
    userdict = menuitem.objects.all()
    return render(request, "viewmenuitem.html", {"userdict": userdict})


def insertorder(request):
    import datetime
    username = request.session.get('username', '')
    kname = request.session.get('kname', '')
    oid = request.session.get('oid', '')
    
    # Calculate sum of total_price from orderitem table where order is oid
    items = orderitem.objects.filter(order=oid)
    total_sum = 0.0
    for item in items:
        try:
            total_sum += float(item.total_price)
        except (ValueError, TypeError):
            pass
            
    discount = request.session.get('discount_price', '0.00')
    try:
        discount_val = float(discount)
    except ValueError:
        discount_val = 0.0
        
    famt = max(0.0, total_sum - discount_val)
    today = datetime.date.today().strftime('%Y-%m-%d')
    
    if request.method=="POST":
        s1=request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s8 = request.POST.get("t8")
        s9 = request.POST.get("t9")
        s10 = request.POST.get("t10")
        order.objects.create(customer=s1,kitchen=s2,order_date=s3,delivery_address=s4,total_amount=s5,discount_applied=s6,final_amount=s7,order_type=s8,special_instructions=s9,status=s10)
        request.session['totamt'] = s7
        return redirect('insertpayment')
        
    context = {
        'username': username,
        'kname': kname,
        'today': today,
        'total_sum': f"{total_sum:.2f}",
        'discount': f"{discount_val:.2f}",
        'famt': f"{famt:.2f}",
    }
    return render(request,"order.html", context)

def showorder(request):
    userdict=order.objects.all()
    return render(request,"vieworder.html",{"userdict":userdict})

def delorder(request,pk):
    id = order.objects.get(id=pk)
    id.delete()
    userdict = order.objects.all()
    return render(request, "vieworder.html", {"userdict": userdict})



def insertorderitem(request):
    import datetime
    import random

    item_name = request.session.get('item_name', '')
    price = request.session.get('price', '')
    discount_price = request.session.get('discount_price', '')
    kname = request.session.get('kname', '')
    
    if request.GET.get('item_name'):
        item_name = request.GET.get('item_name')
        request.session['item_name'] = item_name
    if request.GET.get('price'):
        price = request.GET.get('price')
        request.session['price'] = price
    if request.GET.get('discount_price'):
        discount_price = request.GET.get('discount_price')
        request.session['discount_price'] = discount_price
    if request.GET.get('kname'):
        kname = request.GET.get('kname')
        request.session['kname'] = kname

    oid = request.GET.get('oid') or request.session.get('oid')
    if not oid:
        oid = "ORD" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(10, 99))
        request.session['oid'] = oid

    if request.method=="POST":
        s1=request.POST.get("t1") # Order ID
        s2 = request.POST.get("t2") # Menu Item
        s3 = request.POST.get("t3") # Quantity
        s4 = request.POST.get("t4") # Unit Price
        s5 = request.POST.get("t5") # Total Price
        s6 = request.POST.get("t6") # Customization
        orderitem.objects.create(order=s1,menu_item=s2,quantity=s3,unit_price=s4,total_price=s5,customization=s6)
        request.session['oid'] = s1
        
        action = request.POST.get("action")
        if action == "add_item":
            if 'item_name' in request.session: del request.session['item_name']
            if 'price' in request.session: del request.session['price']
            return redirect('showkitchen')
        else:
            return redirect('insertorder')

    context = {
        'oid': oid,
        'item_name': item_name,
        'price': price,
        'discount_price': discount_price,
        'kname': kname,
    }
    return render(request,"orderitem.html", context)

def showorderitem(request):
    userdict=orderitem.objects.all()
    return render(request,"vieworderitem.html",{"userdict":userdict})

def delorderitem(request,pk):
    id = orderitem.objects.get(id=pk)
    id.delete()
    userdict = orderitem.objects.all()
    return render(request, "vieworderitem.html", {"userdict": userdict})

def insertdelivery(request):
    order_id = request.GET.get('order')
    if order_id:
        request.session['selected_order'] = order_id
    else:
        order_id = request.session.get('selected_order', '')
        
    delivery_address = request.session.get('selected_delivery_address', '')
    
    if request.method=="POST":
        s1=request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s8 = request.POST.get("t8")
        delivery.objects.create(order=s1,delivery_person=s2,pickup_time=s3,delivery_time=s4,estimated_time=s5,delivery_address=s6,delivery_fee=s7,status=s8)
        return render(request,"delivery.html")
        
    context = {
        'order': order_id,
        'delivery_address': delivery_address,
        'status': 'Sent out for delivery',
    }
    return render(request,"delivery.html", context)

def showdelivery(request):
    userdict=delivery.objects.all()
    return render(request,"viewdelivery.html",{"userdict":userdict})

def deldelivery(request,pk):
    id = delivery.objects.get(id=pk)
    id.delete()
    userdict = delivery.objects.all()
    return render(request, "viewdelivery.html", {"userdict": userdict})

def insertpayment(request):
    import datetime
    import random

    oid = request.session.get('oid', '')
    username = request.session.get('username', '')
    totamt = request.session.get('totamt', '0.00')
    
    # Generate Transactionid (TXN + 8 random digits)
    txn_id = "TXN" + "".join(str(random.randint(0, 9)) for _ in range(8))
    today = datetime.date.today().strftime('%Y-%m-%d')
    
    if request.method=="POST":
        s1=request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        payment.objects.create(order=s1,customer=s2,amount=s3,payment_method=s4,transaction_id=s5,payment_date=s6,status=s7)
        return redirect('payment_qrcode')
        
    context = {
        'oid': oid,
        'username': username,
        'totamt': totamt,
        'txn_id': txn_id,
        'today': today,
    }
    return render(request,"payment.html", context)

def showpayment(request):
    customer = request.GET.get('customer')
    delivery_address = request.GET.get('delivery_address')
    
    if customer:
        request.session['selected_customer'] = customer
    else:
        customer = request.session.get('selected_customer')
        
    if delivery_address:
        request.session['selected_delivery_address'] = delivery_address
    else:
        delivery_address = request.session.get('selected_delivery_address')
        
    if customer:
        userdict = payment.objects.filter(customer=customer)
    else:
        userdict = payment.objects.all()
        
    return render(request,"viewpayment.html",{"userdict":userdict})

def delpayment(request,pk):
    id = payment.objects.get(id=pk)
    id.delete()
    userdict = payment.objects.all()
    return render(request, "viewpayment.html", {"userdict": userdict})



def insertcoupon(request):
    if request.method=="POST":
        s1=request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s8 = request.POST.get("t8")
        s9 = request.POST.get("t9")
        s10 = request.POST.get("t10")
        s11 = request.POST.get("t11")
        coupon.objects.create(kitchen=s1,coupon_code=s2,description=s3,discount_type=s4,discount_value=s5,min_order_amount=s6,max_discount_amount=s7,valid_from=s8,valid_to=s9,usage_limit=s10,status=s11)
        return render(request,"coupon.html")
    return render(request,"coupon.html")

def showcoupon(request):
    userdict=coupon.objects.all()
    return render(request,"viewcoupon.html",{"userdict":userdict})

def delcoupon(request,pk):
    id = coupon.objects.get(id=pk)
    id.delete()
    userdict = coupon.objects.all()
    return render(request, "viewcoupon.html", {"userdict": userdict})




def insertingredient(request):
    kitchen_list = kitchen.objects.all()
    if request.method=="POST":
        s1=request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s8 = request.POST.get("t8")
        s9 = request.POST.get("t9")
        ingredient.objects.create(kitchen=s1,ingredient_name=s2,quantity_available=s3,unit=s4,reorder_level=s5,supplier_name=s6,last_restocked_date=s7,cost_per_unit=s8,status=s9)
        return render(request,"ingredient.html", {"kitchen_list": kitchen_list})
    return render(request,"ingredient.html", {"kitchen_list": kitchen_list})

def showingredient(request):
    userdict=ingredient.objects.all()
    return render(request,"viewingredient.html",{"userdict":userdict})

def delingredient(request,pk):
    id = ingredient.objects.get(id=pk)
    id.delete()
    userdict = ingredient.objects.all()
    return render(request, "viewingredient.html", {"userdict": userdict})

def insertreview(request):
    import datetime
    kitchen_list = kitchen.objects.all()
    menu_item_list = menuitem.objects.all()
    username = request.session.get('username', '')
    today = datetime.date.today().strftime('%Y-%m-%d')

    if request.method=="POST":
        s1 = request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        s7 = request.POST.get("t7")
        s8 = request.FILES.get("t8")
        review.objects.create(customer=s1,kitchen=s2,menu_item=s3,order=s4,rating=s5,review_text=s6,review_date=s7,photo=s8)
        return render(request,"review.html", {"kitchen_list": kitchen_list, "menu_item_list": menu_item_list, "username": username, "today": today})
    return render(request,"review.html", {"kitchen_list": kitchen_list, "menu_item_list": menu_item_list, "username": username, "today": today})

def showreview(request):
    userdict=review.objects.all()
    return render(request,"viewreview.html",{"userdict":userdict})

def delreview(request,pk):
    id = review.objects.get(id=pk)
    id.delete()
    userdict = review.objects.all()
    return render(request, "viewreview.html", {"userdict": userdict})

def insertnotification(request):
    if request.method=="POST":
        s1=request.POST.get("t1")
        s2 = request.POST.get("t2")
        s3 = request.POST.get("t3")
        s4 = request.POST.get("t4")
        s5 = request.POST.get("t5")
        s6 = request.POST.get("t6")
        notification.objects.create(user=s1,title=s2,message=s3,notification_date=s4,read_status=s5,notification_type=s6)
        return render(request,"notification.html")
    return render(request,"notification.html")

def shownotification(request):
    userdict=notification.objects.all()
    return render(request,"viewnotification.html",{"userdict":userdict})


def delnotification(request,pk):
    id = notification.objects.get(id=pk)
    id.delete()
    userdict = notification.objects.all()
    return render(request, "viewnotification.html", {"userdict": userdict})

def payment_qrcode(request):
    totamt = request.session.get('totamt', '0.00')
    oid = request.session.get('oid', '')
    return render(request, "payment_qrcode.html", {"totamt": totamt, "oid": oid})

def owner_showmenucategory(request):
    userdict = menucategory.objects.all()
    return render(request, "owner_viewmenucategory.html", {"userdict": userdict})

def owner_delmenucategory(request, pk):
    id = menucategory.objects.get(id=pk)
    id.delete()
    return redirect('owner_showmenucategory')

def owner_updatemenucategory(request, pk):
    category = menucategory.objects.get(id=pk)
    if request.method == "POST":
        category.kitchen = request.POST.get("t1")
        category.category_name = request.POST.get("t2")
        category.description = request.POST.get("t3")
        category.display_order = request.POST.get("t4")
        category.status = request.POST.get("t5")
        category.save()
        return redirect('owner_showmenucategory')
    return render(request, "update_menucategory.html", {"category": category})

def owner_showmenuitem(request):
    userdict = menuitem.objects.all()
    return render(request, "owner_viewmenuitem.html", {"userdict": userdict})

def owner_delmenuitem(request, pk):
    id = menuitem.objects.get(id=pk)
    id.delete()
    return redirect('owner_showmenuitem')

def owner_updatemenuitem(request, pk):
    item = menuitem.objects.get(id=pk)
    if request.method == "POST":
        item.menuitem = request.POST.get("t1")
        item.category = request.POST.get("t2")
        item.item_name = request.POST.get("t3")
        item.description = request.POST.get("t4")
        item.price = request.POST.get("t5")
        item.discount_price = request.POST.get("t6")
        item.preparation_time = request.POST.get("t7")
        item.veg_non_veg = request.POST.get("t8")
        item.spice_level = request.POST.get("t9")
        if request.FILES.get("t10"):
            item.photo = request.FILES.get("t10")
        item.availability = request.POST.get("t11")
        item.save()
        return redirect('owner_showmenuitem')
    return render(request, "update_menuitem.html", {"item": item})
