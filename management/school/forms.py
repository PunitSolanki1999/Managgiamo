from django import forms
from .models import School_Management, School_Employee_Data, School_Faculty_Data,School_Marks_Data, School_Student_Data, School_Examination_Data, School_Total_Attendance

none        = None
nursery     = 'nursery'
lkg         = 'lkg'
pre_first   = 'pre first'
first       = 'first'
second      = 'second'
third       = 'third'
fourth      = 'fourth'
fifth       = 'fifth'
sixth       = 'sixth'
seventh     = 'seventh'
eigth       = 'eigth'
ninth       = 'ninth'
tenth       = 'tenth'
eleventh    = 'eleventh'
twelveth    = 'twelveth'
CLASS_CHOICE = (
    (none,'None'),
    (nursery,'Nursery'),
    (lkg,'LKG'),
    (pre_first,'Pre First'),
    (first,'First'),
    (second,'Second'),
    (third,'Third'),
    (fourth,'Fourth'),
    (fifth,'Fifth'),
    (sixth,'Sixth'),
    (seventh,'Seventh'),
    (eigth,'Eigth'),
    (ninth,'Ninth'),
    (tenth,'Tenth'),
    (eleventh,'Eleventh'),
    (twelveth,'Twelveth'),
)

class SchoolLogin(forms.Form):
    username = forms.CharField(label="Username",max_length=20,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Username'}))
    password = forms.CharField(label="Password",max_length=20,widget=forms.PasswordInput(attrs={'class':"au-input au-input--full",'placeholder':'Password'}))

    class Meta:
        fields = [
            'username',
            'password',
        ]

class SchoolRegister(forms.ModelForm):
    # username        = forms.CharField(label="Username",max_length=20,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Username'}))
    # password        = forms.CharField(label="Password",max_length=20,widget=forms.PasswordInput(attrs={'class':"au-input au-input--full",'placeholder':'Password'}))
    # cpassword       = forms.CharField(label="Confirm Password",max_length=20,widget=forms.PasswordInput(attrs={'class':"au-input au-input--full",'placeholder':'Confirm Password'}))
    emailid         = forms.EmailField(label="Email ID",max_length=100,widget=forms.EmailInput(attrs={'class':"au-input au-input--full",'placeholder':'Email ID'}))
    phone           = forms.IntegerField(label="Contact Number",widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Contact Number'}))
    organisation    = forms.CharField(label="School Name",max_length=20,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'School Name'}))
    school_code     = forms.CharField(label="School Code",max_length=10,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'School Code'}))
    state           = forms.CharField(label="State",max_length=30,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'State'}))
    city            = forms.CharField(label="City",max_length=30,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'City'}))
    pincode         = forms.IntegerField(label="Pincode",widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Pincode'}))
    address         = forms.CharField(label="Address",max_length=200,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Address'}))

    class Meta:
        model = School_Management
        fields = [
            # 'username',
            # 'password',
            # 'cpassword',
            'emailid',
            'school_code',
            'phone',
            'organisation',
            'state',
            'city',
            'pincode',
            'address',
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
    
    def clean_organisation(self):
        organisation = self.cleaned_data.get('organisation')
        if(len(organisation) <= 2 or len(organisation) >= 30):
            raise forms.ValidationError('Please a enter a approriate Organization Name')
        organisation_name = organisation.split(' ')
        if(len(organisation_name) != 1):
            try:
                if(not (organisation_name[0].isalpha() & organisation_name[1].isalpha())):
                    raise forms.ValidationError('Name Should not contain integers')
            except:
                raise forms.ValidationError('Please Enter Appropriate Name')
        else:
            if(not (organisation_name[0].isalpha())):
                raise forms.ValidationError('Name Should not contain integers')
        return organisation

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


class Faculty_Data_Insert(forms.ModelForm):
    username        = forms.CharField(label="Username",max_length=20,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Username'}))
    password        = forms.CharField(label="Password",max_length=20,widget=forms.PasswordInput(attrs={'class':"au-input au-input--full",'placeholder':'Password'}))
    cpassword       = forms.CharField(label="Confirm Password",max_length=20,widget=forms.PasswordInput(attrs={'class':"au-input au-input--full",'placeholder':'Confirm Password'}))
    faculty_no      = forms.IntegerField(label="Faculty Number",widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'id generate acoording to number'}))
    fname           = forms.CharField(label="First Name",max_length=20,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'First Name'}))
    mname           = forms.CharField(label="Middle Name",max_length=20,required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Middle Name'}))
    lname           = forms.CharField(label="Last Name",max_length=20,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Last Name'}))
    picture         = forms.ImageField(label='Faculty Pic',required=False,widget = forms.FileInput(attrs={'class':"au-input au-input--full","onchange":"readURL(this);"}))
    emailid         = forms.EmailField(label="Email ID",max_length=100,widget=forms.EmailInput(attrs={'class':"au-input au-input--full",'placeholder':'Email ID'}))
    phone           = forms.IntegerField(label="Contact Number",widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Contact Number'}))
    father_name     = forms.CharField(label="Father Name",max_length=50,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Father Name'}))
    father_phone    = forms.IntegerField(label="Father's Contact Number",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':"Father's Contact Number"}))
    mother_name     = forms.CharField(label="Mother Name",max_length=50,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Mother Name'}))
    mother_phone    = forms.IntegerField(label="Mother's Contact Number",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':"Mother's Contact Number"}))
    state           = forms.CharField(label="State",max_length=30,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'State'}))
    city            = forms.CharField(label="City",max_length=30,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'City'}))
    address         = forms.CharField(label="Address",max_length=200,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Address'}))
    pincode         = forms.IntegerField(label="Pincode",widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Pincode'}))
    subject         = forms.CharField(label="Subject",max_length=30,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Subject'}))
    dob             = forms.DateField(label="DOB",widget=forms.DateInput(attrs={'type':'date'}))
    salary          = forms.IntegerField(label="Salary",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Salary'}))
    clas            = forms.ChoiceField(label="Class",choices=CLASS_CHOICE,required=False,widget=forms.Select(attrs={'class':"au-input au-input--full",'placeholder':'Class'}))
    from_date       = forms.DateField(label="Joining Date",required=False,widget=forms.DateInput(attrs={'type':'date','readonly':'True','placeholder':'Joining Date'}))
    
    class Meta:
        model = School_Faculty_Data
        fields = [
            'username',
            'password',
            'cpassword',
            'faculty_no',
            'fname',
            'mname',
            'lname',
            'picture',
            'phone',
            'emailid',
            'father_name',
            'father_phone',
            'mother_name',
            'mother_phone',
            'subject',
            'dob',
            'salary',
            'state',
            'city',
            'address',
            'pincode',
            'clas',
            'from_date',   
        ]
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if(len(username) <= 2):
            raise forms.ValidationError('Please a enter username contain more than 3 characters.')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if(len(password) < 6 or len(password) > 12):
            raise forms.ValidationError('Please a enter password of 6 to 14 character.')
        return password

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

    def clean_cpassword(self):
        password = self.cleaned_data.get('password')
        cpassword = self.cleaned_data.get('cpassword')
        if password != cpassword:
            raise forms.ValidationError("Password and Confirm Password is not same")
        return cpassword
    
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

    def clean_father_name(self):
        father_name = self.cleaned_data.get('father_name')
        name = father_name.split(' ')
        try:
            if(not (name[0].isalpha() & name[1].isalpha())):
                raise forms.ValidationError('Name Should not contain integers')
        except:
            raise forms.ValidationError('Please Enter Appropriate Name')
        return father_name

    def clean_mother_name(self):
        mother_name = self.cleaned_data.get('mother_name')
        name = mother_name.split(' ')
        try:
            if(not (name[0].isalpha() & name[1].isalpha())):
                raise forms.ValidationError('Mother Name Should not contain integers')
        except:
            raise forms.ValidationError('Please Enter Appropriate Name')
        return mother_name

    def clean_father_phone(self):
        father_phone = self.cleaned_data.get('father_phone')
        if father_phone != None:
            c = 0
            p = father_phone
            while(p != 0):
                p = p // 10
                c = c + 1
            if(c != 10):
                raise forms.ValidationError("Enter valid phone number")
        return father_phone

    def clean_mother_phone(self):
        mother_phone = self.cleaned_data.get('mother_phone')
        if mother_phone != None:
            c = 0
            p = mother_phone
            while(p != 0):
                p = p // 10
                c = c + 1
            if(c != 10):
                raise forms.ValidationError("Enter valid phone number")
        return mother_phone

class Student_Data_Insert(forms.ModelForm):
    scholar_no      = forms.IntegerField(label="Scholar Number",widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'id generate acoording to number','readonly':'true'}))
    fname           = forms.CharField(label="First Name",max_length=20,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'First Name'}))
    mname           = forms.CharField(label="Middle Name",max_length=20,required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Middle Name'}))
    lname           = forms.CharField(label="Last Name",max_length=20,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Last Name'}))
    picture         = forms.ImageField(label='Student Pic',required=False,widget = forms.FileInput(attrs={"onchange":"readURL(this);"}))
    father_name     = forms.CharField(label="Father Name",max_length=50,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Father Name'}))
    father_phone    = forms.IntegerField(label="Father Contact Number",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':"Father's Contact Number"}))
    mother_name     = forms.CharField(label="Mother Name",max_length=50,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Mother Name'}))
    mother_phone    = forms.IntegerField(label="Mother's Contact Number",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':"Mother's Contact Number"}))
    state           = forms.CharField(label="State",max_length=30,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'state'}))
    city            = forms.CharField(label="City",max_length=30,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'City'}))
    pincode         = forms.IntegerField(label="Pincode",widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Pincode'}))
    address         = forms.CharField(label="Address",max_length=200,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Address'}))
    dob             = forms.DateField(label="DOB",widget=forms.DateInput(attrs={'type':'date'}))
    fee             = forms.IntegerField(label="Fee of the Student",widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Fee of the Student'}))
    clas            = forms.ChoiceField(label="Class",choices=CLASS_CHOICE,required=False,widget=forms.Select(attrs={'class':"au-input au-input--full",'placeholder':'Class'}))
    from_date       = forms.DateField(label="Joining Date",required=False,widget=forms.DateInput(attrs={'class':"au-input au-input--full",'type':'date','readonly':'true','placeholder':'Joining Date'}))
    
    class Meta:
        model = School_Student_Data
        fields = [
            'scholar_no',
            'fname',        
            'mname',       
            'lname',  
            'picture',      
            'father_name',  
            'father_phone', 
            'mother_name',  
            'mother_phone', 
            'state',        
            'city',       
            'address', 
            'pincode',           
            'dob',          
            'fee',          
            'clas',         
            'from_date',         
        ]
    
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

    def clean_father_name(self):
        father_name = self.cleaned_data.get('father_name')
        name = father_name.split(' ')
        try:
            if(not (name[0].isalpha() & name[1].isalpha())):
                raise forms.ValidationError('Name Should not contain integers')
        except:
            raise forms.ValidationError('Please Enter Appropriate Name')
        return father_name

    def clean_mother_name(self):
        mother_name = self.cleaned_data.get('mother_name')
        name = mother_name.split(' ')
        try:
            if(not (name[0].isalpha() & name[1].isalpha())):
                raise forms.ValidationError('Mother Name Should not contain integers')
        except:
            raise forms.ValidationError('Please Enter Appropriate Name')
        return mother_name

    def clean_father_phone(self):
        father_phone = self.cleaned_data.get('father_phone')
        if father_phone != None:
            c = 0
            p = father_phone
            while(p != 0):
                p = p // 10
                c = c + 1
            if(c != 10):
                raise forms.ValidationError("Enter valid phone number")
        return father_phone

    def clean_mother_phone(self):
        mother_phone = self.cleaned_data.get('mother_phone')
        if mother_phone != None:
            c = 0
            p = mother_phone
            while(p != 0):
                p = (p//10)
                c = c + 1
            if(c != 10):
                raise forms.ValidationError("Enter valid phone number")
        return mother_phone

class Employee_Data_Insert(forms.ModelForm):
    employee_no     = forms.IntegerField(label="Employee Number",widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'id generate acoording to number'}))
    fname           = forms.CharField(label="First Name",max_length=20,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    mname           = forms.CharField(label="Middle Name",max_length=20,required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    lname           = forms.CharField(label="Last Name",max_length=20,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    phone           = forms.IntegerField(label="Contact Number",widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    picture         = forms.ImageField(label='Employee Pic',required=False,widget = forms.FileInput(attrs={"onchange":"readURL(this);"}))
    father_name     = forms.CharField(label="Father Name",max_length=50,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    father_phone    = forms.IntegerField(label="Father's Contact Number",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    mother_name     = forms.CharField(label="Mother Name",max_length=50,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    mother_phone    = forms.IntegerField(label="Mother's Contact Number",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    work            = forms.CharField(label="Work",max_length=30,required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    dob             = forms.DateField(label="DOB",widget=forms.DateInput(attrs={'type':'date'}))
    salary          = forms.IntegerField(label="Salary",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    state           = forms.CharField(label="State",max_length=30,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    city            = forms.CharField(label="City",max_length=30,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    address         = forms.CharField(label="Address",max_length=200,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    pincode         = forms.IntegerField(label="Pincode",widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    from_date       = forms.DateField(label="Joining Date",required=False,widget=forms.DateInput(attrs={'class':"au-input au-input--full",'type':'date','readonly':'True'}))

    class Meta:
        model = School_Employee_Data
        fields = [
            'employee_no',
            'fname',       
            'mname',       
            'lname',  
            'picture',     
            'phone',       
            'father_name', 
            'father_phone',
            'mother_name', 
            'mother_phone',
            'work',        
            'dob',         
            'salary',      
            'state',       
            'city',       
            'address', 
            'pincode',    
            'from_date',        
        ]

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

    def clean_father_name(self):
        father_name = self.cleaned_data.get('father_name')
        name = father_name.split(' ')
        try:
            if(not (name[0].isalpha() & name[1].isalpha())):
                raise forms.ValidationError('Name Should not contain integers')
        except:
            raise forms.ValidationError('Please Enter Appropriate Name')
        return father_name

    def clean_mother_name(self):
        mother_name = self.cleaned_data.get('mother_name')
        name = mother_name.split(' ')
        try:
            if(not (name[0].isalpha() & name[1].isalpha())):
                raise forms.ValidationError('Mother Name Should not contain integers')
        except:
            raise forms.ValidationError('Please Enter Appropriate Name')
        return mother_name

    def clean_father_phone(self):
        father_phone = self.cleaned_data.get('father_phone')
        if father_phone != None:
            c = 0
            p = father_phone
            while(p != 0):
                p = p // 10
                c = c + 1
            if(c != 10):
                raise forms.ValidationError("Enter valid phone number")
        return father_phone

    def clean_mother_phone(self):
        mother_phone = self.cleaned_data.get('mother_phone')
        if mother_phone != None:
            c = 0
            p = mother_phone
            while(p != 0):
                p = (p//10)
                c = c + 1
            if(c != 10):
                raise forms.ValidationError("Enter valid phone number")
        return mother_phone

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

class Student_Marks_Insertion(forms.ModelForm):
    student_id      = forms.CharField(label="Student ID",max_length=100,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    clas            = forms.ChoiceField(label="Class",choices=CLASS_CHOICE,widget=forms.Select(attrs={'class':"au-input au-input--full"}))
    subject         = forms.CharField(label="Subject",max_length=40,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    marks           = forms.IntegerField(label="Marks",widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))

    class Meta:
        model = School_Marks_Data
        fields = [
            'student_id',
            'clas',
            'subject',
            'marks',
        ]

    def clean_marks(self):
        marks = self.cleaned_data.get('marks')
        if(marks > -1 & marks < 100):
            raise forms.ValidationError("Please Enter Correct Marks")
        return marks

class Student_Data_Update(forms.ModelForm):
    fname           = forms.CharField(label="First Name",max_length=20,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    mname           = forms.CharField(label="Middle Name",max_length=20,required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    lname           = forms.CharField(label="Last Name",max_length=20,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    picture         = forms.ImageField(label='Student Pic',required=False,widget = forms.FileInput(attrs={"onchange":"readURL(this);"}))
    father_name     = forms.CharField(label="Father Name",max_length=50,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    father_phone    = forms.IntegerField(label="Father's Contact Number",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    mother_name     = forms.CharField(label="Mother Name",max_length=50,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    mother_phone    = forms.IntegerField(label="Mother's Contact Number",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    state           = forms.CharField(label="State",max_length=30,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    city            = forms.CharField(label="City",max_length=30,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    address         = forms.CharField(label="Address",max_length=200,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    pincode         = forms.IntegerField(label="Pincode",widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    dob             = forms.DateField(label="DOB",widget=forms.DateInput(attrs={'type':'date'}))
    clas            = forms.ChoiceField(label="Class",choices=CLASS_CHOICE,required=False,widget=forms.Select(attrs={'class':"au-input au-input--full"}))

    class Meta:
        model = School_Student_Data
        fields = [
            'fname',        
            'mname',       
            'lname',   
            'picture',     
            'father_name',  
            'father_phone', 
            'mother_name',  
            'mother_phone', 
            'state',        
            'city',       
            'address',      
            'pincode',      
            'dob',                    
            'clas',               
        ]
    
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

    def clean_father_name(self):
        father_name = self.cleaned_data.get('father_name')
        name = father_name.split(' ')
        try:
            if(not (name[0].isalpha() & name[1].isalpha())):
                raise forms.ValidationError('Name Should not contain integers')
        except:
            raise forms.ValidationError('Please Enter Appropriate Name')
        return father_name

    def clean_mother_name(self):
        mother_name = self.cleaned_data.get('mother_name')
        name = mother_name.split(' ')
        try:
            if(not (name[0].isalpha() & name[1].isalpha())):
                raise forms.ValidationError('Mother Name Should not contain integers')
        except:
            raise forms.ValidationError('Please Enter Appropriate Name')
        return mother_name

    def clean_father_phone(self):
        father_phone = self.cleaned_data.get('father_phone')
        if father_phone != None:
            c = 0
            p = father_phone
            while(p != 0):
                p = p // 10
                c = c + 1
            if(c != 10):
                raise forms.ValidationError("Enter valid phone number")
        return father_phone

    def clean_mother_phone(self):
        mother_phone = self.cleaned_data.get('mother_phone')
        if mother_phone != None:
            c = 0
            p = mother_phone
            while(p != 0):
                p = (p//10)
                c = c + 1
            if(c != 10):
                raise forms.ValidationError("Enter valid phone number")
        return mother_phone

class Faculty_Data_Update(forms.ModelForm):
    fname           = forms.CharField(label="First Name",max_length=20,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    mname           = forms.CharField(label="Middle Name",max_length=20,required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    lname           = forms.CharField(label="Last Name",max_length=20,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    picture         = forms.ImageField(label='Faculty Pic',required=False,widget = forms.FileInput(attrs={"onchange":"readURL(this);"}))
    emailid         = forms.EmailField(label="Email ID",max_length=100,widget=forms.EmailInput(attrs={'class':"au-input au-input--full"}))
    phone           = forms.IntegerField(label="Contact Number",widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    father_name     = forms.CharField(label="Father Name",max_length=50,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    father_phone    = forms.IntegerField(label="Fathe's Contact Number",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    mother_name     = forms.CharField(label="Mother Name",max_length=50,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    mother_phone    = forms.IntegerField(label="Mother's Contact Number",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    state           = forms.CharField(label="State",max_length=30,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    city            = forms.CharField(label="City",max_length=30,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    address         = forms.CharField(label="Address",max_length=200,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    pincode         = forms.IntegerField(label="Pincode",widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    subject         = forms.CharField(label="Subject",max_length=30,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    dob             = forms.DateField(label="DOB",widget=forms.DateInput(attrs={'type':'date'}))
    salary          = forms.IntegerField(label="Salary",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    clas            = forms.ChoiceField(label="Class",choices=CLASS_CHOICE,required=False,widget=forms.Select(attrs={'class':"au-input au-input--full"}))    

    class Meta:
        model = School_Faculty_Data
        fields = [
            'fname',
            'mname',
            'lname',
            'picture',
            'phone',
            'emailid',
            'father_name',
            'father_phone',
            'mother_name',
            'mother_phone',
            'subject',
            'dob',
            'salary',
            'state',
            'city',
            'address',
            'pincode',
            'clas',  
        ]

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

    def clean_father_name(self):
        father_name = self.cleaned_data.get('father_name')
        name = father_name.split(' ')
        try:
            if(not (name[0].isalpha() & name[1].isalpha())):
                raise forms.ValidationError('Name Should not contain integers')
        except:
            raise forms.ValidationError('Please Enter Appropriate Name')
        return father_name

    def clean_mother_name(self):
        mother_name = self.cleaned_data.get('mother_name')
        name = mother_name.split(' ')
        try:
            if(not (name[0].isalpha() & name[1].isalpha())):
                raise forms.ValidationError('Mother Name Should not contain integers')
        except:
            raise forms.ValidationError('Please Enter Appropriate Name')
        return mother_name

    def clean_father_phone(self):
        father_phone = self.cleaned_data.get('father_phone')
        if father_phone != None:
            c = 0
            p = father_phone
            while(p != 0):
                p = p // 10
                c = c + 1
            if(c != 10):
                raise forms.ValidationError("Enter valid phone number")
        return father_phone

    def clean_mother_phone(self):
        mother_phone = self.cleaned_data.get('mother_phone')
        if mother_phone != None:
            c = 0
            p = mother_phone
            while(p != 0):
                p = p // 10
                c = c + 1
            if(c != 10):
                raise forms.ValidationError("Enter valid phone number")
        return mother_phone

class Employee_Data_Update(forms.ModelForm):
    fname           = forms.CharField(label="First Name",max_length=20,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    mname           = forms.CharField(label="Middle Name",max_length=20,required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    lname           = forms.CharField(label="Last Name",max_length=20,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    picture         = forms.ImageField(label='Employee Pic',required=False,widget = forms.FileInput(attrs={"onchange":"readURL(this);"}))
    phone           = forms.IntegerField(label="Contact Number",widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    father_name     = forms.CharField(label="Father Name",max_length=50,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    father_phone    = forms.IntegerField(label="Father's Contact Number",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    mother_name     = forms.CharField(label="Mother Name",max_length=50,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    mother_phone    = forms.IntegerField(label="Mother's Contact Number",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    work            = forms.CharField(label="Work",max_length=30,required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    dob             = forms.DateField(label="DOB",widget=forms.DateInput(attrs={'type':'date'}))
    salary          = forms.IntegerField(label="Salary",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    state           = forms.CharField(label="State",max_length=30,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    city            = forms.CharField(label="City",max_length=30,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    address         = forms.CharField(label="Address",max_length=200,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    pincode         = forms.IntegerField(label="Pincode",widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    
    class Meta:
        model = School_Employee_Data
        fields = [
            'fname',       
            'mname',       
            'lname',       
            'picture',
            'phone',       
            'father_name', 
            'father_phone',
            'mother_name', 
            'mother_phone',
            'work',        
            'dob',         
            'salary',      
            'state',       
            'city',           
            'address',     
            'pincode',
        ]

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

    def clean_father_name(self):
        father_name = self.cleaned_data.get('father_name')
        name = father_name.split(' ')
        try:
            if(not (name[0].isalpha() & name[1].isalpha())):
                raise forms.ValidationError('Name Should not contain integers')
        except:
            raise forms.ValidationError('Please Enter Appropriate Name')
        return father_name

    def clean_mother_name(self):
        mother_name = self.cleaned_data.get('mother_name')
        name = mother_name.split(' ')
        try:
            if(not (name[0].isalpha() & name[1].isalpha())):
                raise forms.ValidationError('Mother Name Should not contain integers')
        except:
            raise forms.ValidationError('Please Enter Appropriate Name')
        return mother_name

    def clean_father_phone(self):
        father_phone = self.cleaned_data.get('father_phone')
        if father_phone != None:
            c = 0
            p = father_phone
            while(p != 0):
                p = p // 10
                c = c + 1
            if(c != 10):
                raise forms.ValidationError("Enter valid phone number")
        return father_phone

    def clean_mother_phone(self):
        mother_phone = self.cleaned_data.get('mother_phone')
        if mother_phone != None:
            c = 0
            p = mother_phone
            while(p != 0):
                p = (p//10)
                c = c + 1
            if(c != 10):
                raise forms.ValidationError("Enter valid phone number")
        return mother_phone

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

class Update_Student_Fee(forms.ModelForm):
    fee             = forms.IntegerField(label="Fee of Student",widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    fee_submitted   = forms.IntegerField(label="Fee Submitted by Student",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))

    class Meta:
        model = School_Student_Data
        fields = [
            'fee',
            'fee_submitted',
        ]

    def clean_fee_submitted(self):
        fee = self.cleaned_data.get('fee')
        fee_submitted = self.cleaned_data.get('fee_submitted')
        if fee < fee_submitted:
            raise forms.ValidationError("fee submitted should not be more than actual fee")
        return fee_submitted

class Student_Leave_Update(forms.ModelForm):
    to_date       = forms.DateField(label="Leaving Date",widget=forms.DateInput(attrs={'type':'date','readonly':'True'}))

    class Meta:
        model = School_Student_Data
        fields = [
            'to_date',
        ]

class Faculty_Leave_Update(forms.ModelForm):
    to_date       = forms.DateField(label="Leaving Date",widget=forms.DateInput(attrs={'type':'date','readonly':'True'}))

    class Meta:
        model = School_Faculty_Data
        fields = [
            'to_date',
        ]

class Employee_Leave_Update(forms.ModelForm):
    to_date       = forms.DateField(label="Leaving Date",widget=forms.DateInput(attrs={'type':'date','readonly':'True'}))

    class Meta:
        model = School_Employee_Data
        fields = [
            'to_date',
        ]

class Examination_Leave_Update(forms.ModelForm):
    to_date       = forms.DateField(label="Leaving Date",widget=forms.DateInput(attrs={'type':'date','readonly':'True'}))

    class Meta:
        model = School_Examination_Data
        fields = [
            'to_date',
        ]

class School_Examiner_Insert(forms.ModelForm):
    username        = forms.CharField(label="Username",max_length=20,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    password        = forms.CharField(label="Password",max_length=20,widget=forms.PasswordInput(attrs={'class':"au-input au-input--full"}))
    cpassword       = forms.CharField(label="Confirm Password",max_length=20,widget=forms.PasswordInput(attrs={'class':"au-input au-input--full"}))
    examiner_no     = forms.IntegerField(label="Examiner Number",widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'id generate acoording to number'}))
    fname           = forms.CharField(label="First Name",max_length=20,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    mname           = forms.CharField(label="Middle Name",max_length=20,required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    lname           = forms.CharField(label="Last Name",max_length=20,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    picture         = forms.ImageField(label='Examiner Pic',required=False,widget = forms.FileInput(attrs={"onchange":"readURL(this);"}))
    emailid         = forms.EmailField(label="Email ID",max_length=100,widget=forms.EmailInput(attrs={'class':"au-input au-input--full"}))
    phone           = forms.IntegerField(label="Contact Number",widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    father_name     = forms.CharField(label="Father Name",max_length=50,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    father_phone    = forms.IntegerField(label="Father's Contact Number",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    mother_name     = forms.CharField(label="Mother Name",max_length=50,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    mother_phone    = forms.IntegerField(label="Mother's Contact Number",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    state           = forms.CharField(label="State",max_length=30,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    city            = forms.CharField(label="City",max_length=30,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    address         = forms.CharField(label="Address",max_length=200,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    pincode         = forms.IntegerField(label="Pincode",widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    dob             = forms.DateField(label="DOB",widget=forms.DateInput(attrs={'type':'date'}))
    salary          = forms.IntegerField(label="Salary",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    from_date       = forms.DateField(label="Joining Dates",required=False,widget=forms.DateInput(attrs={'type':'date','readonly':'True'}))

    class Meta:
        model = School_Examination_Data
        fields = [
            'username',
            'password',
            'cpassword',
            'examiner_no',
            'fname',
            'mname',
            'lname',
            'picture',
            'phone',
            'emailid',
            'father_name',
            'father_phone',
            'mother_name',
            'mother_phone',
            'dob',
            'salary',
            'state',
            'city',
            'address',
            'pincode',
            'from_date',   
        ]

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if(len(username) <= 2):
            raise forms.ValidationError('Please a enter username contain more than 3 characters.')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if(len(password) < 6 or len(password) > 12):
            raise forms.ValidationError('Please a enter password of 6 to 14 character.')
        return password

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

    def clean_cpassword(self):
        password = self.cleaned_data.get('password')
        cpassword = self.cleaned_data.get('cpassword')
        if password != cpassword:
            raise forms.ValidationError("Password and Confirm Password is not same")
        return cpassword
    
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

    def clean_father_name(self):
        father_name = self.cleaned_data.get('father_name')
        name = father_name.split(' ')
        try:
            if(not (name[0].isalpha() & name[1].isalpha())):
                raise forms.ValidationError('Name Should not contain integers')
        except:
            raise forms.ValidationError('Please Enter Appropriate Name')
        return father_name

    def clean_mother_name(self):
        mother_name = self.cleaned_data.get('mother_name')
        name = mother_name.split(' ')
        try:
            if(not (name[0].isalpha() & name[1].isalpha())):
                raise forms.ValidationError('Mother Name Should not contain integers')
        except:
            raise forms.ValidationError('Please Enter Appropriate Name')
        return mother_name

    def clean_father_phone(self):
        father_phone = self.cleaned_data.get('father_phone')
        if father_phone != None:
            c = 0
            p = father_phone
            while(p != 0):
                p = p // 10
                c = c + 1
            if(c != 10):
                raise forms.ValidationError("Enter valid phone number")
        return father_phone

    def clean_mother_phone(self):
        mother_phone = self.cleaned_data.get('mother_phone')
        if mother_phone != None:
            c = 0
            p = mother_phone
            while(p != 0):
                p = p // 10
                c = c + 1
            if(c != 10):
                raise forms.ValidationError("Enter valid phone number")
        return mother_phone

class School_Total_Attendance_Detail(forms.ModelForm):
    student_id      = forms.CharField(label="Student ID",max_length=50,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    clas            = forms.ChoiceField(label="Class",choices=CLASS_CHOICE,widget=forms.Select(attrs={'class':"au-input au-input--full"}))
    student_attend  = forms.IntegerField(label="Student Attendance",widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    total_working   = forms.IntegerField(label="Total Working Days in Session",widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))

    class Meta:
        model = School_Total_Attendance
        fields = [
            'student_id',
            'clas',
            'student_attend',
            'total_working',
        ]

    def clean_total_working(self):
        attend = self.cleaned_data.get('student_attend')
        total = self.cleaned_data.get('total_working')
        if(attend > total):
            raise forms.ValidationError("Attendance can't be greater than Total Working Days.")
        if(total > 366):
            raise forms.ValidationError("Total Working Days are not greater than days in a year.")
        return total

class Examiner_Data_Update(forms.ModelForm):
    fname           = forms.CharField(label="First Name",max_length=20,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    mname           = forms.CharField(label="Middle Name",max_length=20,required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    lname           = forms.CharField(label="Last Name",max_length=20,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    picture         = forms.ImageField(label='Examiner Pic',required=False,widget = forms.FileInput(attrs={"onchange":"readURL(this);"}))
    emailid         = forms.EmailField(label="Email ID",max_length=100,widget=forms.EmailInput(attrs={'class':"au-input au-input--full"}))
    phone           = forms.IntegerField(label="Contact Number",widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    father_name     = forms.CharField(label="Father Name",max_length=50,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    father_phone    = forms.IntegerField(label="Father's Contact Number",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    mother_name     = forms.CharField(label="Mother Name",max_length=50,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    mother_phone    = forms.IntegerField(label="Mother's Contact Name",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    state           = forms.CharField(label="State",max_length=30,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    city            = forms.CharField(label="City",max_length=30,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    address         = forms.CharField(label="Address",max_length=200,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    pincode         = forms.IntegerField(label="Pincode",widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    dob             = forms.DateField(label="DOB",widget=forms.DateInput(attrs={'type':'date'}))
    salary          = forms.IntegerField(label="Salary",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))

    class Meta:
        model = School_Examination_Data
        fields = [
            'fname',
            'mname',
            'lname',
            'picture',
            'phone',
            'emailid',
            'father_name',
            'father_phone',
            'mother_name',
            'mother_phone',
            'dob',
            'salary',
            'state',
            'city',
            'address',
            'pincode',
        ]

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

    def clean_father_name(self):
        father_name = self.cleaned_data.get('father_name')
        name = father_name.split(' ')
        try:
            if(not (name[0].isalpha() & name[1].isalpha())):
                raise forms.ValidationError('Name Should not contain integers')
        except:
            raise forms.ValidationError('Please Enter Appropriate Name')
        return father_name

    def clean_mother_name(self):
        mother_name = self.cleaned_data.get('mother_name')
        name = mother_name.split(' ')
        try:
            if(not (name[0].isalpha() & name[1].isalpha())):
                raise forms.ValidationError('Mother Name Should not contain integers')
        except:
            raise forms.ValidationError('Please Enter Appropriate Name')
        return mother_name

    def clean_father_phone(self):
        father_phone = self.cleaned_data.get('father_phone')
        if father_phone != None:
            c = 0
            p = father_phone
            while(p != 0):
                p = p // 10
                c = c + 1
            if(c != 10):
                raise forms.ValidationError("Enter valid phone number")
        return father_phone

    def clean_mother_phone(self):
        mother_phone = self.cleaned_data.get('mother_phone')
        if mother_phone != None:
            c = 0
            p = mother_phone
            while(p != 0):
                p = p // 10
                c = c + 1
            if(c != 10):
                raise forms.ValidationError("Enter valid phone number")
        return mother_phone

class Student_Marks(forms.Form):
    student_id      = forms.CharField(label="Student ID",max_length=50,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    clas            = forms.ChoiceField(label="Class",choices=CLASS_CHOICE,widget=forms.Select(attrs={'class':"au-input au-input--full"}))

    class Meta:
        fields = [
            'student_id',
            'clas',
        ]

class Change_School_Password(forms.ModelForm):
    password        = forms.CharField(label="Password",max_length=20,required=True,widget=forms.PasswordInput(attrs={'class':"au-input au-input--full"}))
    cpassword       = forms.CharField(label="Confirm Password",max_length=20,required=True,widget=forms.PasswordInput(attrs={'class':"au-input au-input--full"}))

    class Meta:
        model = School_Management
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

class Update_School_Detail(forms.ModelForm):
    emailid         = forms.EmailField(label="Email ID",max_length=100,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    phone           = forms.IntegerField(label="Contact Number",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    organisation    = forms.CharField(label="Organisation Name",max_length=50,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':'True'}))
    state           = forms.CharField(label="State",max_length=30,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':'True'}))
    city            = forms.CharField(label="City",max_length=30,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':'True'}))
    pincode         = forms.CharField(label="Pincode",max_length=6,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':'True'}))
    address         = forms.CharField(label="Address",max_length=200,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))

    class Meta:
        model = School_Management
        fields = [
             'emailid',   
             'phone',   
             'organisation',
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