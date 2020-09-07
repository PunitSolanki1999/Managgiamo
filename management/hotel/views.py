from django.shortcuts import render,redirect
from django.db.models import Q
import datetime
from random import randint
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
from .models import Hotel_Management, Hotel_Employee_Register, Hotel_Room_Register, Customer_Register, Bill

from .forms import Hotel_Employee_Register_Data, Hotel_Management_Data, Hotel_Room_Register_Data, Customer_Register_Data, Bill_Data, Update_Hotel_Room, Update_Employee, Employee_Leave, Update_Customer_Day, Customer_Checkout, Update_Hotel_Detail, Change_Hotel_Password

from all.models import User_Data

from datetime import date
# def logout(request,*args,**kwargs):
#     if request.session.has_key('hotel'):
#         del request.session['hotel']
#         return redirect('hotel:hotel-login')
#     else:
#         return redirect('hotel:hotel-login')

def hotel_register(request,*args,**kwargs):
    if request.session.has_key('user'):
        form = Hotel_Management_Data(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                instance = form.save(commit = False)
                user = User_Data.objects.get(mainkey = request.session['user'])
                user.management = user.management + 'hotel,'
                instance.mainkey = user.mainkey
                instance.username = user.username
                instance.password = user.password
                instance.superkey = instance.registration_no
                instance.save()
                user.save()
                request.session['hotel'] = instance.superkey
                return redirect('hotel:hotel-interface')
        context = {
            'form': form,
        }
        return render(request,'hotel/hotel_register.html',context)
    else:
        return redirect('all:user-login')

# def hotel_login(request,*args,**kwargs):
#     if request.session.has_key("hotel"):
#         return redirect("hotel:hotel-interface")
#     form = Hotel_Management_Data(request.POST or None)
#     username_not_available = False
#     password_not_available = False
#     if request.method == 'POST':
#         data = request.POST.copy()
#         username = data.get('username')
#         password = data.get('password')
#         print(password)
#         try:
#             user = Hotel_Management.objects.get(username = username)
#             if user.username == username and user.password == password:
#                 request.session['hotel'] = user.superkey
#                 return redirect('hotel:hotel-interface')
#             else:
#                 password_not_available = True
#         except Exception:
#             username_not_available = True
#     context = {
#         'form': form,
#         'username_not_available': username_not_available,
#         'password_not_available': password_not_available,
#     }
#     return render(request,'hotel/hotel_login.html',context)

def hotel_interface(request):
    if request.session.has_key('user'):
        if request.session.has_key("hotel"):
            key = request.session['hotel']
            room_booked = Hotel_Room_Register.objects.filter(Q(superkey__iexact=key) & Q(available__iexact=0)).count()
            room = Hotel_Room_Register.objects.filter(Q(superkey__iexact=key)).count()
            employee = Hotel_Employee_Register.objects.filter(Q(superkey__iexact=key)).count()
            context = {
                'room_booked': room_booked,
                'room':room,
                'employee':employee,
            }
            return render(request,'hotel/hotel_interface.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def hotel_room_register(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key("hotel"):
            room_already = False
            form = Hotel_Room_Register_Data(request.POST or None)
            if request.method == "POST":
                if form.is_valid():
                    key = request.session['hotel']
                    instance = form.save(commit = False)
                    room = Hotel_Room_Register.objects.filter(Q(superkey__iexact = key))
                    instance.superkey = key
                    instance.room_id = (key + "RI" + instance.room_no)
                    for i in room:
                        if i.room_no == instance.room_no:
                            room_already = True
                    if room_already == False:
                        instance.save()
                        return redirect("hotel:hotel-room-register")
            context = {
                'form': form,
                'room_already': room_already,
            }
            return render(request,'hotel/hotel_room_register.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_hotel_room_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key("hotel"):
            confirm = False
            room = None
            if request.method == "POST":
                data = request.POST.copy()
                search = data.get('search')
                key = request.session['hotel']
                room = Hotel_Room_Register.objects.filter(Q(superkey__iexact = key) & Q(room_id__icontains = search))
                confirm = True
            context = {
                'room': room,
                'confirm': confirm,
            }
            return render(request,'hotel/update_hotel_room_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_hotel_room(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('hotel'):
            if pk != None:
                form = Update_Hotel_Room(request.POST or None)
                room = Hotel_Room_Register.objects.get(pk=pk)
                form.fields['room_type'].initial = room.room_type
                form.fields['room_cost'].initial = room.room_cost
                form.fields['ac'].initial        = room.ac
                form.fields['available'].initial = room.available
                if request.method == "POST":
                    if form.is_valid():
                        instance = form.save(commit = False)
                        room.room_type  = instance.room_type
                        room.room_cost  = instance.room_cost
                        room.ac         = instance.ac       
                        room.available  = instance.available
                        room.save()
                        return redirect('hotel:hotel-interface')
                context = {
                    'form': form,
                }
                return render(request,"hotel/update_hotel_room.html",context)
            else:
                return redirect('hotel:update-hotel-room-form')
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def hotel_room_detail_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key("hotel"):
            confirm = False
            room = None
            if request.method == "POST":
                data = request.POST.copy()
                room_id = data.get('room_id')
                room_type = data.get('room_type')
                key = request.session['hotel']
                if((room_id != None) & (room_type != None)):
                    room = Hotel_Room_Register.objects.filter(Q(superkey__iexact = key) & Q(room_id__icontains = room_id) & Q(room_type__icontains = room_type))
                elif(room_id != None & room_type == None):
                    room = Hotel_Room_Register.objects.filter(Q(superkey__iexact = key) & Q(room_id__icontains = room_id))
                elif(room_id == None & room_type != None):
                    room = Hotel_Room_Register.objects.filter(Q(superkey__iexact = key) & Q(room_type__icontains = room_id))
                else:
                    room = Hotel_Room_Register.objects.filter(Q(superkey__iexact = key) & Q(room_id__icontains = room_id))
                confirm = True
            context = {
                'room': room,
                'confirm': confirm,
            }
            return render(request,'hotel/hotel_room_detail_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def hotel_room_detail(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('hotel'):
            if pk != None:
                room = Hotel_Room_Register.objects.get(pk=pk)
                context = {
                    'room': room,
                }
                return render(request,"hotel/hotel_room_detail.html",context)
            else:
                return redirect('hotel:hotel-room-detail-form')
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def hotel_employee_register(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key("hotel"):
            form = Hotel_Employee_Register_Data(request.POST or None , request.FILES or None)
            if request.method == "POST":
                if form.is_valid():
                    key = request.session['hotel']
                    instance = form.save(commit = False)
                    employee = Hotel_Employee_Register.objects.filter(Q(superkey__iexact = key))
                    instance.superkey = key
                    count = len(employee)
                    count = count + 1
                    instance.employee_id = (key + "EI" + str(count))
                    if 'profile_pic' in request.FILES:
                            instance.picture = request.FILES['profile_pic']
                    instance.save()
                    return redirect("hotel:hotel-employee-register")
            form.fields['from_date'].initial = datetime.date.today()
            context = {
                'form': form,
            }
            return render(request,'hotel/hotel_employee_register.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_employee_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('hotel'):
            confirm = False
            employee = None
            if request.method == 'POST':
                data = request.POST.copy()
                search = data.get('search')
                key = request.session['hotel']
                employee = Hotel_Employee_Register.objects.filter(Q(superkey__iexact = key) & Q(employee_id__icontains = search))
                confirm = True
            context = {
                'employee': employee,
                'confirm': confirm,
            }
            return render(request,'hotel/update_employee_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_employee(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('hotel'):
            if(pk != None):
                employee = Hotel_Employee_Register.objects.get(employee_id = pk)
                form = Update_Employee(request.POST or None , request.FILES or None)
                form.fields['fname'].initial        = employee.fname              
                form.fields['mname'].initial        = employee.mname              
                form.fields['lname'].initial        = employee.lname              
                form.fields['phone'].initial        = employee.phone        
                form.fields['father_name'].initial  = employee.father_name 
                form.fields['father_phone'].initial = employee.father_phone
                form.fields['mother_name'].initial  = employee.mother_name 
                form.fields['mother_phone'].initial = employee.mother_phone       
                form.fields['designation'].initial         = employee.designation            
                form.fields['emailid'].initial      = employee.emailid   
                form.fields['dob'].initial          = employee.dob           
                form.fields['salary'].initial       = employee.salary          
                form.fields['state'].initial        = employee.state                             
                form.fields['city'].initial         = employee.city        
                form.fields['pincode'].initial      = employee.pincode     
                form.fields['address'].initial      = employee.address     
                form.fields['picture'].initial      = employee.picture
                if request.method == 'POST':
                    if form.is_valid():
                        instance = form.save(commit = False)
                        employee.fname        = instance.fname       
                        employee.mname        = instance.mname       
                        employee.lname        = instance.lname       
                        employee.phone        = instance.phone       
                        employee.father_name  = instance.father_name 
                        employee.father_phone = instance.father_phone
                        employee.mother_name  = instance.mother_name 
                        employee.mother_phone = instance.mother_phone
                        employee.designation         = instance.designation      
                        employee.emailid      = instance.emailid  
                        employee.dob          = instance.dob         
                        employee.salary       = instance.salary      
                        employee.state        = instance.state       
                        employee.city         = instance.city        
                        employee.pincode      = instance.pincode     
                        employee.address      = instance.address    
                        if 'profile_pic' in request.FILES:
                            instance.picture = request.FILES['profile_pic']
                        employee.picture      = instance.picture 
                        employee.save()      
                        return redirect('hotel:update-employee-form') 
                context = {
                    'form': form,
                    'employee': employee,
                }    
            else:
                return redirect('hotel:update-employee-form')
            return render(request,'hotel/update_employee.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_employee_leave_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('hotel'):
            confirm = False
            employee = None
            if request.method == 'POST':
                data = request.POST.copy()
                search = data.get('search')
                key = request.session['hotel']
                employee = Hotel_Employee_Register.objects.filter(Q(superkey__iexact = key) & Q(employee_id__icontains = search))
                confirm = True
            context = {
                'employee': employee,
                'confirm': confirm,
            }
            return render(request,'hotel/update_employee_leave_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_employee_leave(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('hotel'):
            if(pk != None):
                employee = Hotel_Employee_Register.objects.get(employee_id = pk)
                form = Employee_Leave(request.POST or None)
                form.fields['to_date'].initial = datetime.date.today()                 
                if request.method == 'POST':
                    if form.is_valid():
                        instance = form.save(commit = False)
                        employee.to_date    = instance.to_date       

                        employee.save()  
                        return redirect('hotel:update-employee-leave-form')     
                context = {
                    'form': form,
                    'employee': employee,
                }    
            else:
                return redirect('hotel:update-employee-leave-form')
            return render(request,'hotel/update_employee_leave.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def hotel_account_detail(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('hotel'):
            key = request.session['hotel']
            user = Hotel_Management.objects.get(superkey = key)
            context = {
                'user': user,
            }
            return render(request,'hotel/hotel_account_detail.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def customer_checkin(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('hotel'):
            if pk != None:
                room_already = False
                form = Customer_Register_Data(request.POST or None)
                room = Hotel_Room_Register.objects.get(room_id__iexact = pk)
                form.fields['room_id'].initial = room.room_id
                if request.method == "POST":
                    if form.is_valid():
                        key = request.session['hotel']
                        instance = form.save(commit = False)
                        if room.available == False:
                            room_already = True
                        if room_already == False:
                            customer = Customer_Register.objects.filter(Q(superkey__iexact = key))
                            count = len(customer) + 1
                            instance.superkey = key
                            instance.customer_id = (key + "CI" + str(count))
                            room.available = False
                            room.save()
                            instance.save()
                            return redirect("hotel:hotel-room-detail-form")
                form.fields['checkin_date'].initial = datetime.date.today()
                context = {
                    'form': form,
                    'room': room,
                }
                return render(request,'hotel/customer_checkin.html',context)
            else:
                return redirect("hotel:hotel-interface")
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_days_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('hotel'):
            confirm = False
            customer = None
            if request.method == "POST":
                data = request.POST.copy()
                customer_id = data.get('customer_id')
                room_id = data.get('room_id')
                key = request.session['hotel']
                if((customer_id != None) & (room_id != None)):
                    customer = Customer_Register.objects.filter(Q(superkey__iexact = key) & Q(customer_id__icontains = customer_id) & Q(room_id__icontains = room_id))
                elif((customer_id != None) & (room_id == None)):
                    customer = Customer_Register.objects.filter(Q(superkey__iexact = key) & Q(customer_id__icontains = customer_id))
                elif((customer_id == None) & (room_id != None)):
                    customer = Customer_Register.objects.filter(Q(superkey__iexact = key) & Q(room_id__icontains = room_id))
                confirm = True
            context = {
                'confirm': confirm,
                'customer': customer,
            }
            return render(request,'hotel/update_days_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_days(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('hotel'):
            if pk != None:
                form = Update_Customer_Day(request.POST or None)
                customer = Customer_Register.objects.get(pk=pk)
                room = Hotel_Room_Register.objects.get(room_id = customer.room_id)
                form.fields['addar_no'].initial     = customer.addar_no
                form.fields['room_id'].initial      = customer.room_id
                form.fields['fname'].initial        = customer.fname
                form.fields['mname'].initial        = customer.mname
                form.fields['lname'].initial        = customer.lname
                form.fields['no_of_days'].initial   = customer.no_of_days
                form.fields['cost'].initial         = customer.cost
                form.fields['phone'].initial        = customer.phone
                form.fields['address'].initial      = customer.address
                form.fields['amount_paid'].initial  = customer.amount_paid
                form.fields['checkin_date'].initial = customer.checkin_date
                if request.method == "POST":
                    if form.is_valid():
                        instance = form.save(commit = False)
                        customer.addar_no       = instance.addar_no               
                        customer.room_id        = instance.room_id                
                        customer.fname          = instance.fname              
                        customer.mname          = instance.mname              
                        customer.lname          = instance.lname              
                        customer.no_of_days     = instance.no_of_days             
                        customer.cost           = instance.cost               
                        customer.phone          = instance.phone              
                        customer.address        = instance.address                
                        customer.amount_paid    = instance.amount_paid            
                        customer.checkin_date   = instance.checkin_date   
                        customer.save() 
                        return redirect("hotel:hotel-interface")           
                context = {
                    'room': room,
                    'form': form,
                    'customer': customer,
                }
                return render(request,'hotel/update_days.html',context)

            else:
                return redirect("hotel:update-days-form")
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')
    
def customer_checkout_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('hotel'):
            confirm = False
            customer = None
            if request.method == "POST":
                data = request.POST.copy()
                customer_id = data.get('customer_id')
                room_id = data.get('room_id')
                key = request.session['hotel']
                if((customer_id != None) & (room_id != None)):
                    customer = Customer_Register.objects.filter(Q(superkey__iexact = key) & Q(customer_id__icontains = customer_id) & Q(room_id__icontains = room_id))
                elif((customer_id != None) & (room_id == None)):
                    customer = Customer_Register.objects.filter(Q(superkey__iexact = key) & Q(customer_id__icontains = customer_id))
                elif((customer_id == None) & (room_id != None)):
                    customer = Customer_Register.objects.filter(Q(superkey__iexact = key) & Q(room_id__icontains = room_id))
                confirm = True
            context = {
                'confirm': confirm,
                'customer': customer,
            }
            return render(request,'hotel/customer_checkout_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def customer_checkout(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('hotel'):
            if pk != None:
                form = Customer_Checkout(request.POST or None)
                form1 = Bill_Data(request.POST or None)
                customer = Customer_Register.objects.get(pk=pk)
                if request.method == "POST":
                    if form.is_valid():
                        instance = form.save(commit = False)
                        instance1 = form1.save(commit = False)
                        key = request.session['hotel']
                        data = request.POST.copy()
                        extra = data.get('extra')
                        work_type   = data.get('work_type')
                        room = Hotel_Room_Register.objects.get(room_id = customer.room_id)

                        bill = Bill.objects.filter(Q(superkey__iexact = key))
                        count = len(bill) + 1
                        customer.checkout_date = instance.checkout_date

                        instance1.superkey = key
                        instance1.bill_no = ( key + "BI" + str(count))
                        instance1.room_id = customer.room_id
                        instance1.no_of_days = customer.no_of_days
                        instance1.customer_id = customer.customer_id
                        instance1.cost      = customer.cost
                        instance1.extra     = extra
                        instance1.type_of_work = work_type
                        instance1.day_out   = date.today()
                        print(date.today())
                        instance1.save()
                        room.available = True
                        room.save()
                        customer.save()
                        return redirect('hotel:bill-generation',pk=instance1.bill_no)
                form.fields['checkout_date'].initial = datetime.date.today()         
                context = {
                    'form1': form,
                    'form': form,
                    'customer': customer,
                }
                return render(request,"hotel/customer_checkout.html",context)
            else:
                return redirect("hotel:customer-checkout-form")
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def bill_detail(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('hotel'):
            confirm = False
            bill = None
            if request.method == "POST":
                data = request.POST.copy()
                bill_no = data.get("bill_no")
                key = request.session['hotel']
                bill = Bill.objects.filter(Q(superkey__iexact = key) & Q(bill_no__icontains = (key + "BI" + bill_no)))
                confirm = True
            context = {
                'confirm': confirm,
                'bill': bill,
            }
            return render(request,'hotel/bill_detail.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def customer_detail_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('hotel'):
            confirm = False
            customer = None
            if request.method == "POST":
                data = request.POST.copy()
                customer_id = data.get('customer_id')
                key = request.session['hotel']
                customer = Customer_Register.objects.filter(Q(superkey__iexact = key) & Q(customer_id__icontains = customer_id))
                confirm = True
            context = {
                'confirm': confirm,
                'customer': customer,
            }
            return render(request,'hotel/customer_detail_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def customer_detail(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('hotel'):
            if pk != None:
                customer = Customer_Register.objects.get(pk=pk)
                context = {
                    'customer': customer,
                }
                return render(request,'hotel/customer_detail.html',context)
            else:
                return redirect("hotel:customer-detail-form")
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def employee_detail_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('hotel'):
            confirm = False
            context = {
                'confirm': confirm,
            }
            if request.method == 'POST':
                data = request.POST.copy()
                search = data.get('search')
                superk = request.session['hotel']
                employee = Hotel_Employee_Register.objects.filter(Q(superkey__iexact = superk) & Q(employee_id__icontains = search))
                confirm = True
                context = {
                    'employee': employee,
                    'confirm': confirm,
                }
            return render(request,'hotel/employee_detail_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def employee_detail(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('hotel'):
            context = {}
            if(pk != None):
                employee = Hotel_Employee_Register.objects.get(employee_id = pk)
                context = {
                    'employee': employee,
                }
            else:
                return redirect('hotel:employee-detail-form')
            return render(request,'hotel/employee_detail.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def bill_generation(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('hotel'):
            if pk != None :
                key = request.session['hotel']
                bill = Bill.objects.get(pk=pk)
                hotel = Hotel_Management.objects.get(pk=key)
                context = {
                    'bill': bill,
                    'hotel': hotel,
                }
                return render(request,"hotel/bill.html",context)
            else:
                return redirect("hotel:bill-detail")
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_hotel_detail(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('hotel'):
            key = request.session['hotel']
            form = Update_Hotel_Detail(request.POST or None)
            hotel = Hotel_Management.objects.get(pk=key)
            form.fields['emailid'].initial = hotel.emailid
            form.fields['phone'].initial = hotel.phone
            form.fields['hotel_name'].initial = hotel.hotel_name
            form.fields['state'].initial = hotel.state
            form.fields['city'].initial = hotel.city
            form.fields['pincode'].initial = hotel.pincode
            form.fields['address'].initial = hotel.address
            if request.method == "POST":
                if form.is_valid():
                    instance = form.save(commit=False)
                    hotel.emailid = instance.emailid
                    hotel.phone = instance.phone
                    hotel.address = instance.address
                    hotel.save()
                    return redirect('hotel:hotel-account-detail')
            context = {
                'form': form,
            }
            return render(request,'hotel/update_hotel_detail.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

# def username(request,*args,**kwargs):
#     username_not = False
#     if request.method == "POST":
#         data = request.POST.copy()
#         username = data.get('username')
#         try:
#             user = Hotel_Management.objects.get(username=username)
#             return redirect('hotel:otp-verification',username)
#         except:
#             username_not = True
#     return render(request,'hotel/username.html',{'username_not':username_not})

# def otp_verification(request,username=None,*args,**kwargs):
#     if request.session.has_key('hotel'):
#         key = request.session['hotel']
#         hotel = Hotel_Management.objects.get(superkey=key)
#     elif username != None:
#         hotel = Hotel_Management.objects.get(username=username)
#     else:
#         return redirect('hotel:username')
#     otp = randint(100000,999999)
#     subject = "[MANAGGIAMO] Account Verification Code."
#     message = ("Hey " + str(hotel.username) + "\nThe changing password attempt require futher verfication because we did not recognize your decive. To Complete the verification enter code on the unrecognized device.\nVerification Code: " + str(otp))
#     email_from = settings.EMAIL_HOST_USER
#     email = hotel.emailid
#     recipient_list = [email,]
#     send_mail( subject, message, email_from, recipient_list )
#     return redirect('hotel:otp',otp,hotel)

# def otp_confirm(request,otp=None,hotel=None,*args,**kwargs):
#     if otp == None or hotel == None:
#         return redirect("hotel:otp-verification")
#     confirm = False
#     otp_not = False
#     hotel = Hotel_Management.objects.get(username=hotel)
#     if request.method == "POST":
#         confirm = True
#         data = request.POST.copy()
#         otp_verification = data.get('otp')
#         if int(otp) == int(otp_verification):
#             request.session['hotel_otp'] = hotel.username
#             return redirect('hotel:change-password')
#         else:
#             otp_not = True
#     context = {
#         'hotel': hotel,
#         'confirm': confirm,
#         'otp': otp_not,
#     }
#     return render(request,'hotel/opt_verification.html',context)

# def change_password(request,*args,**kwargs):
#     if request.session.has_key('hotel_otp'):
#         form = Change_Hotel_Password(request.POST or None)
#         if request.method == "POST":
#             username = request.session['hotel_otp']
#             hotel = Hotel_Management.objects.get(username=username)
#             if form.is_valid():
#                 instance = form.save(commit=False)
#                 hotel.password = instance.password
#                 hotel.save()
#                 del request.session['hotel_otp']
#                 return redirect('hotel:hotel-login')
#         context = {
#             'form': form,
#         }
#         return render(request,'hotel/change_password.html',context)
#     else:
#         if request.session.has_key('hotel'):
#             key = request.session['hotel']
#             hotel = Hotel_Management.objects.get(superkey=key)
#             return redirect('hotel:otp-verification',hotel.username)
#         else:
#             return redirect('hotel:username')