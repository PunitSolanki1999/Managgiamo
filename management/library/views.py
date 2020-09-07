from django.shortcuts import render,redirect
import datetime
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from random import randint

from .models import Library_Member_Register, Library_Book_Register, Library_Management, Book_Issue, Library_Fine
from .forms import Library_Book_Detail, Library_Management_Register, Library_Member_Detail, Library_Login, Book_Issue_Form, Library_Fine_Detail, Change_Library_Password, Update_Library_Detail

from all.models import User_Data
# Create your views here.
# def logout(request,*args,**kwargs):
#     if request.session.has_key('library'):
#         del request.session['library']
#         return redirect('library:library-login')
#     else:
#         return redirect('library:library-login')

# def login(request,*args,**kwargs):
#     if request.session.has_key('library'):
#         return redirect('library:library-interface')
#     form = Library_Login(request.POST or None)
#     username_not_available = False
#     password_not_available = False
#     if request.method == 'POST':
#         data = request.POST.copy()
#         username = data.get('username')
#         password = data.get('password')
#         try:
#             user = Library_Management.objects.get(username = username)
#             if user.username == username and user.password == password:
#                 request.session['library'] = user.superkey
#                 return redirect('library:library-interface')
#             else:
#                 password_not_available = True
#         except Exception:
#             username_not_available = True
#     context = {
#         'form': form,
#         'username_not_available': username_not_available,
#         'password_not_available': password_not_available,
#     }
#     return render(request,'library/login.html',context)

