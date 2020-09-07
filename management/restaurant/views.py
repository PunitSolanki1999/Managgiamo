from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.db.models import Q
import datetime
from django.core.mail import send_mail
from django.conf import settings
from random import randint
# Create your views here.
from .models import Rest_Employee, Rest_Food, Rest_Management, Ingredient_Table, Bill, Bill_Product

from .forms import Rest_Management_Detail, Rest_Employee_Detail, Rest_Food_Detail, Ingredient_Detail, Bill_Detail, Update_Employee, Employee_Leave, Update_Ingredient_Detail, Bill_Product_Detail, Change_Rest_Password, Update_Rest_Detail

from all.models import User_Data

# def logout(request,*args,**kwargs):
#     if request.session.has_key('rest'):
#         del request.session['rest']
#         return redirect('rest:rest-login')
#     else:
#         return redirect('rest:rest-login')
def rest_register(request,*args,**kwargs):
    if request.session.has_key('user'):
        form = Rest_Management_Detail(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                instance = form.save(commit = False)
                user = User_Data.objects.get(mainkey = request.session['user'])
                user.management = user.management + 'rest,'
                instance.username = user.username
                instance.password = user.password
                instance.mainkey = user.mainkey
                instance.superkey = instance.license_no
                instance.save()
                user.save()
                request.session['rest'] = instance.superkey
                return redirect('rest:rest-interface')
        context = {
            'form': form,
        }
        return render(request,'rest/rest_register.html',context)
    else:
        return redirect('all:user-login')

# def rest_login(request,*args,**kwargs):
#     if request.session.has_key("rest"):
#         return redirect("rest:rest-interface")
#     username_not_available = False
#     password_not_available = False
#     if request.method == 'POST':
#         data = request.POST.copy()
#         username = data.get('username')
#         password = data.get('password')
#         try:
#             user = Rest_Management.objects.get(username = username)
#             if user.username == username and user.password == password:
#                 request.session['rest'] = user.superkey
#                 return redirect('rest:rest-interface')
#             else:
#                 password_not_available = True
#         except Exception:
#             username_not_available = True
#     context = {
#         'username_not_available': username_not_available,
#         'password_not_available': password_not_available,
#     }
#     return render(request,'rest/rest_login.html',context)

def rest_interface(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('rest'):
            key = request.session['rest']
            employee = Rest_Employee.objects.filter(Q(superkey__iexact=key)).count()
            food = Rest_Food.objects.filter(Q(superkey__iexact=key)).count()
            ingredient = Ingredient_Table.objects.filter(Q(superkey__iexact=key) & Q(available__gt=0)).count()
            context = {
                'ingredient':ingredient,
                'food':food,
                'employee': employee,
            }
            return render(request,'rest/rest_interface.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def rest_employee_register(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key("rest"):
            form = Rest_Employee_Detail(request.POST or None , request.FILES or None)
            if request.method == "POST":
                if form.is_valid():
                    key = request.session['rest']
                    instance = form.save(commit = False)
                    employee = Rest_Employee.objects.filter(Q(superkey__iexact = key))
                    instance.superkey = key
                    count = len(employee)
                    count = count + 1
                    instance.employee_id = (key + "EI" + str(count))
                    if 'profile_pic' in request.FILES:
                        instance.picture = request.FILES['profile_pic']
                    instance.save()
                    return redirect("rest:employee-detail",instance.pk)
            form.fields['from_date'].initial = datetime.date.today()
            context = {
                'form': form,
            }
            return render(request,'rest/rest_employee_register.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def rest_account_detail(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('rest'):
            key = request.session['rest']
            user = Rest_Management.objects.get(superkey = key)
            context = {
                'user': user,
            }
            return render(request,'rest/rest_account_detail.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_employee_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('rest'):
            confirm = False
            employee = None
            if request.method == 'POST':
                data = request.POST.copy()
                search = data.get('search')
                key = request.session['rest']
                employee = Rest_Employee.objects.filter(Q(superkey__iexact = key) & Q(employee_id__icontains = search))
                confirm = True
            context = {
                'employee': employee,
                'confirm': confirm,
            }
            return render(request,'rest/update_employee_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_employee(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('rest'):
            if(pk != None):
                employee = Rest_Employee.objects.get(employee_id = pk)
                form = Update_Employee(request.POST or None , request.FILES or None)
                form.fields['fname'].initial        = employee.fname              
                form.fields['mname'].initial        = employee.mname              
                form.fields['lname'].initial        = employee.lname              
                form.fields['phone'].initial        = employee.phone        
                form.fields['father_name'].initial  = employee.father_name 
                form.fields['father_phone'].initial = employee.father_phone     
                form.fields['work'].initial         = employee.work     
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
                        employee.work         = instance.work     
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
                        return redirect('rest:update-employee-form') 
                context = {
                    'form': form,
                    'employee': employee,
                }    
            else:
                return redirect('rest:update-employee-form')
            return render(request,'rest/update_employee.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_employee_leave_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('rest'):
            confirm = False
            employee = None
            if request.method == 'POST':
                data = request.POST.copy()
                search = data.get('search')
                key = request.session['rest']
                employee = Rest_Employee.objects.filter(Q(superkey__iexact = key) & Q(employee_id__icontains = search))
                confirm = True
            context = {
                'employee': employee,
                'confirm': confirm,
            }
            return render(request,'rest/update_employee_leave_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_employee_leave(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('rest'):
            if(pk != None):
                employee = Rest_Employee.objects.get(employee_id = pk)
                form = Employee_Leave(request.POST or None)
                if request.method == 'POST':
                    if form.is_valid():
                        instance = form.save(commit = False)
                        employee.to_date    = instance.to_date       
                        employee.save()  
                        return redirect('rest:update-employee-leave-form')     
                form.fields['to_date'].initial = datetime.date.today() 
                context = {
                    'form': form,
                    'employee': employee,
                }    
            else:
                return redirect('rest:update-employee-leave-form')
            return render(request,'rest/update_employee_leave.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def employee_detail_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('rest'):
            confirm = False
            context = {
                'confirm': confirm,
            }
            if request.method == 'POST':
                data = request.POST.copy()
                search = data.get('search')
                superk = request.session['rest']
                employee = Rest_Employee.objects.filter(Q(superkey__iexact = superk) & Q(employee_id__icontains = search))
                confirm = True
                context = {
                    'employee': employee,
                    'confirm': confirm,
                }
            return render(request,'rest/employee_detail_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def employee_detail(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('rest'):
            context = {}
            if(pk != None):
                employee = Rest_Employee.objects.get(employee_id = pk)
                context = {
                    'employee': employee,
                }
            else:
                return redirect('rest:employee-detail-form')
            return render(request,'rest/employee_detail.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def food_insert(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('rest'):
            food_already = False
            form = Rest_Food_Detail(request.POST or None)
            if request.method == "POST":
                if form.is_valid():
                    instance = form.save(commit = False)
                    key = request.session['rest']
                    food = Rest_Food.objects.filter(Q(superkey__iexact = key))
                    count = len(food) + 1
                    for i in food:
                        if i.food_name == instance.food_name:
                            food_already = True
                    if food_already == False:
                        instance.food_id = (key + "FI" + str(count))
                        instance.superkey = key
                        instance.save()
                        return redirect("rest:food-insert")
            context = {
                'food_already': food_already,
                'form': form,
            }
            return render(request,'rest/food_insert.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def ingredient_entry(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('rest'):
            ingredient_already = False
            form = Ingredient_Detail(request.POST or None)
            if request.method == "POST":
                if form.is_valid():
                    instance = form.save(commit = False)
                    key = request.session['rest']
                    ingredient = Ingredient_Table.objects.filter(Q(superkey__iexact = key))
                    for i in ingredient:
                        if i.ingredient_name == instance.ingredient_name:
                            ingredient_already = True
                    if ingredient_already == False:
                        instance.superkey = key
                        count = len(ingredient) + 1
                        instance.ingredient_id = (key + "II" + str(count))
                        instance.save()
                        return redirect('rest:ingredient-entry')
            context = {
                'form': form,
                'ingredient_alreay': ingredient_already,
            }
            return render(request,'rest/ingredient_entry.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_ingredient_detail_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('rest'):
            confirm = False
            ingredient = None
            if request.method == "POST":
                data = request.POST.copy()
                indgredient_name = data.get('ingredient_name')
                key = request.session['rest']
                ingredient = Ingredient_Table.objects.filter(Q(superkey__iexact = key) & Q(ingredient_name__icontains = indgredient_name))
                confirm = True
            context = {
                'confirm': confirm,
                'ingredient': ingredient,
            }
            return render(request,'rest/update_ingredient_detail_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')
    
def update_ingredient_detail(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('rest'):
            if pk != None:
                ingredient = Ingredient_Table.objects.get(pk=pk)
                form = Update_Ingredient_Detail(request.POST or None)
                form.fields['ingredient_name'].initial = ingredient.ingredient_name
                form.fields['total'].initial = ingredient.total
                form.fields['available'].initial = ingredient.available
                if request.method == "POST":
                    if form.is_valid():
                        instance = form.save(commit = False)
                        ingredient.total = instance.total
                        ingredient.available = instance.available
                        ingredient.save()
                        return redirect('rest:update-ingredient-detail-form')
                context = {
                    'form': form,
                    'ingredient': ingredient,
                }
                return render(request,'rest/update_ingredient_detail.html',context)
            else:
                return redirect("rest:update-ingredient-detail-form")
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def bill_data_entry(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('rest'):
            form = Bill_Detail(request.POST or None)
            if request.method == "POST":
                if form.is_valid():
                    instance = form.save(commit = False)
                    key = request.session['rest']
                    instance.superkey = key
                    bill = Bill.objects.filter(Q(superkey__iexact = key))
                    count = len(bill) + 1
                    instance.bill_id = (key + "BI" + str(count))
                    instance.save()
                    return redirect('rest:bill-food-entry',pk=instance.bill_id)
            context = {
                'form': form,
            }
            return render(request,'rest/bill_data_entry.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def bill_food_entry(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('rest'):
            if pk != None:
                bill = Bill.objects.get(pk = pk)
                bill_detail = Bill_Product.objects.filter(Q(superkey__iexact = bill.superkey) & Q(bill_id__iexact = bill.bill_id))
                form = Bill_Product_Detail(request.POST or None)
                if request.method == "POST":
                    if form.is_valid():
                        instance = form.save(commit = False)
                        food = Rest_Food.objects.get(food_id = instance.food_id)
                        instance.superkey = bill.superkey
                        instance.bill_id = bill.bill_id
                        instance.table_no = bill.table_no
                        instance.price = int(food.price) * int(instance.quantity) 
                        instance.save()
                        return redirect('rest:bill-food-entry',pk=bill.bill_id)
                context = {
                    'form': form,
                    'bill': bill,
                    'bill_detail': bill_detail,
                }
                return render(request,'rest/bill_food_entry.html',context)
            else:
                return redirect('rest:bill-data-entry')
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def bill_final(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('rest'):
            if pk != None:
                key = request.session['rest']
                bill = Bill_Product.objects.filter(Q(superkey__iexact = key) & Q(bill_id__iexact = pk))
                total_price = 0
                for i in bill:
                    total_price = total_price + i.price
                context = {
                    'bill': bill,
                    'total_price': total_price,
                }
                return render(request,'rest/bill_final.html',context)
            else:
                return redirect('rest:bill-detail-entry')
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def bill_search(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('rest'):
            confirm = False
            bill = None
            if request.method == "POST":
                data = request.POST.copy()
                key = request.session['rest']
                bill_id = data.get('bill_id')
                bill = Bill.objects.filter(Q(superkey__iexact = key) & Q(bill_id__icontains = (key + "BI" + str(bill_id))))
                confirm = True
            context = {
                'confirm': confirm,
                'bill': bill,
            }
            return render(request,'rest/bill_search.html',context)
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
#             user = Rest_Management.objects.get(username=username)
#             return redirect('rest:otp-verification',username)
#         except:
#             username_not = True
#     return render(request,'rest/username.html',{'username_not':username_not})

# def otp_verification(request,username=None,*args,**kwargs):
#     if request.session.has_key('rest'):
#         key = request.session['rest']
#         rest = Rest_Management.objects.get(superkey=key)
#     elif username != None:
#         rest = Rest_Management.objects.get(username=username)
#     else:
#         return redirect('rest:username')
#     otp = randint(100000,999999)
#     subject = "[MANAGGIAMO] Account Verification Code."
#     message = ("Hey " + str(rest.username) + "\nThe changing password attempt require futher verfication because we did not recognize your decive. To Complete the verification enter code on the unrecognized device.\nVerification Code: " + str(otp))
#     email_from = settings.EMAIL_HOST_USER
#     email = rest.emailid
#     recipient_list = [email,]
#     send_mail( subject, message, email_from, recipient_list )
#     return redirect('rest:otp',otp,rest)

# def otp_confirm(request,otp=None,rest=None,*args,**kwargs):
#     if(otp == None or rest == None):
#         return redirect("rest:otp-verification",rest)
#     confirm = False
#     otp_not = False
#     rest = Rest_Management.objects.get(username=rest)
#     if request.method == "POST":
#         confirm = True
#         data = request.POST.copy()
#         otp_verification = data.get('otp')
#         if int(otp) == int(otp_verification):
#             request.session['rest_otp'] = rest.username
#             return redirect('rest:change-password')
#         else:
#             otp_not = True
#     context = {
#         'rest': rest,
#         'confirm': confirm,
#         'otp': otp_not,
#     }
#     return render(request,'rest/opt_verification.html',context)

# def change_password(request,*args,**kwargs):
#     if request.session.has_key('rest_otp'):
#         form = Change_Rest_Password(request.POST or None)
#         if request.method == "POST":
#             username = request.session['rest_otp']
#             rest = Rest_Management.objects.get(username=username)
#             if form.is_valid():
#                 instance = form.save(commit=False)
#                 rest.password = instance.password
#                 rest.save()
#                 del request.session['rest_otp']
#                 return redirect('rest:rest-login')
#         context = {
#             'form': form,
#         }
#         return render(request,'rest/change_password.html',context)
#     else:
#         if request.session.has_key('rest'):
#             key = request.session['rest']
#             rest = Rest_Management.objects.get(superkey=key)
#             return redirect('rest:otp-verification',rest.username)
#         else:
#             return redirect('rest:username')

def update_rest_detail(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('rest'):
            key = request.session['rest']
            form = Update_Rest_Detail(request.POST or None)
            rest = Rest_Management.objects.get(superkey=key)
            form.fields['emailid'].initial = rest.emailid
            form.fields['phone'].initial = rest.phone
            form.fields['rest_name'].initial = rest.rest_name
            form.fields['state'].initial = rest.state
            form.fields['city'].initial = rest.city
            form.fields['pincode'].initial = rest.pincode
            form.fields['address'].initial = rest.address
            if request.method == "POST":
                if form.is_valid():
                    instance = form.save(commit=False)
                    rest.emailid = instance.emailid
                    rest.phone = instance.phone
                    rest.address = instance.address
                    rest.save()
                    return redirect('rest:rest-account-detail')
            context = {
                'form': form,
            }
            return render(request,'rest/update_rest_detail.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

import pandas as pd 
import numpy as np 
from nltk.stem.porter import PorterStemmer
def predict(request,*args,**kwargs):
    k = pd.read_excel(r"C:\Users\Asus\Downloads\dataset.xlsx")
    print(k)
    l = ['Khandwa','Rajendra Nagar','Pithampur','Saket Nagar','Kalyani Nagar','Limbodi','A.B. Road','Annapurna Road','Khajuri Bazar','Race Course Road','Chhawani','Khatiwala Tank','Rajwada','Dhar Road','Maharani Road','RNT Marg','Sector 23-D','Depalpur','Datoda','Dakachia','Chordia','Choral','Chittoda','Burankhedi','Binawda','Bhatkhedi','Bai','Badodia Khan','Bachhoda','Aurangpura','Atwada','Attahada','Ambachandan','Alwasa','Ajnod','Barlai Jagir','Baoliakhurd','Badgonda','Bhagora','Bhanwrasala','Bhilbadoli','Banadia','Army Headquarters','Baloda Tkun','Chadoda','Indore Agrawal Nagar','Indore Badwali Chowk','Indore Bajasan Road','Bicholi Mardana','Biyabani','CGO Complex','Cloth Market','Dhannad','Dharnaka','Dudhia','Farkodha','Fatahabad Chandrawatiganj','FC Ganj Edso','Gandhi Nagar-Indore','Gautampura','Gawali Palasia','Girota','Gokulpur','Gujarkheda','Guran','Gurunanak Chowk','Harsola','Hasalpur','Army','Collectorate','Courts','Jail Road','Javeri Bagh','Cantt','Khajrana','Kumar Khadi','Lokmanya Nagar','Malharganj','Malwa Mill','Manorama Ganj','Mills','Nanda Nagar','Palasiya','Pardesipura','RSS Nagar','Indore Rajendra Nagar','Rajmohalla','Rambagh','Siyaganj','Topkhana','Srinagar Colony','Tukoganj','VS Market','Uchchanyayalay','Yeshwant Road','Jalodiyagyan','Jambudi Hapsi','Simrol','Palakhedi','Palda','Paliya','Panod','Pedmi','Pigdamber','Pipalda','Piwdai','Radio Colony Indore','Rajendra Nagar-Indore','Rangwasa','Jinda Kheda','Rolai','Sadar Bazar','Juni Indore','Kadwali Buzurg','Sagdod','Sanawadia','Kanadia','Kanadia Road','Sanwer Link Road','Sanwer','Khatiwala Tank-Indore','Khurdi','Sivani','Kodria','Krishnaganj','Solsinda','Kudana','Sudama Nagar','Lasudia','Tilak Nagar','Tillor Khurd','Tillorbujurg','Limbiodapar','Todi','Lokmanya Nagar','Machal','Vallabh Nagar','Machla','Vijay Nagar','Maithwada','Yashwant Nagar','Manglia','Manpur','Jamli','Nanda Nagar-Indore','Pagnispaga Indore','Jhalaria','Biyabani-Indore','Kankaripal','DDU Nagar','Kanwasa','Indore Nagar','Kelod Kartal','Ravi Shankar Shukla Nagar','Kalaria','Khajrana','Kallibillod','Murkheda','Kalmer','Sawer','Sumtha','Kampel','Bhavarkua','piplihana chouraha','bengali chouraha','navlakha chouraha','grand exotica','tilik nagar','geeta bhawan','LIG','rajiv gandhi','navlakha','M.Y.','palasia']
    corpus = []
    y = []
    area = Rest_Management.objects.get(superkey = request.session['rest'])
    area = area.address
    area = area.split(',')
    ps = PorterStemmer()
    area = [ps.stem(word) for word in area if word.strip() in set(l)]
    area = ' '.join(area)
    area = area.strip()
    print("area:",area)
    for i in range(len(l)):
        l[i] = l[i].lower()
    for i in range(len(k)):
        p = str(k['address'][i])
        y.append([p.lower()])
    for i in range(len(k)):
        review = y[i][0]
        review = review.lower()
        review = review.split(',')
        ps = PorterStemmer()
        review = [ps.stem(word) for word in review if word.strip() in set(l)]
        review = ' '.join(review)
        review = review.strip()
        corpus.append(review)
    u = []
    for i in range(len(corpus)):
        if corpus[i] != '':
            u.append(corpus[i])
        else:
            u.append(np.NAN)
    print(u)
    for i in range(len(u)):
        k['address'][i] = u[i]
    print(k)
    # print(corpus)
    # corpus = pd.DataFrame({'area':u,'area_name':u})
    # corpus = corpus.dropna()
    # print(corpus)
    # x = corpus.iloc[:,1].values
    # y = corpus.iloc[:,0:1].values
    # from sklearn.preprocessing import LabelEncoder
    # label = LabelEncoder()
    # y[:,0] = label.fit_transform(y[:,0])
    # j = y.flatten()
    # from sklearn.tree import DecisionTreeClassifier
    # classifier = DecisionTreeClassifier()
    # classifier.fit(y,x)
    # h = []

    # for i in range(len(set(j))):
    #     l = list(classifier.predict([[i]]))
    #     h.append([i,l[0]])
    # h = np.matrix(h)

    # print("h",h)
    
    # print(corpus)
    
    # corpus = pd.DataFrame({'area':k['food'],'area_name':k['food']})
    # corpus = corpus.dropna()
    # print(corpus)
    # x = corpus.iloc[:,1].values
    # y = corpus.iloc[:,0:1].values
    # from sklearn.preprocessing import LabelEncoder
    # label = LabelEncoder()
    # y[:,0] = label.fit_transform(y[:,0])
    # j = y.flatten()
    # from sklearn.tree import DecisionTreeClassifier
    # classifier = DecisionTreeClassifier()
    # classifier.fit(y,x)
    # h1 = []
    
    # for i in range(len(set(j))):
    #     l = list(classifier.predict([[i]]))
    #     h1.append([i,l[0]])
    # h1 = np.matrix(h1)
    # print('h1',h1)

    # j = []
    # for i in range(len(k)):
    #     for j in range(len(h)):
    #         if([j][1] == area):
    #             if((area not in j[:,1])):
    #                 j.append([h[j][0],h[j][1],])
            
    # print(h)
    h = [['address','order','food']]
    print(h)
    for i in range(len(k['address'])):
        if(area == k['address'][i]):
            flag = 0
            for j in range(len(h)):
                if(k['food'][i] == h[j][2]):
                    flag = 1
                    break
            if(flag != 1):
                h.append([k['address'][i],k['order'][i],k['food'][i]])
                print("hello")
            elif(flag == 1):
                for j in range(len(h)):
                    if(h[j][2] == k['food'][i]):
                        h[j][1] = h[j][1] + k['order'][i]
                        print("hi")
    print(h)

    default = [0]
    labels = [""]
    color = []
    for i in range(1,len(h)):
        default.append(int(h[i][1]))
        labels.append(str(h[i][2]).title())
        color.append('rgba(54, 162, 235, .8)')
    color.append('rgba(54, 162, 235, .8)')
    data = {
        'color':color,
        'labels':labels,
        'default':default,
    }
    return JsonResponse(data)

