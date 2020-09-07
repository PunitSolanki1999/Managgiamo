from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.db.models import Q
import datetime
from django.core.mail import send_mail
from django.conf import settings
from random import randint

from .models import School_Management, School_Faculty_Data, School_Student_Data, School_Employee_Data, School_Marks_Data, School_Examination_Data, School_Total_Attendance

from .forms import SchoolLogin, SchoolRegister, Faculty_Data_Insert, Student_Data_Insert, Employee_Data_Insert, Student_Marks_Insertion, Student_Data_Update, Faculty_Data_Update, Employee_Data_Update, Update_Student_Fee, Student_Leave_Update, Faculty_Leave_Update, Employee_Leave_Update, School_Examiner_Insert, School_Total_Attendance_Detail, Examiner_Data_Update, Student_Marks, Employee_Leave_Update, Examination_Leave_Update, Change_School_Password, Update_School_Detail

from all.models import User_Data
# Create your views here.

# def logout(request,*args,**kwargs):
#     if request.session.has_key('school'):
#         del request.session['school']
#         return redirect('school:school-login')
#     elif request.session.has_key('faculty'):
#         del request.session['faculty']
#         return redirect('school:school-login')
#     elif request.session.has_key('examiner'):
#         del request.session['examiner']
#         return redirect('school:school-login')
#     else:
#         return redirect('school:school-login')

# def school_login(request,*args,**kwargs):
#     if request.session.has_key('school'):
#         return redirect('school:school-interface')
#     form = SchoolLogin(request.POST or None)
#     username_not_available = False
#     password_not_available = False
#     if request.method == 'POST':
#         data = request.POST.copy()
#         username = data.get('username')
#         password = data.get('password')
#         try:
#             user = School_Management.objects.get(username = username)
#             if user.username == username and user.password == password:
#                 if request.session.has_key('faculty'):
#                     del request.session['faculty']
#                 elif request.session.has_key('examiner'):
#                     del request.session['examiner']
#                 request.session['school'] = user.superkey
#                 return redirect('school:school-interface')
#             else:
#                 password_not_available = True
#         except Exception:
#             username_not_available = True
#     context = {
#         'form': form,
#         'username_not_available': username_not_available,
#         'password_not_available': password_not_available,
#     }
#     return render(request,'school/school_login.html',context)