def register(request,*args,**kwargs):
    if request.session.has_key('user'):
        form = Library_Management_Register(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                instance = form.save(commit = False)
                manage = User_Data.objects.get(mainkey = request.session['user'])
                instance.username = manage.username
                instance.password = manage.password
                instance.mainkey = manage.mainkey
                manage.management = manage.management + 'library,'
                user = Library_Management.objects.all()
                c = user.count()
                c = c + 1
                instance.user_id = ("LM" + str(c))
                instance.superkey = (instance.username)
                instance.save()
                manage.save()
                request.session['library'] = instance.superkey
                return redirect('library:library-interface')
        context = {
            'form': form,
        }
        return render(request,'library/register.html',context)
    else:
        return redirect('all:user-login')

def library_interface(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('library'):
            key = request.session['library']
            member = Library_Member_Register.objects.filter(Q(superkey__iexact=key)).count()
            book = Book_Issue.objects.filter(Q(superkey__iexact=key)).count()
            total_book = Library_Book_Register.objects.filter(Q(superkey__iexact=key)).count()
            fine = Library_Fine.objects.filter(Q(superkey__iexact=key))
            fine = fine[::-1]
            context = {
                'fine': fine,
                'total_book': total_book,
                'book': book,
                'member': member,
            }
            return render(request,'library/library_interface.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def library_book_register(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('library'):
            form = Library_Book_Detail(request.POST or None)
            if request.method == 'POST':
                if form.is_valid():
                    data = request.POST.copy()
                    instance = form.save(commit = False)
                    key = request.session['library']
                    instance.superkey = key
                    no_of_books = int(data.get("book"))
                    user = Library_Book_Register.objects.filter(Q(superkey__iexact = key))
                    a = len(user)
                    for i in range(0,no_of_books):
                        form1 = Library_Book_Register(request.POST or None)
                        form1 = instance
                        form1.pk = None
                        form1.accession_no = a + 1
                        a = a + 1
                        form1.save()
                    return redirect("library:book-register")
            context = {
                'form': form,
            }
            return render(request,'library/book_register_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def library_member_register(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('library'):
            form = Library_Member_Detail(request.POST or None)
            if request.method == 'POST':
                if form.is_valid():
                    instance = form.save(commit = False)
                    key = request.session['library']
                    instance.superkey = key
                    instance.save()
                    return redirect('library:member-in-library',instance.pk)
            context = {
                'form': form,
            }
            return render(request,'library/member_register_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def update_fine(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('library'):
            if request.method == 'POST':
                data = request.POST.copy()
                fine = data.get('fine')
                day = data.get('no_of_days')
                key = request.session['library']
                user = Library_Management.objects.get(superkey = key)
                user.fine = fine
                user.no_of_days = day
                user.save()
                return redirect('library:library-interface')
            return render(request,'library/library_update_fine.html')
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def book_issue(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('library'):
            accession_not_found = False
            member_not_found = False
            limit = False
            book_issued = False
            form = Book_Issue_Form(request.POST or None)
            key = request.session['library']
            days = Library_Management.objects.get(superkey = key)
            if request.method == 'POST':
                if form.is_valid():
                    instance = form.save(commit=False)
                    instance.superkey = key
                    try:
                        accession = Library_Book_Register.objects.filter(Q(accession_no__iexact = instance.accession_no) & Q(superkey__iexact = key) &Q(isbn_number__iexact = instance.isbn_number))
                        if not accession:
                            raise Exception
                        for i in accession:
                            if(i.issue == True):
                                book_issued = True
                    except Exception:
                        accession_not_found = True
                    try:
                        member = Library_Member_Register.objects.get(member_id = instance.member_id)
                        if member.superkey != key:
                            raise Exception
                    except Exception:
                        member_not_found = True
                    mem = Book_Issue.objects.filter(Q(member_id__icontains=instance.member_id))
                    c = mem.count()
                    if c >= 5:
                        limit = True
                    if(accession_not_found == False and member_not_found == False and limit == False and book_issued == False):
                        for i in accession:
                            i.issue = True
                            i.save()
                        instance.save()
                        return redirect('library:book-issue')
            form.fields['date_of_issue'].initial = datetime.date.today()
            form.fields['date_of_return'].initial = datetime.date.today() + datetime.timedelta(days=days.no_of_days)
            context = {
                'form': form,
                'member': member_not_found,
                'isbn': accession_not_found,
                'book_issued' : book_issued,
                'limit': limit,
                'days' : days,
            }
            return render(request,'library/book_issue.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def return_book_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('library'):
            book = None
            if request.method == 'POST':
                data = request.POST.copy()
                key = request.session['library']
                accession = data.get('search')
                member_id = data.get('member')
                book = Book_Issue.objects.filter(Q(superkey__iexact = key) & (Q(accession_no__icontains = accession) & Q(member_id__icontains = member_id)))
            context = {
                'book': book,
            }
            return render(request,'library/return_book_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def return_book(request,pk=None,*args,**kwargs):
    context = {}
    if request.session.has_key('user'):
        if request.session.has_key('library'):
            if(pk != None):
                fine = 0
                try:
                    user = Book_Issue.objects.get(pk=pk)
                except Exception:
                    return redirect("library:library-interface")
                key = request.session['library']
                library = Library_Management.objects.get(superkey = key)
                if((library.fine) & library.fine != 0):
                    day = (datetime.date.today() - user.date_of_return).days
                    if(day > 0):
                        fine = str(day * library.fine)
                    context = {
                        'fine': fine,
                    }
                if request.method == 'POST':
                    book = Library_Book_Register.objects.filter(Q(superkey__iexact =key) & Q(accession_no__iexact = user.accession_no))
                    if user.date_of_return < datetime.date.today():
                        form = Library_Fine_Detail(request.POST or None)
                        if((library.fine) & library.fine != 0):
                            instance = form.save(commit=False)
                            instance.superkey = key
                            instance.accession_no = user.accession_no
                            instance.isbn_number = user.isbn_number
                            instance.member_id = user.member_id
                            instance.date_of_issue = user.date_of_issue
                            instance.date_of_return = user.date_of_return
                            instance.return_date = datetime.date.today()
                            instance.fine = fine
                            instance.save()
                    for i in book:
                        i.issue = False
                        i.save()
                    user.delete()
                    return redirect('library:return-book-form')

                return render(request,'library/return_book.html',context)
            else:
                return redirect('library:return-book-form')
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def book_in_library_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('library'):
            confirm = False
            book = None
            context = {
                'confirm': confirm,
            }
            if request.method == 'POST':
                data = request.POST.copy()
                search = data.get('search')
                key = request.session['library']
                search1 = data.get('search1')
                filter1 = data.get('filter')
                if(filter1 == "author"):
                    book = Library_Book_Register.objects.filter(Q(superkey__iexact = key) & (Q(book_name__icontains = search) & (Q(author1__icontains = search1) | Q(author2__icontains = search1))))
                elif(filter1 == "accession"):
                    book = Library_Book_Register.objects.filter(Q(superkey__iexact = key) & Q(book_name__icontains = search) & Q(accession_no__iexact = search1))
                elif(filter1 == "publication"):
                    book = Library_Book_Register.objects.filter(Q(superkey__iexact = key) & Q(book_name__icontains = search) & Q(publication__icontains = search1))
                confirm = True
                context = {
                    'book': book,
                    'confirm': confirm,
                }
            return render(request,'library/book_in_library_form.html',context)   
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def book_in_library(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('library'):
            if(pk != None):
                detail = Library_Book_Register.objects.get(pk = pk)
                context = {
                    'detail': detail,
                }
                return render(request,'library/book_in_library.html',context)
            else:
                return redirect('library:book-in-library-form')
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def member_in_library_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('library'):
            confirm = False
            context = {
                'confirm': confirm,
            }
            if request.method == 'POST':
                data = request.POST.copy()
                search = data.get('search')
                key = request.session['library']
                member = Library_Member_Register.objects.filter(Q(superkey__iexact = key) & Q(member_id__icontains = search))
                confirm = True
                context = {
                    'member': member,
                    'confirm': confirm,
                }
            return render(request,'library/member_in_library_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def member_in_library(request,pk=None,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('library'):
            if(pk != None):
                detail = Library_Member_Register.objects.get(pk = pk)
                context = {
                    'detail': detail,
                }
                return render(request,'library/member_in_library.html',context)
            else:
                return redirect('library:member-in-library-form')
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def book_issue_detail_form(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('library'):
            confirm = False
            context = {
                'confirm': confirm,
            }
            if request.method == 'POST':
                data = request.POST.copy()
                isbn_number = data.get('isbn_number')
                member_id = data.get('member_id')
                key = request.session['library']
                book = Book_Issue.objects.filter(Q(superkey__iexact = key) & Q(isbn_number__icontains = isbn_number) & Q(member_id__icontains = member_id))
                confirm = True
                context = {
                    'book': book,
                    'confirm': confirm,
                }
            return render(request,'library/book_issue_detail_form.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def library_book_fine(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('library'):
            confirm = False
            context = {
                'confirm': confirm,
            }
            key = request.session['library']
            book = Library_Fine.objects.filter(Q(superkey__iexact = key))
            confirm = True
            context = {
                'book': book,
                'confirm': confirm,
            }
            return render(request,'library/library_book_fine.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')

def library_account_detail(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('library'):
            key = request.session['library']
            user = Library_Management.objects.get(superkey = key)
            context = {
                'user': user,
            }
            return render(request,'library/library_account_detail.html',context)
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
#             user = Library_Management.objects.get(username=username)
#             return redirect('library:otp-verification',username)
#         except:
#             username_not = True
#     return render(request,'library/username.html',{'username_not':username_not})

# def otp_verification(request,username=None,*args,**kwargs):
#     if request.session.has_key('library'):
#         key = request.session['library']
#         library = Library_Management.objects.get(superkey=key)
#     elif username != None:
#         library = Library_Management.objects.get(username=username)
#     else:
#         return redirect('library:username')
#     otp = randint(100000,999999)
#     subject = "[MANAGGIAMO] Account Verification Code."
#     message = ("Hey " + str(library.username) + "\nThe changing password attempt require futher verfication because we did not recognize your decive. To Complete the verification enter code on the unrecognized device.\nVerification Code: " + str(otp))
#     email_from = settings.EMAIL_HOST_USER
#     email = library.emailid
#     recipient_list = [email,]
#     send_mail( subject, message, email_from, recipient_list )
#     return redirect('library:otp',otp,library)

# def otp_confirm(request,otp=None,library=None,*args,**kwargs):
#     if(otp == None or library == None):
#         return redirect("library:otp-verification",library)
#     confirm = False
#     otp_not = False
#     library = Library_Management.objects.get(username=library)
#     if request.method == "POST":
#         confirm = True
#         data = request.POST.copy()
#         otp_verification = data.get('otp')
#         if int(otp) == int(otp_verification):            
#             request.session['library_otp'] = library.username
#             return redirect('library:change-password')
#         else:
#             otp_not = True
#     context = {
#         'library': library,
#         'confirm': confirm,
#         'otp': otp_not,
#     }
#     return render(request,'library/opt_verification.html',context)

# def change_password(request,*args,**kwargs):
#     if request.session.has_key('library_otp'):
#         form = Change_Library_Password(request.POST or None)
#         if request.method == "POST":
#             username = request.session['library_otp']
#             library = Library_Management.objects.get(username=username)
#             if form.is_valid():
#                 instance = form.save(commit=False)
#                 library.password = instance.password
#                 library.save()
#                 del request.session['library_otp']
#                 return redirect('library:library-login')
#         context = {
#             'form': form,
#         }
#         return render(request,'library/change_password.html',context)
#     else:
#         if request.session.has_key('library'):
#             key = request.session['library']
#             library = Library_Management.objects.get(superkey=key)
#             return redirect('library:otp-verification',library.username)
#         else:
#             return redirect('library:username')

def update_library_detail(request,*args,**kwargs):
    if request.session.has_key('user'):
        if request.session.has_key('library'):
            key = request.session['library']
            form = Update_Library_Detail(request.POST or None)
            library = Library_Management.objects.get(superkey=key)
            form.fields['emailid'].initial = library.emailid
            form.fields['phone'].initial = library.phone
            form.fields['library_name'].initial = library.library_name
            form.fields['state'].initial = library.state
            form.fields['city'].initial = library.city
            form.fields['pincode'].initial = library.pincode
            form.fields['address'].initial = library.address
            if request.method == "POST":
                if form.is_valid():
                    instance = form.save(commit=False)
                    library.emailid = instance.emailid
                    library.phone = instance.phone
                    library.address = instance.address
                    library.save()
                    return redirect('library:library-account-detail')
            context = {
                'form': form,
            }
            return render(request,'library/update_library_detail.html',context)
        else:
            return redirect('all:user-login')
    else:
        return redirect('all:user-login')