from django import forms
from .models import Library_Management, Library_Book_Register, Library_Member_Register, Book_Issue, Library_Fine

class Library_Management_Register(forms.ModelForm):
    emailid         = forms.EmailField(label="Email Id",max_length=100,required=True,widget=forms.EmailInput(attrs={'class':"au-input au-input--full",'placeholder':'example:Example@gmail.com','title':'Enter your Email Address. example:examle@gmail.com'}))
    phone           = forms.IntegerField(label="Contact No.",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Contact Number','title':'Enter your Contact Number.'}))
    library_name    = forms.CharField(label="Library Name",max_length=50,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Library Name','title':'Enter your Library Name.'}))
    state           = forms.CharField(label="State",max_length=30,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'State','title':'Enter the state where library is located.'}))
    city            = forms.CharField(label="City",max_length=30,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'City','title':'Enter the city where library is located.'}))
    pincode         = forms.IntegerField(label="Pincode",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Pincode','title':"Enter The Pincode of the city."}))
    address         = forms.CharField(label="Address",max_length=200,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Address','title':'Enter Address of Library.'}))
    fine            = forms.IntegerField(label="Late Return Fine",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Fine per Day','title':'Enter the Fine taken per day if the customer unable to return book on time.'}))
    no_of_days      = forms.IntegerField(label="Max Borrowing Days",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Max Borrowing Days','title':'Enter the No. of days that a book is given to customer.'}))

    class Meta:
        model = Library_Management
        fields = [   
            'emailid',     
            'phone',       
            'library_name',
            'state',       
            'city',        
            'pincode',     
            'address',
            'no_of_days',     
            'fine', 
        ]
    
    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if(len(username) <= 2):
    #         raise forms.ValidationError('Please a enter username contain more than 3 characters.')
    #     return username

    # def clean_password(self):
    #     password = self.cleaned_data.get('password')
    #     if(len(password) < 6 or len(password) > 12):
    #         raise forms.ValidationError('Please a enter password of 6 to 14 character.')
    #     return password

    # def clean_cpassword(self):
    #     password = self.cleaned_data.get('password')
    #     cpassword = self.cleaned_data.get('cpassword')
    #     if password != cpassword:
    #         raise forms.ValidationError("Password and Confirm Password is not same")
    #     return cpassword
    
    def clean_emailid(self):
        email = self.cleaned_data.get('emailid')
        if "@gmail.com" not in email:
            raise forms.ValidationError("please Enter appropriate Email")
        return email

    def clean_library_name(self):
        library_name = self.cleaned_data.get('library_name')
        if(len(library_name) <= 2 or len(library_name) >= 30):
            raise forms.ValidationError('Please a enter a approriate Library Name')
        library = library_name.split(' ')
        if(len(library) != 1):
            try:
                if(not (library[0].isalpha() & library[1].isalpha())):
                    raise forms.ValidationError('Name Should not contain integers')
            except:
                raise forms.ValidationError('Please Enter Appropriate Name')
        else:
            if(not (library[0].isalpha())):
                raise forms.ValidationError('Name Should not contain integers')
        return library_name
        
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        c = 0
        p = phone
        while(p != 0):
            p = p // 10
            c = c + 1
        if(c != 10):
            raise forms.ValidationError("Enter valid phone number")
        return phone

    def clean_pincode(self):
        pincode = self.cleaned_data.get('pincode')
        c = 0
        p = pincode
        while(p != 0):
            p = p // 10
            c = c + 1
        if(c != 6):
            raise forms.ValidationError("Enter valid pincode")
        return pincode

    def clean_no_of_days(self):
        day = self.cleaned_data.get('no_of_days')
        if(day > 366):
            return forms.ValidationError("Book Issue Days Can't be greater than the days in a year.")
        return day

class Library_Book_Detail(forms.ModelForm):
    isbn_number     = forms.IntegerField(label="ISBN Number",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'ISBN Number'}))
    book_name       = forms.CharField(label="Book Name",max_length=100,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Book Name'}))
    publication     = forms.CharField(label="Publication",max_length=60,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Publication'}))
    author1         = forms.CharField(label="Author 1",max_length=50,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Name of 1st Author'}))
    author2         = forms.CharField(label="Author 2",max_length=50,required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Name of 2nd Author'}))
    with_cd         = forms.BooleanField(label="With CD",required=False)
    no_of_pages     = forms.IntegerField(label="Total No. of Pages",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Total Pages in Book'}))
    edition         = forms.CharField(label="Edition",max_length=40,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Edition of Book'}))
    category        = forms.CharField(label="Catrgory",max_length=60,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Book is of which Field'}))

    class Meta:
        model = Library_Book_Register
        fields = [       
            'isbn_number',    
            'book_name',      
            'publication',    
            'author1', 
            'author2',
            'with_cd',
            'no_of_pages',        
            'edition',        
            'category',               
        ]

    def clean_isbn_number(self):
        isbn_number = self.cleaned_data.get('isbn_number')
        c = 0
        p = int(isbn_number)
        while(p != 0):
            p = p // 10
            c = c + 1
        if(c != 10 | c != 14):
            raise forms.ValidationError("Enter valid isbn number number")
        return isbn_number

class Library_Member_Detail(forms.ModelForm):
    
    male = 'male'
    female = 'female'
    other = 'other'

    GENDER = (
        (male,"Male"),
        (female,"Female"),
        (other,"Other"),
    )
    member_id       = forms.CharField(label="Member ID",max_length=50,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Member ID'}))
    fname           = forms.CharField(label="First Name",max_length=20,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'First Name'}))
    mname           = forms.CharField(label="Middle Name",max_length=20,required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Middle Name'}))
    lname           = forms.CharField(label="Last Name",max_length=20,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Last Name'}))
    gender          = forms.ChoiceField(label="Gender",choices=GENDER,required=True)
    dob             = forms.DateField(label="DOB",widget=forms.DateInput(attrs={'type':'date'}))
    emailid         = forms.EmailField(label="Email ID",max_length=100,required=True,widget=forms.EmailInput(attrs={'class':"au-input au-input--full",'placeholder':'Email Address'}))
    phone           = forms.IntegerField(label="Contact No.",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Contact Number'}))
    address         = forms.CharField(label="Address",max_length=200,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Address'}))

    class Meta:
        model = Library_Member_Register
        fields = [
            'member_id',
            'fname',    
            'mname',    
            'lname', 
            'gender',   
            'dob',      
            'emailid',  
            'phone',           
            'address',  
        ]
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        c = 0
        p = phone
        while(p != 0):
            p = p // 10
            c = c + 1
        if(c != 10):
            raise forms.ValidationError("Enter valid phone number")
        return phone

    def clean_fname(self):
        fname = self.cleaned_data.get('fname')
        if(len(fname) <= 2 or len(fname) >= 15):
            raise forms.ValidationError('Please a enter a approriate First Name')
        if(not fname.isalpha()):
            raise forms.ValidationError('Please a enter a approriate First Name')
        return fname
    
    def clean_mname(self):
        mname = self.cleaned_data.get('mname')
        if mname != '':
            if(len(mname) <= 2 or len(mname) >= 15):
                raise forms.ValidationError('Please a enter a approriate Middle Name')
            if(not mname.isalpha()):
                raise forms.ValidationError('Please a enter a approriate Middle Name')
        return mname

    def clean_lname(self):
        lname = self.cleaned_data.get('lname')
        if(len(lname) <= 2 or len(lname) >= 15):
            raise forms.ValidationError('Please a enter a approriate Last Name')
        if(not lname.isalpha()):
            raise forms.ValidationError('Please a enter a approriate Last Name')
        return lname

    def clean_emailid(self):
        email = self.cleaned_data.get('emailid')
        if "@gmail.com" not in email:
            raise forms.ValidationError("please Enter appropriate Email")
        return email
    

class Library_Login(forms.Form):
    username        = forms.CharField(label="",max_length=20,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Username'}))
    password        = forms.CharField(label="",max_length=20,required=True,widget=forms.PasswordInput(attrs={'class':"au-input au-input--full",'placeholder':'Password'}))
    
    class Meta:
        fields = [
            'username',
            'password',
        ]

class Book_Issue_Form(forms.ModelForm):
    isbn_number     = forms.IntegerField(widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'ISBN Number'}))
    member_id       = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Member ID'}))
    accession_no    = forms.IntegerField(widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Accession Number'}))
    date_of_issue   = forms.DateField(required=False,widget=forms.DateInput(attrs={'type':'date','readonly':'True'}))
    date_of_return  = forms.DateField(required=False,widget=forms.DateInput(attrs={'type':'date','readonly':'True'}))

    class Meta:
        model = Book_Issue
        fields = [
            'isbn_number',   
            'member_id',     
            'accession_no',
            'date_of_issue', 
            'date_of_return',
        ]

    def clean_isbn_number(self):
        isbn_number = self.cleaned_data.get('isbn_number')
        c = 0
        p = isbn_number
        while(p != 0):
            p = p // 10
            c = c + 1
        if(c != 10 | c != 14):
            raise forms.ValidationError("Enter valid isbn number number")
        return isbn_number

class Library_Fine_Detail(forms.ModelForm):
    superkey        = forms.CharField(max_length=50,required=False,widget=forms.TextInput())
    isbn_number     = forms.CharField(max_length=50,required=False,widget=forms.TextInput())
    member_id       = forms.CharField(max_length=50,required=False,widget=forms.TextInput())
    date_of_issue   = forms.DateField(required=False)
    date_of_return  = forms.DateField(required=False)
    return_date     = forms.DateField(required=False)
    fine            = forms.CharField(required=False,widget=forms.TextInput())

    class Meta:
        model = Library_Fine
        fields = [
            'superkey',
            'isbn_number',
            'member_id',
            'date_of_issue',
            'date_of_return',
            'return_date',
            'fine',       
        ]


class Change_Library_Password(forms.ModelForm):
    password        = forms.CharField(label="Password",max_length=20,required=True,widget=forms.PasswordInput(attrs={'class':"au-input au-input--full",'placeholder':'Password'}))
    cpassword       = forms.CharField(label="Confirm Password",max_length=20,required=True,widget=forms.PasswordInput(attrs={'class':"au-input au-input--full",'placeholder':'Confirm Password'}))

    class Meta:
        model = Library_Management
        fields = [
            'password',
            'cpassword',
        ]

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if(len(password) < 6 or len(password) > 12):
            raise forms.ValidationError('Please a enter password of 6 to 14 character.')
        return password

    def clean_cpassword(self):
        password = self.cleaned_data.get('password')
        cpassword = self.cleaned_data.get('cpassword')
        if password != cpassword:
            raise forms.ValidationError("Password and Confirm Password is not same")
        return cpassword


class Update_Library_Detail(forms.ModelForm):
    emailid         = forms.EmailField(label="Email ID",max_length=100,required=True,widget=forms.EmailInput(attrs={'class':"au-input au-input--full"}))
    phone           = forms.IntegerField(label="Contact Number",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    library_name    = forms.CharField(label="Library Name",max_length=50,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':'True'}))
    state           = forms.CharField(label="State",max_length=30,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':'True'}))
    city            = forms.CharField(label="City",max_length=30,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':'True'}))
    pincode         = forms.IntegerField(label="Pincode",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':'True'}))
    address         = forms.CharField(label="Address",max_length=200,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))

    class Meta:
        model = Library_Management
        fields = [
            'emailid',
            'phone',
            'library_name',
            'state',
            'city',
            'pincode',
            'address',
        ]

    def clean_emailid(self):
        email = self.cleaned_data.get('emailid')
        if "@gmail.com" not in email:
            raise forms.ValidationError("please Enter appropriate Email")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        c = 0
        p = phone
        while(p != 0):
            p = p // 10
            c = c + 1
        if(c != 10):
            raise forms.ValidationError("Enter valid phone number")
        return phone