def school_register(request,*args,**kwargs):
    if request.session.has_key('user'):
        form = SchoolRegister(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                instance = form.save(commit = False)
                user = User_Data.objects.get(mainkey = request.session['user'])
                instance.username = user.username
                instance.password = user.password
                user.management = user.management + 'school,'
                instance.user_id = instance.school_code
                instance.superkey = (instance.school_code + instance.username)
                instance.mainkey = user.mainkey
                instance.save()
                user.save()
                request.session['school'] = instance.superkey
                return redirect('school:school-interface')
        context = {
            'form': form,
        }
        return render(request,'school/school_register.html',context)
    else:
        return redirect('all:user-login')

def school_interface(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            key = request.session['school']
            student = School_Student_Data.objects.filter(Q(superkey__iexact=key) & Q(to_date__iexact=None)).count()
            employee = School_Employee_Data.objects.filter(Q(superkey__iexact=key) & Q(to_date__iexact=None)).count()
            examiner = School_Examination_Data.objects.filter(Q(superkey__iexact=key) & Q(to_date__iexact=None)).count()
            faculty = School_Faculty_Data.objects.filter(Q(superkey__iexact=key) & Q(to_date__iexact=None)).count()
            context = {
                'student': student + 1,
                'employee': employee , 
                'examiner': examiner ,
                'faculty' : faculty , 
            }
            return render(request,'school/school_interface.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def faculty_insertion(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            form = Faculty_Data_Insert(request.POST or None , request.FILES or None)
            faculty_id_not = False
            if request.method == 'POST':
                if form.is_valid():
                    instance = form.save(commit = False)
                    superk = request.session['school']
                    user = School_Management.objects.get(superkey=superk)
                    faculty_user = School_Faculty_Data.objects.filter(Q(superkey__iexact = superk))
                    i = 0
                    for i in faculty_user:
                        if instance.faculty_no != i.faculty_no:
                            i = 1
                        else:
                            faculty_id_not = True
                            i = 0
                            break
                    else:
                        i = 1
                    if(i == 1):
                        instance.faculty_id =  (user.school_code + ("FI") + str(instance.faculty_no))
                        instance.superkey = superk
                        if 'profile_pic' in request.FILES:
                            instance.picture = request.FILES['profile_pic']
                        instance.save()
                        return redirect("school:faculty-detail",instance.pk)
            form.fields['from_date'].initial = datetime.date.today()      
            context = {
                'form': form,
                'faculty_id_not': faculty_id_not,
            }
            return render(request,'school/school_faculty_insertion.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def student_insertion(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            form = Student_Data_Insert(request.POST or None , request.FILES or None)
            scholar_id_not = False
            scholar = School_Student_Data.objects.all().count()
            if request.method == 'POST':
                if form.is_valid():
                    instance = form.save(commit = False)
                    superk = request.session['school']
                    user = School_Management.objects.get(superkey=superk)
                    scholar_user = School_Student_Data.objects.filter(Q(superkey__iexact = superk))
                    i = 0
                    for i in scholar_user:
                        if instance.scholar_no != i.scholar_no:
                            i = 1
                        else:
                            scholar_id_not = True
                            i = 0
                            print('hello')
                            break
                    else:
                        i = 1
                    if(i == 1):
                        instance.student_id = (user.school_code + "ST" + str(instance.scholar_no))
                        instance.superkey = superk
                        if 'profile_pic' in request.FILES:
                            instance.picture = request.FILES['profile_pic']
                        instance.save()
                        return redirect('school:student-insertion')
                        # return redirect('school:student-detail',instance.pk)
            form.fields['scholar_no'].initial = scholar + 1
            form.fields['from_date'].initial = datetime.date.today()
            context = {
                'form': form,
                'scholar_id_not' : scholar_id_not,
            }
            return render(request,'school/school_student_insertion.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def employee_insertion(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            form = Employee_Data_Insert(request.POST or None , request.FILES or None)
            employee_id_not = False
            if request.method == 'POST':
                if form.is_valid():
                    instance = form.save(commit = False)
                    superk = request.session['school']
                    user = School_Management.objects.get(superkey=superk)
                    employee_user = School_Employee_Data.objects.filter(Q(superkey__iexact = superk))
                    i = 0
                    for i in employee_user:
                        if instance.employee_no != i.employee_no:
                            i = 1
                            print("Bye")
                        else:
                            employee_id_not = True
                            i = 0
                            print("Hello")
                            break
                    else:
                        i = 1
                    if(i == 1):
                        instance.employee_id = (user.school_code + "EI" + str(instance.employee_no))
                        instance.superkey = superk
                        if 'profile_pic' in request.FILES:
                            instance.picture = request.FILES['profile_pic']
                        instance.save()
                        return redirect('school:employee-detail',instance.pk)
            form.fields['from_date'].initial = datetime.date.today()
            context = {
                'form': form,
                'employee_id_not': employee_id_not,
            }
            return render(request,'school/school_employee_insertion.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

# def faculty_login(request,*args,**kwargs):
#     form = SchoolLogin(request.POST or None)
#     username_not_available = False
#     password_not_available = False
#     if request.method == 'POST':
#         data = request.POST.copy()
#         username = data.get('username')
#         password = data.get('password')
#         try:
#             user = School_Faculty_Data.objects.get(username = username)
#             if user.username == username and user.password == password:
#                 if request.session.has_key('school'):
#                     del request.session['school']
#                 elif request.session.has_key('examiner'):
#                     del request.session['examiner']
#                 request.session['faculty'] = user.faculty_id
#                 return redirect('school:faculty-student-detail-form')
#             else:
#                 password_not_available = True
#         except Exception:
#             username_not_available = True
#     context = {
#         'form': form,
#         'username_not_available': username_not_available,
#         'password_not_available': password_not_available,
#     }
#     return render(request,'school/school_faculty_login.html',context)

def student_marks(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            form = Student_Marks_Insertion(request.POST or None)
            student_id_not = False
            if request.method == 'POST':
                if form.is_valid():
                    instance = form.save(commit = False)
                    key = request.session['school']
                    user = School_Management.objects.get(superkey = key)
                    try:    
                        student = School_Student_Data.objects.get(student_id = instance.student_id)
                        if(student.superkey != user.superkey):
                            raise Exception             
                        instance.superkey = user.superkey
                        instance.save()
                        return redirect('school:student-marks')
                    except:
                        student_id_not = True
            context = {
                'form': form,
                'student_id_not': student_id_not,
            }
            return render(request,'school/student_marks_insertion.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def student_detail_form(request,*args,**kwargs): 
    if request.session.has_key('user'):    
        if request.session.has_key('school'):
            confirm = False
            context = {
                'confirm': confirm,
            }
            if request.method == 'POST':
                data = request.POST.copy()
                search = data.get('search')
                superk = request.session['school']
                student = School_Student_Data.objects.filter(Q(superkey__iexact = superk)&Q(student_id__icontains = search))
                confirm = True
                context = {
                    'student': student,
                    'confirm': confirm,
                }
            return render(request,'school/student_detail_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def student_detail(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            if(pk != None):
                student = School_Student_Data.objects.get(student_id = pk)
                context = {
                    'student': student,
                }
                return render(request,'school/student_detail.html',context)
            else:
                return redirect('school:student-detail-form')
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def faculty_detail_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            confirm = False
            context = {
                'confirm': confirm,
            }
            if request.method == 'POST':
                data = request.POST.copy()
                search = data.get('search')
                superk = request.session['school']
                faculty = School_Faculty_Data.objects.filter(Q(superkey__iexact = superk)&Q(faculty_id__icontains = search))
                confirm = True
                context = {
                    'faculty': faculty,
                    'confirm': confirm,
                }
            return render(request,'school/faculty_detail_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def faculty_detail(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            context = {}
            if(pk != None):
                faculty = School_Faculty_Data.objects.get(faculty_id = pk)
                context = {
                    'faculty': faculty,
                }
            else:
                return redirect('school:faculty-detail-form')
            return render(request,'school/faculty_detail.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def employee_detail_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            confirm = False
            context = {
                'confirm': confirm,
            }
            if request.method == 'POST':
                data = request.POST.copy()
                search = data.get('search')
                superk = request.session['school']
                employee = School_Employee_Data.objects.filter(Q(superkey__iexact = superk) & Q(employee_id__icontains = search))
                confirm = True
                context = {
                    'employee': employee,
                    'confirm': confirm,
                }
            return render(request,'school/employee_detail_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def employee_detail(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            context = {}
            if(pk != None):
                employee = School_Employee_Data.objects.get(employee_id = pk)
                context = {
                    'employee': employee,
                }
            else:
                return redirect('school:employee-detail-form')
            return render(request,'school/employee_detail.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def income(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            key = request.session['school']
            student = School_Student_Data.objects.filter(Q(superkey__iexact = key))
            nursery     = 0
            lkg         = 0
            pre_first   = 0
            first       = 0
            second      = 0
            third       = 0
            fourth      = 0
            fifth       = 0
            sixth       = 0
            seventh     = 0
            eigth       = 0
            ninth       = 0
            tenth       = 0
            eleventh    = 0
            twelveth    = 0
            for i in student:
                if(i.to_date == None):     #extra added line
                    if(i.clas == 'nursery'):
                        nursery = nursery + i.fee_submitted
                    elif(i.clas == 'lkg'):
                        lkg = lkg + i.fee_submitted
                    elif(i.clas == 'pre first'):
                        pre_first = pre_first + i.fee_submitted
                    elif(i.clas == 'first'):
                        first = first + i.fee_submitted
                    elif(i.clas == 'second'):
                        second = second + i.fee_submitted
                    elif(i.clas == 'third'):
                        third = third + i.fee_submitted
                    elif(i.clas == 'fourth'):
                        fourth = fourth + i.fee_submitted
                    elif(i.clas == 'fifth'):
                        fifth =  fifth + i.fee_submitted
                    elif(i.clas == 'sixth'):
                        sixth = sixth + i.fee_submitted
                    elif(i.clas == 'seventh'):
                        seventh =  seventh + i.fee_submitted
                    elif(i.clas == 'eigth'):
                        eigth = eigth + i.fee_submitted
                    elif(i.clas == 'ninth'):
                        ninth = ninth + i.fee_submitted
                    elif(i.clas == 'tenth'):
                        tenth = tenth + i.fee_submitted
                    elif(i.clas == 'eleventh'):
                        eleventh = eleventh + i.fee_submitted
                    elif(i.clas == 'twelveth'):
                        twelveth = twelveth + i.fee_submitted
            total = nursery + lkg + pre_first + first + second + third + fourth + fifth + sixth + seventh + eigth + ninth + tenth + eleventh + twelveth
            context = {
                'total': total,
                'nursery': nursery,
                'lkg': lkg,
                'pre_first': pre_first,
                'first': first,
                'second': second,
                'third': third,
                'fourth': fourth,
                'fifth': fifth,
                'sixth': sixth,
                'seventh': seventh,
                'eigth': eigth,
                'ninth': ninth,
                'tenth': tenth,
                'eleventh': eleventh,
                'twelveth': twelveth,
            }
            return render(request,'school/income.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def income_class(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            if(kwargs):
                key = request.session['school']
                if(kwargs['clas'] == 'pre_first'):
                    kwargs['clas'] = kwargs['clas'].replace('_',' ')
                student = School_Student_Data.objects.filter(Q(superkey__iexact = key) & Q(clas__icontains = kwargs['clas']))
                context = {
                    'income': kwargs['income'],
                    'student': student,
                }
            else:
                return redirect('school:income')
            return render(request,'school/income_class.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_student_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            confirm = False
            context = {
                'confirm': confirm,
            }
            if request.method == 'POST':
                data = request.POST.copy()
                search = data.get('search')
                key = request.session['school']
                student = School_Student_Data.objects.filter(Q(superkey__iexact = key)&Q(student_id__icontains = search))
                confirm = True
                context = {
                    'student': student,
                    'confirm': confirm,
                }
            return render(request,'school/update_student_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_student(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            if(pk != None):
                student = School_Student_Data.objects.get(student_id = pk)
                form = Student_Data_Update(request.POST or None , request.FILES or None)
                form.fields['fname'].initial        = student.fname       
                form.fields['mname'].initial        = student.mname       
                form.fields['lname'].initial        = student.lname       
                form.fields['father_name'].initial  = student.father_name 
                form.fields['father_phone'].initial = student.father_phone
                form.fields['mother_name'].initial  = student.mother_name 
                form.fields['mother_phone'].initial = student.mother_phone
                form.fields['state'].initial        = student.state       
                form.fields['city'].initial         = student.city        
                form.fields['pincode'].initial      = student.pincode     
                form.fields['address'].initial      = student.address       
                form.fields['dob'].initial          = student.dob                        
                form.fields['clas'].initial         = student.clas    
                form.fields['picture'].initial      = student.picture
                if request.method == 'POST':
                    if form.is_valid():
                        instance = form.save(commit = False)
                        student.fname        = instance.fname       
                        student.mname        = instance.mname       
                        student.lname        = instance.lname       
                        student.father_name  = instance.father_name 
                        student.father_phone = instance.father_phone
                        student.mother_name  = instance.mother_name 
                        student.mother_phone = instance.mother_phone
                        student.state        = instance.state       
                        student.city         = instance.city        
                        student.pincode      = instance.pincode     
                        student.address      = instance.address     
                        student.dob          = instance.dob                  
                        student.clas         = instance.clas  
                        if 'profile_pic' in request.FILES:
                            instance.picture = request.FILES['profile_pic']
                        student.picture      = instance.picture
                        student.save()    
                        return redirect('school:student-detail',student.pk)  
                context = {
                    'form': form,
                    'student': student,
                }    
            else:
                return redirect('school:update-student-form')
            return render(request,'school/update_student.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_faculty_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            confirm = False
            context = {
                'confirm': confirm,
            }
            if request.method == 'POST':
                data = request.POST.copy()
                search = data.get('search')
                key = request.session['school']
                faculty = School_Faculty_Data.objects.filter(Q(superkey__iexact = key) & Q(faculty_id__icontains = search))
                confirm = True
                context = {
                    'faculty': faculty,
                    'confirm': confirm,
                }
            return render(request,'school/update_faculty_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_faculty(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            if(pk != None):
                faculty = School_Faculty_Data.objects.get(faculty_id = pk)
                form = Faculty_Data_Update(request.POST or None , request.FILES or None)
                form.fields['fname'].initial        = faculty.fname              
                form.fields['mname'].initial        = faculty.mname              
                form.fields['lname'].initial        = faculty.lname              
                form.fields['emailid'].initial      = faculty.emailid      
                form.fields['phone'].initial        = faculty.phone       
                form.fields['father_name'].initial  = faculty.father_name 
                form.fields['father_phone'].initial = faculty.father_phone
                form.fields['mother_name'].initial  = faculty.mother_name        
                form.fields['mother_phone'].initial = faculty.mother_phone       
                form.fields['state'].initial        = faculty.state         
                form.fields['city'].initial         = faculty.city            
                form.fields['pincode'].initial      = faculty.pincode                           
                form.fields['address'].initial      = faculty.address     
                form.fields['subject'].initial      = faculty.subject     
                form.fields['dob'].initial          = faculty.dob         
                form.fields['salary'].initial       = faculty.salary      
                form.fields['clas'].initial         = faculty.clas        
                form.fields['picture'].initial      = faculty.picture
                if request.method == 'POST':
                    if form.is_valid():
                        instance = form.save(commit = False)
                        faculty.fname        = instance.fname       
                        faculty.mname        = instance.mname       
                        faculty.lname        = instance.lname       
                        faculty.emailid      = instance.emailid     
                        faculty.phone        = instance.phone       
                        faculty.father_name  = instance.father_name 
                        faculty.father_phone = instance.father_phone
                        faculty.mother_name  = instance.mother_name 
                        faculty.mother_phone = instance.mother_phone
                        faculty.state        = instance.state       
                        faculty.city         = instance.city        
                        faculty.pincode      = instance.pincode     
                        faculty.address      = instance.address     
                        faculty.subject      = instance.subject     
                        faculty.dob          = instance.dob         
                        faculty.salary       = instance.salary      
                        faculty.clas         = instance.clas    
                        if 'profile_pic' in request.FILES:
                            instance.picture = request.FILES['profile_pic']
                        faculty.picture      = instance.picture      
                        faculty.save()
                        return redirect('school:faculty-detail',faculty.pk)       
                context = {
                    'form': form,
                    'faculty': faculty,
                }    
            else:
                return redirect('school:update-faculty-form')
            return render(request,'school/update_faculty.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_employee_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            confirm = False
            context = {
                'confirm': confirm,
            }
            if request.method == 'POST':
                data = request.POST.copy()
                search = data.get('search')
                key = request.session['school']
                employee = School_Employee_Data.objects.filter(Q(superkey__iexact = key) & Q(employee_id__icontains = search))
                confirm = True
                context = {
                    'employee': employee,
                    'confirm': confirm,
                }
            return render(request,'school/update_employee_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_employee(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            if(pk != None):
                employee = School_Employee_Data.objects.get(employee_id = pk)
                form = Employee_Data_Update(request.POST or None , request.FILES or None)
                form.fields['fname'].initial        = employee.fname              
                form.fields['mname'].initial        = employee.mname              
                form.fields['lname'].initial        = employee.lname              
                form.fields['phone'].initial        = employee.phone        
                form.fields['father_name'].initial  = employee.father_name 
                form.fields['father_phone'].initial = employee.father_phone
                form.fields['mother_name'].initial  = employee.mother_name 
                form.fields['mother_phone'].initial = employee.mother_phone       
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
                        employee.mother_name  = instance.mother_name 
                        employee.mother_phone = instance.mother_phone
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
                        return redirect('school:employee-detail',employee.pk) 
                context = {
                    'form': form,
                    'employee': employee,
                }    
            else:
                return redirect('school:update-employee-form')
            return render(request,'school/update_employee.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')


def update_student_fee_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            confirm = False
            context = {
                'confirm': confirm,
            }
            if request.method == 'POST':
                data = request.POST.copy()
                search = data.get('search')
                key = request.session['school']
                student = School_Student_Data.objects.filter(Q(superkey__iexact = key) & Q(student_id__icontains = search))
                confirm = True
                context = {
                    'student': student,
                    'confirm': confirm,
                }
            return render(request,'school/update_student_fee_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_student_fee(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            if(pk != None):
                student = School_Student_Data.objects.get(student_id = pk)
                form = Update_Student_Fee(request.POST or None)
                form.fields['fee'].initial = student.fee      
                form.fields['fee_submitted'].initial = student.fee_submitted         
                if request.method == 'POST':
                    if form.is_valid():
                        instance = form.save(commit = False)
                        student.fee             = instance.fee   
                        student.fee_submitted   = instance.fee_submitted        
                        student.save()  
                        return redirect('school:update-student-fee-form')     
                context = {
                    'form': form,
                    'student': student,
                }    
            else:
                return redirect('school:update-student-fee-form')
            return render(request,'school/update_student_fee.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_student_leave_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            confirm = False
            context = {
                'confirm': confirm,
            }
            if request.method == 'POST':
                data = request.POST.copy()
                search = data.get('search')
                key = request.session['school']
                student = School_Student_Data.objects.filter(Q(superkey__iexact = key) & Q(student_id__icontains = search))
                confirm = True
                context = {
                    'student': student,
                    'confirm': confirm,
                }
            return render(request,'school/update_student_leave_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')
        

def update_student_leave(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            if(pk != None):
                student = School_Student_Data.objects.get(student_id = pk)
                form = Student_Leave_Update(request.POST or None) 
                form.fields['to_date'].initial = datetime.date.today()      
                if request.method == 'POST':
                    if form.is_valid():
                        instance = form.save(commit = False)
                        student.to_date = instance.to_date       
                        student.save()      
                        return redirect('school:update-student-leave-form') 
                context = {
                    'form': form,
                    'student': student,
                }    
            else:
                return redirect('school:update-student-leave-form')
            return render(request,'school/update_student_leave.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_faculty_leave_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            confirm = False
            context = {
                'confirm': confirm,
            }
            if request.method == 'POST':
                data = request.POST.copy()
                search = data.get('search')
                key = request.session['school']
                faculty = School_Faculty_Data.objects.filter(Q(superkey__iexact = key) & Q(faculty_id__icontains = search))
                confirm = True
                context = {
                    'faculty': faculty,
                    'confirm': confirm,
                }
            return render(request,'school/update_faculty_leave_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_faculty_leave(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            if(pk != None):
                faculty = School_Faculty_Data.objects.get(faculty_id = pk)
                form = Faculty_Leave_Update(request.POST or None)       
                form.fields['to_date'].initial  = datetime.date.today()
                if request.method == 'POST':
                    if form.is_valid():
                        instance = form.save(commit = False)
                        faculty.to_date = instance.to_date 
                        faculty.save()   
                        return redirect('school:update-faculty-leave-form')    
                context = {
                    'form': form,
                    'faculty': faculty,
                }    
            else:
                return redirect('school:update-faculty-leave-form')
            return render(request,'school/update_faculty_leave.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_employee_leave_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            confirm = False
            context = {
                'confirm': confirm,
            }
            if request.method == 'POST':
                data = request.POST.copy()
                search = data.get('search')
                key = request.session['school']
                employee = School_Employee_Data.objects.filter(Q(superkey__iexact = key) & Q(employee_id__icontains = search))
                confirm = True
                context = {
                    'employee': employee,
                    'confirm': confirm,
                }
            return render(request,'school/update_employee_leave_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_employee_leave(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            if(pk != None):
                employee = School_Employee_Data.objects.get(employee_id = pk)
                form = Employee_Leave_Update(request.POST or None)
                form.fields['to_date'].initial = datetime.date.today()                 
                if request.method == 'POST':
                    if form.is_valid():
                        instance = form.save(commit = False)
                        employee.to_date    = instance.to_date       
                        employee.save()  
                        return redirect('school:update-employee-leave-form')     
                context = {
                    'form': form,
                    'employee': employee,
                }    
            else:
                return redirect('school:update-employee-leave-form')
            return render(request,'school/update_employee_leave.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def school_account_detail(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            key = request.session['school']
            user = School_Management.objects.get(superkey = key)
            context = {
                'user': user,
            }
            return render(request,'school/school_account_detail.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')


def school_examiner_insert(request):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            form = School_Examiner_Insert(request.POST or None, request.FILES or None)
            examiner_id_not = False
            if request.method == 'POST':
                if form.is_valid():
                    instance = form.save(commit = False)
                    superk = request.session['school']
                    user = School_Management.objects.get(superkey=superk)
                    examiner_user = School_Examination_Data.objects.filter(Q(superkey__iexact = superk))
                    i = 0
                    for i in examiner_user:
                        if instance.examiner_no != i.examiner_no:
                            i = 1
                        else:
                            examiner_id_not = True
                            i = 0
                            break
                    else:
                        i = 1

                    if(i == 1):
                        instance.examiner_id =  (user.school_code + ("ED") + str(instance.examiner_no))
                        instance.superkey = superk
                        if 'profile_pic' in request.FILES:
                            instance.picture = request.FILES['profile_pic']
                        instance.save()
                        return redirect("school:school-examiner-insert")
            form.fields['from_date'].initial = datetime.date.today()      
            context = {
                'form': form,
                'examiner_id_not': examiner_id_not,
            }
            return render(request,'school/school_examiner_register.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def student_attendance(request):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            form = School_Total_Attendance_Detail(request.POST or None)
            student_id_not = False
            if request.method == 'POST':
                if form.is_valid():
                    instance = form.save(commit = False)
                    key = request.session['school']
                    user = School_Management.objects.get(superkey = key)
                    try:    
                        student = School_Student_Data.objects.get(student_id = instance.student_id)
                        if(student.superkey != user.superkey):
                            student_id_not = True
                            raise Exception             
                        instance.superkey = user.superkey
                        instance.save()
                        return redirect('school:student-attendance') 
                    except:
                        student_id_not = True
            context = {
                'form': form,
                'student_id_not': student_id_not,
            }
            return render(request,'school/student_attendance.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_examiner_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            confirm = False
            context = {
                'confirm': confirm,
            }
            if request.method == 'POST':
                data = request.POST.copy()
                search = data.get('search')
                key = request.session['school']
                examiner = School_Examination_Data.objects.filter(Q(superkey__iexact = key) & Q(examiner_id__icontains = search))
                confirm = True
                context = {
                    'examiner': examiner,
                    'confirm': confirm,
                }
            return render(request,'school/update_examiner_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_examiner(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            if(pk != None):
                examiner = School_Examination_Data.objects.get(examiner_id = pk)
                form = Examiner_Data_Update(request.POST or None , request.FILES or None)
                form.fields['fname'].initial        = examiner.fname              
                form.fields['mname'].initial        = examiner.mname              
                form.fields['lname'].initial        = examiner.lname              
                form.fields['emailid'].initial      = examiner.emailid      
                form.fields['phone'].initial        = examiner.phone       
                form.fields['father_name'].initial  = examiner.father_name 
                form.fields['father_phone'].initial = examiner.father_phone
                form.fields['mother_name'].initial  = examiner.mother_name        
                form.fields['mother_phone'].initial = examiner.mother_phone       
                form.fields['state'].initial        = examiner.state         
                form.fields['city'].initial         = examiner.city            
                form.fields['pincode'].initial      = examiner.pincode                           
                form.fields['address'].initial      = examiner.address     
                form.fields['dob'].initial          = examiner.dob         
                form.fields['salary'].initial       = examiner.salary      
                form.fields['picture'].initial      = examiner.picture
                if request.method == 'POST':
                    if form.is_valid():
                        instance = form.save(commit = False)
                        examiner.fname        = instance.fname       
                        examiner.mname        = instance.mname       
                        examiner.lname        = instance.lname       
                        examiner.emailid      = instance.emailid     
                        examiner.phone        = instance.phone       
                        examiner.father_name  = instance.father_name 
                        examiner.father_phone = instance.father_phone
                        examiner.mother_name  = instance.mother_name 
                        examiner.mother_phone = instance.mother_phone
                        examiner.state        = instance.state       
                        examiner.city         = instance.city        
                        examiner.pincode      = instance.pincode     
                        examiner.address      = instance.address     
                        examiner.dob          = instance.dob         
                        examiner.salary       = instance.salary     
                        if 'profile_pic' in request.FILES:
                            instance.picture = request.FILES['profile_pic']
                        examiner.picture      = instance.picture 
                        examiner.save()    
                        return redirect('school:examiner-detail',examiner.pk)   
                context = {
                    'form': form,
                    'examiner': examiner,
                }    
            else:
                return redirect('school:update-examiner-form')
            return render(request,'school/update_examiner.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')


# def examiner_login(request,*args,**kwargs):
#     form = SchoolLogin(request.POST or None)
#     username_not_available = False
#     password_not_available = False
#     if request.method == 'POST':
#         data = request.POST.copy()
#         username = data.get('username')
#         password = data.get('password')
#         try:
#             user = School_Examination_Data.objects.get(username = username)
#             if user.username == username and user.password == password:
#                 if request.session.has_key('school'):
#                     del request.session['school']
#                 elif request.session.has_key('faculty'):
#                     del request.session['faculty']
#                 request.session['examiner'] = user.examiner_id
#                 return redirect('school:student-marks')
#             else:
#                 password_not_available = True
#         except Exception:
#             username_not_available = True
#     context = {
#         'form': form,
#         'username_not_available': username_not_available,
#         'password_not_available': password_not_available,
#     }
#     return render(request,'school/examiner_login.html',context)

def student_marks_detail(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            form = Student_Marks(request.POST or None)
            confirm = False
            student_detail = None
            if request.method == "POST":
                data = request.POST.copy()
                student = data.get('student_id')
                clas = data.get('clas')
                key = School_Management.objects.get(superkey = request.session['school'])
                key = key.superkey
                confirm = True
                student_detail = School_Marks_Data.objects.filter(Q(superkey__iexact = key) & Q(student_id__iexact = student) & Q(clas__iexact = clas))
            context = {
                'form': form,
                'confirm': confirm,
                'student': student_detail,
            }
            return render(request,"school/student_marks_detail.html",context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def student_marks_update_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            confirm = False
            student = None
            form = Student_Marks(request.POST or None)
            if request.method == "POST":
                data = request.POST.copy()
                student_id = data.get('student_id')
                clas = data.get('clas')
                key = request.session['school']
                key = School_Management.objects.get(superkey = key)
                student = School_Marks_Data.objects.filter(Q(superkey__iexact = key.superkey) & Q(student_id__icontains = student_id) & Q(clas__iexact = clas))
                confirm = True
            context = {
                'form': form,
                'confirm': confirm,
                'student': student,
            }
            return render(request,'school/student_marks_update_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def student_marks_update(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            if pk != None:
                form = Student_Marks_Insertion(request.POST or None)
                student = School_Marks_Data.objects.get(pk = pk)
                form.fields['student_id'].initial =  student.student_id
                form.fields['clas'].initial = student.clas
                form.fields['marks'].initial = student.marks
                form.fields['subject'].initial = student.subject
                if request.method == "POST":
                    if form.is_valid():
                        instance = form.save(commit = False)
                        student.student_id  = instance.student_id
                        student.clas        = instance.clas
                        student.marks       = instance.marks
                        student.subject     = instance.subject
                        student.save()
                        return redirect('school:student-marks-update-form')
                context = {
                    'form': form,
                }
                return render(request,'school/student_marks_update.html',context)
            else:
                return redirect('school:student-marks-update-form')
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def examiner_detail_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            confirm = False
            context = {
                'confirm': confirm,
            }
            if request.method == 'POST':
                data = request.POST.copy()
                search = data.get('search')
                superk = request.session['school']
                examiner = School_Examination_Data.objects.filter(Q(superkey__iexact = superk) & Q(examiner_id__icontains = search))
                confirm = True
                context = {
                    'examiner': examiner,
                    'confirm': confirm,
                }
            return render(request,'school/examiner_detail_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def examiner_detail(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            context = {}
            if(pk != None):
                examiner = School_Examination_Data.objects.get(examiner_id = pk)
                context = {
                    'examiner': examiner,
                }
            else:
                return redirect('school:examiner-detail-form')
            return render(request,'school/examiner_detail.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_examiner_leave_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            confirm = False
            context = {
                'confirm': confirm,
            }
            if request.method == 'POST':
                data = request.POST.copy()
                search = data.get('search')
                key = request.session['school']
                examiner = School_Examination_Data.objects.filter(Q(superkey__iexact = key) & Q(examiner_id__icontains = search))
                confirm = True
                context = {
                    'examiner': examiner,
                    'confirm': confirm,
                }
            return render(request,'school/update_examiner_leave_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_examiner_leave(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            if(pk != None):
                examiner = School_Examination_Data.objects.get(examiner_id = pk)
                form = Examination_Leave_Update(request.POST or None)       
                form.fields['to_date'].initial = datetime.date.today()
                if request.method == 'POST':
                    if form.is_valid():
                        instance = form.save(commit = False)
                        examiner.to_date = instance.to_date 
                        examiner.save()
                        return redirect('school:update-examiner-leave-form')       
                context = {
                    'form': form,
                    'examiner': examiner,
                }    
            else:
                return redirect('school:update-examiner-leave-form')
            return render(request,'school/update_examiner_leave.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_attendance_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            confirm = False
            student = None
            form = Student_Marks(request.POST or None)
            if request.method == "POST":
                data = request.POST.copy()
                student_id = data.get('student_id')
                clas = data.get('clas')
                key = request.session['school']
                key = School_Management.objects.get(superkey = key)
                student = School_Total_Attendance.objects.filter(Q(superkey__iexact = key.superkey) & Q(student_id__icontains = student_id) & Q(clas__iexact = clas))
                confirm = True
            context = {
                'form': form,
                'confirm': confirm,
                'student': student,
            }
            return render(request,'school/update_attendance_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_attendance(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            if pk != None:
                form = School_Total_Attendance_Detail(request.POST or None)
                student = School_Total_Attendance.objects.get(pk = pk)
                form.fields['student_id'].initial =  student.student_id
                form.fields['clas'].initial = student.clas
                form.fields['student_attend'].initial = student.student_attend
                form.fields['total_working'].initial = student.total_working
                if request.method == "POST":
                    if form.is_valid():
                        instance = form.save(commit = False)
                        student.student_id      = instance.student_id
                        student.clas            = instance.clas
                        student.student_attend  = instance.student_attend
                        student.total_working   = instance.total_working
                        student.save()
                        return redirect('school:update-attendance-form')
                context = {
                    'form': form,
                }
                return render(request,'school/update_attendance.html',context)
            else:
                return redirect('school:update-attendace-form')
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def student_attendance_report(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            form = Student_Marks(request.POST or None)
            confirm = False
            student_detail = None
            if request.method == "POST":
                data = request.POST.copy()
                student = data.get('student_id')
                clas = data.get('clas')
                key = School_Management.objects.get(superkey = request.session['school'])
                key = key.superkey
                confirm = True
                student_detail = School_Total_Attendance.objects.filter(Q(superkey__iexact = key) & Q(student_id__iexact = student) & Q(clas__iexact = clas))
            context = {
                'form': form,
                'confirm': confirm,
                'student': student_detail,
            }
            return render(request,"school/student_attendance_report.html",context)
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
#             user = School_Management.objects.get(username=username)
#             return redirect('school:otp-verification',username)
#         except:
#             username_not = True
#     return render(request,'school/username.html',{'username_not':username_not})

# def otp_verification(request,username=None,*args,**kwargs):
#     if request.session.has_key('school'):
#         key = request.session['school']
#         school = School_Management.objects.get(superkey=key)
#     elif username != None:
#         school = School_Management.objects.get(username=username)
#     else:
#         return redirect('school:username')
#     otp = randint(100000,999999)
#     subject = "[MANAGGIAMO] Account Verification Code."
#     message = ("Hey " + str(school.username) + "\nThe changing password attempt require futher verfication because we did not recognize your decive. To Complete the verification enter code on the unrecognized device.\nVerification Code: " + str(otp))
#     email_from = settings.EMAIL_HOST_USER
#     email = school.emailid
#     recipient_list = [email,]
#     send_mail( subject, message, email_from, recipient_list )
#     return redirect('school:otp',otp,school)

# def otp_confirm(request,otp=None,school=None,*args,**kwargs):
#     if(otp == None or school == None):
#         return redirect("school:otp-verification",school)
#     confirm = False
#     otp_not = False
#     school = School_Management.objects.get(username=school)
#     if request.method == "POST":
#         confirm = True
#         data = request.POST.copy()
#         otp_verification = data.get('otp')
#         if int(otp) == int(otp_verification):
#             request.session['school_otp'] = school.username
#             return redirect('school:change-password')
#         else:
#             otp_not = True
#     context = {
#         'school': school,
#         'confirm': confirm,
#         'otp': otp_not,
#     }
#     return render(request,'school/opt_verification.html',context)

# def change_password(request,*args,**kwargs):
#     if request.session.has_key('school_otp'):
#         form = Change_School_Password(request.POST or None)
#         if request.method == "POST":
#             username = request.session['school_otp']
#             school = School_Management.objects.get(username=username)
#             if form.is_valid():
#                 instance = form.save(commit=False)
#                 school.password = instance.password
#                 school.save()
#                 del request.session['school_otp']
#                 return redirect('school:school-login')
#         context = {
#             'form': form,
#         }
#         return render(request,'school/change_password.html',context)
#     else:
#         if request.session.has_key('school'):
#             key = request.session['school']
#             school = School_Management.objects.get(superkey=key)
#             return redirect('school:otp-verification',school.username)
#         else:
#             return redirect('school:username')

def update_school_detail(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            key = request.session['school']
            form = Update_School_Detail(request.POST or None)
            school = School_Management.objects.get(superkey=key)
            form.fields['emailid'].initial = school.emailid
            form.fields['phone'].initial = school.phone
            form.fields['organisation'].initial = school.organisation
            form.fields['state'].initial = school.state
            form.fields['city'].initial = school.city
            form.fields['pincode'].initial = school.pincode
            form.fields['address'].initial = school.address
            if request.method == "POST":
                if form.is_valid():
                    instance = form.save(commit=False)
                    school.emailid = instance.emailid
                    school.phone = instance.phone
                    school.address = instance.address
                    school.save()
                    return redirect('school:school-account-detail')
            context = {
                'form': form,
            }
            return render(request,'school/update_school_detail.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def faculty_student_detail_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            confirm = False
            context = {
                'confirm': confirm,
            }
            if request.method == 'POST':
                data = request.POST.copy()
                search = data.get('search')
                faculty = request.session['school']
                user = School_Management.objects.get(superkey=faculty)
                superk = user.superkey
                student = School_Student_Data.objects.filter(Q(superkey__iexact = superk)&Q(student_id__icontains = search))
                confirm = True
                context = {
                    'student': student,
                    'confirm': confirm,
                }
            return render(request,'school/faculty_student_detail_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def faculty_student_detail(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            if(pk != None):
                student = School_Student_Data.objects.get(student_id = pk)
                context = {
                    'student': student,
                }
                return render(request,'school/faculty_student_detail.html',context)
            else:
                return redirect('school:student-detail-form')
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')   


import pandas as pd 
import numpy as np
from nltk.stem.porter import PorterStemmer

def predict(request,*args,**kwargs):
    corpus = []
    k = School_Student_Data.objects.all()
    l = ['Khandwa','Rajendra Nagar','Pithampur','Saket Nagar','Kalyani Nagar','Limbodi','A.B. Road','Annapurna Road','Khajuri Bazar','Race Course Road','Chhawani','Khatiwala Tank','Rajwada','Dhar Road','Maharani Road','RNT Marg','Sector 23-D','Depalpur','Datoda','Dakachia','Chordia','Choral','Chittoda','Burankhedi','Binawda','Bhatkhedi','Bai','Badodia Khan','Bachhoda','Aurangpura','Atwada','Attahada','Ambachandan','Alwasa','Ajnod','Barlai Jagir','Baoliakhurd','Badgonda','Bhagora','Bhanwrasala','Bhilbadoli','Banadia','Army Headquarters','Baloda Tkun','Chadoda','Indore Agrawal Nagar','Indore Badwali Chowk','Indore Bajasan Road','Bicholi Mardana','Biyabani','CGO Complex','Cloth Market','Dhannad','Dharnaka','Dudhia','Farkodha','Fatahabad Chandrawatiganj','FC Ganj Edso','Gandhi Nagar-Indore','Gautampura','Gawali Palasia','Girota','Gokulpur','Gujarkheda','Guran','Gurunanak Chowk','Harsola','Hasalpur','Army','Collectorate','Courts','Jail Road','Javeri Bagh','Cantt','Khajrana','Kumar Khadi','Lokmanya Nagar','Malharganj','Malwa Mill','Manorama Ganj','Mills','Nanda Nagar','Palasiya','Pardesipura','RSS Nagar','Indore Rajendra Nagar','Rajmohalla','Rambagh','Siyaganj','Topkhana','Srinagar Colony','Tukoganj','VS Market','Uchchanyayalay','Yeshwant Road','Jalodiyagyan','Jambudi Hapsi','Simrol','Palakhedi','Palda','Paliya','Panod','Pedmi','Pigdamber','Pipalda','Piwdai','Radio Colony Indore','Rajendra Nagar-Indore','Rangwasa','Jinda Kheda','Rolai','Sadar Bazar','Juni Indore','Kadwali Buzurg','Sagdod','Sanawadia','Kanadia','Kanadia Road','Sanwer Link Road','Sanwer','Khatiwala Tank-Indore','Khurdi','Sivani','Kodria','Krishnaganj','Solsinda','Kudana','Sudama Nagar','Lasudia','Tilak Nagar','Tillor Khurd','Tillorbujurg','Limbiodapar','Todi','Lokmanya Nagar','Machal','Vallabh Nagar','Machla','Vijay Nagar','Maithwada','Yashwant Nagar','Manglia','Manpur','Jamli','Nanda Nagar-Indore','Pagnispaga Indore','Jhalaria','Biyabani-Indore','Kankaripal','DDU Nagar','Kanwasa','Indore Nagar','Kelod Kartal','Ravi Shankar Shukla Nagar','Kalaria','Khajrana','Kallibillod','Murkheda','Kalmer','Sawer','Sumtha','Kampel','Bhavarkua','piplihana chouraha','bengali chouraha','navlakha chouraha','grand exotica','tilik nagar','geeta bhawan','LIG','rajiv gandhi','navlakha','M.Y.','palasia']
    y = []
    for i in range(len(l)):
        l[i] = l[i].lower()
    for i in range(len(k)):
        p = str(k[i].address)
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
    corpus = pd.DataFrame({'area':u,'area_name':u})
    corpus = corpus.dropna()
    x = corpus.iloc[:,1].values
    y = corpus.iloc[:,0:1].values
    from sklearn.preprocessing import LabelEncoder
    label = LabelEncoder()
    y[:,0] = label.fit_transform(y[:,0])
    j = y.flatten()
    from sklearn.tree import DecisionTreeClassifier
    classifier = DecisionTreeClassifier()
    classifier.fit(y,x)
    h = []

    for i in range(len(set(j))):
        l = list(classifier.predict([[i]]))
        h.append([i,l[0],0])
    h = np.matrix(h)

    for i in range(len(y)):
        k = list(classifier.predict([y[i]]))[0]
        for j in range(len(h)):
            if h[j,1] == k:
                h[j,2] = int(h[j,2]) + 1
    default = [0]
    labels = [""]
    color = []
    for i in range(len(h)):
        default.append(h[i,2])
        labels.append(str(h[i,1]).title())
        color.append('rgba(54, 162, 235, .8)')
    color.append('rgba(54, 162, 235, .8)')
    data = {
        'color':color,
        'labels':labels,
        'default':default,
    }
    return JsonResponse(data)
