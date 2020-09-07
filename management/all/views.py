from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

from .models import User_Data
from .forms import User_Login,User_register,Change_Password
from school.models import School_Management
from library.models import Library_Management
from hotel.models import Hotel_Management
from restaurant.models import Rest_Management
from random import randint


def logout(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('school'):
            del request.session['school']
        if request.session.has_key('faculty'):
            del request.session['faculty']
        if request.session.has_key('examiner'):
            del request.session['examiner']
        if request.session.has_key('library'):
            del request.session['library']
        if request.session.has_key('rest'):
            del request.session['rest']
        if request.session.has_key('hotel'):
            del request.session['hotel']
        del request.session['user']
        return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def home(request,*args,**kwargs):
    if request.session.has_key('user'):
        home = []
        if request.session.has_key('school'):
            home.append('school')
        if request.session.has_key('faculty'):
            home.append('faculty')
        if request.session.has_key('examiner'):
            home.append('examiner')
        if request.session.has_key('library'):
            home.append('library')
        if request.session.has_key('rest'):
            home.append('rest')
        if request.session.has_key('hotel'):
            home.append('hotel')
        len_of_home = len(home)
        context = {
            'length': len_of_home,
            'home': home,
        }
        print(home)
        return render(request,'all/home.html',context)
    else:
        return redirect('all:user-login')

def contact(request,*args,**kwargs):
    if request.method == 'POST':
        print("sdgsd")
        data = request.POST.copy()
        message1 = data.get("message")
        name = data.get("name")
        subject = data.get("subject")
        email = data.get("email")
        message = ("Name: " + name + "\nGmail address: " + email  + "\n" + "Message: " + message1)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['managgiamo123@gmail.com',]
        send_mail( subject, message, email_from, recipient_list )
        return redirect("all:contact")
    return render(request,'all/contact.html')
    
def about(request,*args,**kwargs):
    return render(request,'all/about.html')

def user_register(request,*args,**kwargs):
    if request.session.has_key('user'):
        del request.session['user']
        if request.session.has_key('school'):
            del request.session['school']
        if request.session.has_key('library'):
            del request.session['library']
        if request.session.has_key('rest'):
            del request.session['rest']
        if request.session.has_key('hotel'):
            del request.session['hotel']
    form = User_register(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit = False)
            instance.user_id = instance.username
            instance.mainkey = (instance.username)
            instance.save()
            path = instance.management
            path = path + ':' + path + "-register"
            print(path)
            return redirect(path)
    context = {
        'form': form,
    }
    return render(request,'all/user_register.html',context)

def user_login(request,*args,**kwargs):
    if request.session.has_key('user'):
        return redirect('all:home')
    username_not_available = False
    password_not_available = False
    if request.method == 'POST':
        data = request.POST.copy()
        username = data.get('username')
        print(username)
        password = data.get('password')
        print(password)
        try:
            user = User_Data.objects.get(username = username)
            print(user.username)
            print(user.password)
            if user.username == username and user.password == password:
                mana = user.management.split(',')
                for i in mana:
                    print(i)
                    try:
                        if i == 'school':
                            management = School_Management.objects.get(mainkey = user.mainkey)
                        elif i == 'library':
                            management = Library_Management.objects.get(mainkey = user.mainkey)
                        elif i == 'hotel':
                            management = Hotel_Management.objects.get(mainkey = user.mainkey)
                        elif i == 'rest':
                            management = Rest_Management.objects.get(mainkey = user.mainkey)
                        request.session[i] = management.superkey
                    except:
                        user.management = ''
                        user.save()
                        request.session['user'] = user.mainkey
                        return redirect('all:home')
                request.session['user'] = user.mainkey    
                return redirect('all:home')
            else:
                password_not_available = True
        except Exception:
            username_not_available = True
    context = {
        'username_not_available': username_not_available,
        'password_not_available': password_not_available,
    }
    return render(request,'all/user_login.html',context)

def account(request,*args,**kwargs):
    if request.session.has_key('user'):
        home = []
        if request.session.has_key('school'):
            home.append('school')
        if request.session.has_key('faculty'):
            home.append('faculty')
        if request.session.has_key('examiner'):
            home.append('examiner')
        if request.session.has_key('library'):
            home.append('library')
        if request.session.has_key('rest'):
            home.append('rest')
        if request.session.has_key('hotel'):
            home.append('hotel')
        len_of_home = len(home)
        user = User_Data.objects.get(mainkey = request.session['user'])
        context = {
            'length': len_of_home,
            'home': home,
            'user':user,
        }
        return render(request,'all/account.html',context)
    else:
        return redirect('all:user-login')


def username(request,*args,**kwargs):
    username_not = False
    if request.method == "POST":
        data = request.POST.copy()
        username = data.get('username')
        print(username)
        try:
            user = User_Data.objects.get(username=username)
            return redirect('all:otp-verification',username)
        except:
            username_not = True
    return render(request,'all/username.html',{'username_not':username_not})

def otp_verification(request,username=None,*args,**kwargs):
    if request.session.has_key('user'):
        key = request.session['user']
        user = User_Data.objects.get(superkey=key)
    elif username != None:
        user = User_Data.objects.get(username=username)
    else:
        return redirect('all:username')
    otp = randint(100000,999999)
    subject = "[MANAGGIAMO] Account Verification Code."
    message = ("Hey " + str(user.username) + "\nThe changing password attempt require futher verfication because we did not recognize your decive. To Complete the verification enter code on the unrecognized device.\nVerification Code: " + str(otp))
    email_from = settings.EMAIL_HOST_USER
    email = user.emailid
    recipient_list = [email,]
    send_mail( subject, message, email_from, recipient_list )
    print(user)
    return redirect('all:otp',otp,user)

def otp_confirm(request,otp=None,user=None,*args,**kwargs):
    if(otp == None or user == None):
        return redirect("all:otp-verification",user)
    confirm = False
    otp_not = False
    print(user)
    user = User_Data.objects.get(username=user)
    if request.method == "POST":
        confirm = True
        data = request.POST.copy()
        otp_verification = data.get('otp')
        if int(otp) == int(otp_verification):
            request.session['user_otp'] = user.username
            return redirect('all:change-password')
        else:
            otp_not = True
    context = {
        'user': user,
        'confirm': confirm,
        'otp': otp_not,
    }
    return render(request,'all/opt_verification.html',context)

def change_password(request,*args,**kwargs):
    if request.session.has_key('user_otp'):
        form = Change_Password(request.POST or None)
        if request.method == "POST":
            username = request.session['user_otp']
            print(request.session['user_otp'])
            user = User_Data.objects.get(username=username)
            if form.is_valid():
                instance = form.save(commit=False)
                user.password = instance.password
                user.save()
                del request.session['user_otp']
                return redirect('all:user-login')
        context = {
            'form': form,
        }
        return render(request,'all/change_password.html',context)
    else:
        if request.session.has_key('user'):
            key = request.session['user']
            user = User_Data.objects.get(superkey=key)
            return redirect('all:otp-verification',user.username)
        else:
            return redirect('all:username')


def service(request,*args,**kwargs):
    return render(request,'all/service.html')