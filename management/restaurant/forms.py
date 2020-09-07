from django import forms
from .models import Rest_Management, Rest_Food, Rest_Employee, Ingredient_Table, Bill, Bill_Product

class Rest_Management_Detail(forms.ModelForm):
    emailid         = forms.EmailField(label="Email ID",max_length=100,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Email ID'}))
    phone           = forms.IntegerField(label="Contact Number",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Contact Number'}))
    rest_name       = forms.CharField(label="Restaurent Name",max_length=50,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Restaurent Name'}))
    license_no      = forms.CharField(label="Lincense Number",max_length=20,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Lisence Number'}))
    state           = forms.CharField(label="State",max_length=30,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'State'}))
    city            = forms.CharField(label="City",max_length=30,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'City'}))
    pincode         = forms.CharField(label="Pincode",max_length=6,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Pincode'}))
    address         = forms.CharField(label="Address",max_length=200,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Address'}))

    class Meta:
        model = Rest_Management
        fields = [ 
             'emailid',   
             'phone',   
             'rest_name',
             'license_no',   
             'state',   
             'city',   
             'pincode',   
             'address',   
        ]
    
    def clean_rest_name(self):
        rest_name = self.cleaned_data.get('rest_name')
        if(len(rest_name) <= 2 or len(rest_name) >= 30):
            raise forms.ValidationError('Please a enter a approriate Restuarent Name')
        rest = rest_name.split(' ')
        if(len(rest) != 1):
            try:
                if(not (rest[0].isalpha() & rest[1].isalpha())):
                    raise forms.ValidationError('Name Should not contain integers')
            except:
                raise forms.ValidationError('Please Enter Appropriate Name')
        else:
            if(not (rest[0].isalpha())):
                raise forms.ValidationError('Name Should not contain integers')
        return rest_name


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
        p = int(pincode)
        while(p != 0):
            p = p // 10
            c = c + 1
        if(c != 6):
            raise forms.ValidationError("Enter valid pincode")
        return pincode

class Rest_Employee_Detail(forms.ModelForm):
    fname           = forms.CharField(label="First Name",max_length=20,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'First Name'}))
    mname           = forms.CharField(label="Middle Name",max_length=20,required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Middle Name'}))
    lname           = forms.CharField(label="Last Name",max_length=20,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Last Name'}))
    picture         = forms.ImageField(label='Employee Pic',required=False,widget = forms.FileInput(attrs={"onchange":"readURL(this);"}))
    phone           = forms.IntegerField(label="Contact Number",widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Contact Number'}))
    father_name     = forms.CharField(label="Father Name",max_length=50,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Father Name'}))
    father_phone    = forms.IntegerField(label="Father's Contact Number",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':"Father's Contact Number"}))
    work            = forms.CharField(label="Designation",max_length=30,required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Designation'}))
    dob             = forms.DateField(label="DOB",widget=forms.DateInput(attrs={'type':'date'}))
    salary          = forms.IntegerField(label="Salary",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Salary'}))
    state           = forms.CharField(label="State",max_length=30,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'State'}))
    city            = forms.CharField(label="City",max_length=30,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'City'}))
    address         = forms.CharField(label="Address",max_length=200,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Address'}))
    pincode         = forms.IntegerField(label="Pincode",widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Address'}))
    from_date       = forms.DateField(label="Joining Date",required=False,widget=forms.DateInput(attrs={'type':'date','readonly':'True'}))

    class Meta:
        model = Rest_Employee
        fields = [
            'fname',       
            'mname',       
            'lname',       
            'picture',
            'phone',       
            'father_name', 
            'father_phone',
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

class Rest_Food_Detail(forms.ModelForm):
    food_name        = forms.CharField(label="Food Name",max_length=20,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Food Name'}))
    price            = forms.CharField(label="Price",max_length=20,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Price'}))
    
    class Meta:
        model = Rest_Food
        fields = [
             'food_name',       
             'price',     
        ]

    def clean_food_name(self):
        food_name = self.cleaned_data.get('food_name')
        if(len(food_name) <= 2 or len(food_name) >= 15):
            raise forms.ValidationError('Please a enter a approriate Food Name')
        if(not food_name.isalpha()):
            raise forms.ValidationError('Please a enter a approriate Food Name')
        return food_name

class Ingredient_Detail(forms.ModelForm):
    ingredient_name = forms.CharField(label="Ingredient Name",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Ingredient Name'}))
    total           = forms.IntegerField(label="Total Quantity Needed",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Total Quantity'}))
    available       = forms.IntegerField(label="Quantity Available",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Quantity Available'}))

    class Meta:
        model = Ingredient_Table
        fields = [
            'ingredient_name',
            'total',
            'available',
        ]

    def clean_availale(self):
        available = self.cleaned_data.get('available')
        total = self.cleaned_data.get('total')
        if(total < available):
            raise forms.ValidationError("Available Quantity should not be greater than Total Quantity.")
        return available

class Bill_Detail(forms.ModelForm):
    table_no        = forms.CharField(label="Table No.",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Table Number'}))

    class Meta:
        model = Bill
        fields = [
            'table_no',
        ]

class Bill_Product_Detail(forms.ModelForm):
    food_id         = forms.CharField(label="Food ID",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    quantity        = forms.IntegerField(label="Quantity Taken",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))

    class Meta:
        model = Bill_Product
        fields = [
            'food_id',
            'quantity',
        ]


class Update_Employee(forms.ModelForm):
    fname           = forms.CharField(label="First Name",max_length=20,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    mname           = forms.CharField(label="Middle Name",max_length=20,required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    lname           = forms.CharField(label="Last Name",max_length=20,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    picture         = forms.ImageField(label='Employee Pic',required=False,widget = forms.FileInput(attrs={"onchange":"readURL(this);"}))
    work            = forms.CharField(label="Work",max_length=50,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    salary          = forms.IntegerField(label="Salary",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    dob             = forms.DateField(label="DOB",widget=forms.DateInput(attrs={'type':'date'}))
    phone           = forms.IntegerField(label="Contact Number",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    address         = forms.CharField(label="Address",max_length=200,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    state           = forms.CharField(label="State",max_length=50,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    city            = forms.CharField(label="City",max_length=50,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    pincode         = forms.IntegerField(label="Pincode",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    father_name     = forms.CharField(label="Father Name",max_length=60,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    father_phone    = forms.IntegerField(label="Father's Contact Number",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))

    class Meta:
        model = Rest_Employee
        fields = [
            'fname',
            'mname',
            'lname',
            'picture',
            'work',
            'dob',
            'salary',
            'phone',
            'address',
            'state',
            'city',
            'pincode',
            'father_name',
            'father_phone',
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

class Employee_Leave(forms.ModelForm):
    to_date       = forms.DateField(label="Leaving Date",required=False,widget=forms.DateInput(attrs={'class':"au-input au-input--full",'type':'date','readonly':'True'}))

    class Meta:
        model = Rest_Employee
        fields = [
            'to_date',
        ]

class Update_Ingredient_Detail(forms.ModelForm):
    ingredient_name = forms.CharField(label="Ingredient Name",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':'True'}))
    total           = forms.IntegerField(label="Total Quantity Needed",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    available       = forms.IntegerField(label="Quantity Available",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))

    class Meta:
        model = Ingredient_Table
        fields = [
            'ingredient_name',
            'total',
            'available',
        ]
    
    def clean_availale(self):
        available = self.cleaned_data.get('available')
        total = self.cleaned_data.get('total')
        if(total < available):
            raise forms.ValidationError("Available Quantity should not be greater than Total Quantity.")
        return available

class Change_Rest_Password(forms.ModelForm):
    password        = forms.CharField(label="Password",max_length=20,required=True,widget=forms.PasswordInput(attrs={'class':"au-input au-input--full"}))
    cpassword       = forms.CharField(label="Confirm Password",max_length=20,required=True,widget=forms.PasswordInput(attrs={'class':"au-input au-input--full"}))

    class Meta:
        model = Rest_Management
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

class Update_Rest_Detail(forms.ModelForm):
    
    emailid         = forms.EmailField(label="Email ID",max_length=100,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    phone           = forms.IntegerField(label="Contact Number",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    rest_name       = forms.CharField(label="Restaurent Name",max_length=50,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':'True'}))
    state           = forms.CharField(label="State",max_length=30,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':'True'}))
    city            = forms.CharField(label="City",max_length=30,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':'True'}))
    pincode         = forms.CharField(label="Pincode",max_length=6,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':'True'}))
    address         = forms.CharField(label="Address",max_length=200,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))

    class Meta:
        model = Rest_Management
        fields = [
             'emailid',   
             'phone',   
             'rest_name',
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