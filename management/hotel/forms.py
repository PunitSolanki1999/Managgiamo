from django import forms

from .models import Hotel_Management, Hotel_Employee_Register, Hotel_Room_Register, Customer_Register, Bill

class Hotel_Management_Data(forms.ModelForm):
    registration_no = forms.CharField(label="Registration Number",max_length=20,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Registration Number'}))
    emailid         = forms.EmailField(label="Email ID",max_length=100,required=True,widget=forms.EmailInput(attrs={'class':"au-input au-input--full",'placeholder':'Email ID'}))
    phone           = forms.IntegerField(label="Contact Number",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Contact Number'}))
    hotel_name      = forms.CharField(label="Hotel Name",max_length=50,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Hotel Name'}))
    state           = forms.CharField(label="State",max_length=30,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'State'}))
    city            = forms.CharField(label="City",max_length=30,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'City'}))
    pincode         = forms.IntegerField(label="Pincode",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Pincode'}))
    address         = forms.CharField(label="Address",max_length=200,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Address'}))

    class Meta:
        model = Hotel_Management
        fields = [
            'registration_no',
            'emailid',
            'phone',
            'hotel_name',
            'state',
            'city',
            'pincode',
            'address',
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

    def clean_cpassword(self):
        password = self.cleaned_data.get('password')
        cpassword = self.cleaned_data.get('cpassword')
        if password != cpassword:
            raise forms.ValidationError("Password and Confirm Password is not same")
        return cpassword
    
    def clean_hotel_name(self):
        hotel_name = self.cleaned_data.get('hotel_name')
        if(len(hotel_name) <= 2 or len(hotel_name) >= 30):
            raise forms.ValidationError('Please a enter a approriate Hotel Name')
        hotel = hotel_name.split(' ')
        if(len(hotel) != 1):
            try:
                if(not (hotel[0].isalpha() & hotel[1].isalpha())):
                    raise forms.ValidationError('Name Should not contain integers')
            except:
                raise forms.ValidationError('Please Enter Appropriate Name')
        else:
            if(not (hotel[0].isalpha())):
                raise forms.ValidationError('Name Should not contain integers')
        return hotel_name

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


class Hotel_Room_Register_Data(forms.ModelForm):
    room_no     = forms.CharField(label="Room No.",max_length=50,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Room Number'}))
    room_type   = forms.CharField(label="Room Type",max_length=100,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Room Type'}))
    room_cost   = forms.IntegerField(label="Room Cost",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Room Cost'}))
    ac          = forms.BooleanField(label="AC or Non-AC",required=False)
    available   = forms.BooleanField(label="Available",required=False,initial=True)

    class Meta:
        model = Hotel_Room_Register
        fields = [
            'room_no',
            'room_type',
            'room_cost',
            'ac',
            'available',
        ]

class Hotel_Employee_Register_Data(forms.ModelForm):
    fname           = forms.CharField(label="First Name",max_length=20,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'First Name'}))
    mname           = forms.CharField(label="Middle Name",max_length=20,required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Middle Name'}))
    lname           = forms.CharField(label="Last Name",max_length=20,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Last Name'}))
    picture         = forms.ImageField(label='Emloyee Pic',required=False,widget = forms.FileInput(attrs={"onchange":"readURL(this);"}))
    designation     = forms.CharField(label="Designation",max_length=50,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Designation'}))
    salary          = forms.IntegerField(label="Salary",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Salary'}))
    dob             = forms.DateField(label="DOB",widget=forms.DateInput(attrs={'type':'date'}))
    phone           = forms.IntegerField(label="Contact No.",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Contact Number'}))
    emailid         = forms.EmailField(label="Email ID",required=True,widget=forms.EmailInput(attrs={'class':"au-input au-input--full",'placeholder':'Email ID'}))
    address         = forms.CharField(label="Address",max_length=200,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Address'}))
    state           = forms.CharField(label="State",max_length=50,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'State'}))
    city            = forms.CharField(label="City",max_length=50,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'City'}))
    pincode         = forms.IntegerField(label="Pincode",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Pincode'}))
    father_name     = forms.CharField(label="Father Name",max_length=60,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Father Name'}))
    father_phone    = forms.IntegerField(label="Father's Contact No.",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':"Father's Contact Number"}))
    mother_name     = forms.CharField(label="Mother Name",max_length=60,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Mother Name'}))
    mother_phone    = forms.IntegerField(label="Mother's Contact No.",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':"Mother Contact Number"}))
    from_date       = forms.DateField(label="Joining Date",required=False,widget=forms.DateInput(attrs={'class':"au-input au-input--full",'type':'date','readonly':'True'}))

    class Meta:
        model = Hotel_Employee_Register
        fields = [
            'fname',
            'mname',
            'lname',
            'picture',
            'designation',
            'salary',
            'phone',
            'dob',
            'emailid',
            'address',
            'state',
            'city',
            'pincode',
            'father_name',
            'father_phone',
            'mother_name',
            'mother_phone',
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

class Customer_Register_Data(forms.ModelForm):
    addar_no        = forms.CharField(label="Addhar Number",max_length=16,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':"Addhar Number"}))
    room_id         = forms.CharField(label="Room ID",max_length=50,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':'True'}))
    fname           = forms.CharField(label="First Name",max_length=20,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':"First Name"}))
    mname           = forms.CharField(label="Middle Name",max_length=20,required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':"Middle Name"}))
    lname           = forms.CharField(label="Last Name",max_length=20,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':"Last Name"}))
    no_of_days      = forms.CharField(label="No. of Days To Stay",max_length=10,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full","onchange":"multiply();",'id':"days",'placeholder':"Days To Stay"}))
    cost            = forms.IntegerField(label="Cost",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full","id":"total",'readonly':"True",'placeholder':"Cost"}))
    phone           = forms.IntegerField(label="Contact Number",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':"Contact Number"}))
    address         = forms.CharField(label="Address",max_length=200,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':"Address"}))
    amount_paid     = forms.IntegerField(label="Amount Paid",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':"Advance Amount Paid"}))
    checkin_date    = forms.DateField(label="Check-In Date",required=False,widget=forms.DateInput(attrs={'type':'date','readonly':'True'}))

    class Meta:
        model = Customer_Register
        fields = [
            'addar_no',
            'room_id',
            'fname',
            'mname',
            'lname',
            'no_of_days',
            'cost',
            'phone',
            'address',
            'amount_paid',
            'checkin_date',
        ]

    def clean_addar_no(self):
        addar_no = self.cleaned_data.get('addar_no')
        c = 0
        p = int(addar_no)
        while(p != 0):
            p = p // 10
            c = c + 1
        if(c != 14):
            raise forms.ValidationError("Enter valid Addhar number")
        return addar_no

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

    def clean_amount_paid(self):
        cost = self.cleaned_data.get('cost')
        amount_paid = self.cleaned_data.get('amount_paid')
        if(amount_paid > cost):
            raise forms.ValidationError('Paid Amount should not be more than Total Cost.')
        return amount_paid
    
    def clean_no_of_days(self):
        day = self.cleaned_data.get('no_of_days')
        if(int(day) > 366):
            return forms.ValidationError("Book Issue Days Can't be greater than the days in a year.")
        return day
        
class Bill_Data(forms.ModelForm):
    bill_no     = forms.CharField(label="Bill Number",max_length=50,required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    room_id     = forms.CharField(label="Room ID",max_length=50,required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    customer_id = forms.CharField(label="Customer ID",max_length=100,required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    cost        = forms.IntegerField(label="Cost",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    type_of_work= forms.CharField(label="Extra Service Given",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    extra       = forms.IntegerField(label="Extra Cost",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    no_of_days  = forms.IntegerField(label="No. of Days Stayed",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))

    class Meta:
        model = Bill
        fields = [
            'bill_no',
            'room_id',
            'customer_id',
            'cost',
            'extra',
            'no_of_days',
            'type_of_work',
        ]

class Update_Hotel_Room(forms.ModelForm):
    room_type   = forms.CharField(label="Room Type",max_length=100,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':"Room Type"}))
    room_cost   = forms.IntegerField(label="Room Cost",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':"Room Cost"}))
    ac          = forms.BooleanField(label="AC or Non-AC",required=False)
    available   = forms.BooleanField(label="Available",required=False)

    class Meta:
        model = Hotel_Room_Register
        fields = [
            'room_type',
            'room_cost',
            'ac',
            'available',
        ]

class Update_Employee(forms.ModelForm):
    fname           = forms.CharField(label="First Name",max_length=20,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    mname           = forms.CharField(label="Middle Name",max_length=20,required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    lname           = forms.CharField(label="Last Name",max_length=20,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    picture         = forms.ImageField(label='Employee Pic',required=False,widget = forms.FileInput(attrs={"onchange":"readURL(this);"}))
    designation     = forms.CharField(label="Designation",max_length=50,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    salary          = forms.IntegerField(label="Salary",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    dob             = forms.DateField(label="DOB",widget=forms.DateInput(attrs={'type':'date'}))
    phone           = forms.IntegerField(label="Contact No.",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    emailid         = forms.EmailField(label="Email Address",required=True,widget=forms.EmailInput(attrs={'class':"au-input au-input--full"}))
    address         = forms.CharField(label="Address",max_length=200,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    state           = forms.CharField(label="State",max_length=50,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    city            = forms.CharField(label="City",max_length=50,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    pincode         = forms.IntegerField(label="Pincode",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    father_name     = forms.CharField(label="Father Name",max_length=60,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    father_phone    = forms.IntegerField(label="Father's Contact Number",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    mother_name     = forms.CharField(label="Mother Name",max_length=60,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    mother_phone    = forms.IntegerField(label="Mother's Contact Number",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))

    class Meta:
        model = Hotel_Employee_Register
        fields = [
            'fname',
            'mname',
            'lname',
            'picture',
            'designation',
            'dob',
            'salary',
            'phone',
            'emailid',
            'address',
            'state',
            'city',
            'pincode',
            'father_name',
            'father_phone',
            'mother_name',
            'mother_phone',
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


class Employee_Leave(forms.ModelForm):
    to_date       = forms.DateField(label="Leaving Date",required=False,widget=forms.DateInput(attrs={'type':'date','readonly':'True'}))

    class Meta:
        model = Hotel_Employee_Register
        fields = [
            'to_date',
        ]

class Update_Customer_Day(forms.ModelForm):
    addar_no        = forms.CharField(label="Addhar Number",max_length=16,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':"True"}))
    room_id         = forms.CharField(label="Room ID",max_length=50,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':'True'}))
    fname           = forms.CharField(label="First Name",max_length=20,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':"True"}))
    mname           = forms.CharField(label="Middle Name",max_length=20,required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':"True"}))
    lname           = forms.CharField(label="Last Name",max_length=20,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':"True"}))
    no_of_days      = forms.CharField(label="No. of Days to Stay",max_length=10,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full","onchange":"multiply();",'id':"days"}))
    cost            = forms.IntegerField(label="Cost",required=False,widget=forms.TextInput(attrs={'class':"au-input au-input--full","id":"total",'readonly':"True"}))
    phone           = forms.IntegerField(label="Contact Number",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':"True"}))
    address         = forms.CharField(label="Address",max_length=200,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':"True"}))
    amount_paid     = forms.IntegerField(label="Advance Amount Paid",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':"True"}))
    checkin_date    = forms.DateField(label="Check-In Date",required=False,widget=forms.DateInput(attrs={'type':'date','readonly':'True'}))

    class Meta:
        model = Customer_Register
        fields = [
            'addar_no',
            'room_id',
            'fname',
            'mname',
            'lname',
            'no_of_days',
            'cost',
            'phone',
            'address',
            'amount_paid',
            'checkin_date',
        ]

    def clean_no_of_days(self):
        day = self.cleaned_data.get('no_of_days')
        if(day > 366):
            return forms.ValidationError("Book Issue Days Can't be greater than the days in a year.")
        return day

class Customer_Checkout(forms.ModelForm):
    checkout_date       = forms.DateField(label="Check-Out Date",required=False,widget=forms.DateInput(attrs={'type':'date','readonly':'True'}))

    class Meta:
        model = Customer_Register
        fields = [
            'checkout_date',
        ]

class Update_Hotel_Detail(forms.ModelForm):
    emailid         = forms.EmailField(label="Email ID",max_length=100,required=True,widget=forms.EmailInput(attrs={'class':"au-input au-input--full"}))
    phone           = forms.IntegerField(label="Contact Number",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full"}))
    hotel_name      = forms.CharField(label="Hotel Name",max_length=50,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':'True'}))
    state           = forms.CharField(label="State",max_length=30,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':'True'}))
    city            = forms.CharField(label="City",max_length=30,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':'True'}))
    pincode         = forms.IntegerField(label="Pincode",required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'readonly':'True'}))
    address         = forms.CharField(label="Address",max_length=200,required=True)

    class Meta:
        model = Hotel_Management
        fields = [
            'emailid',
            'phone',
            'hotel_name',
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

class Change_Hotel_Password(forms.ModelForm):
    password        = forms.CharField(label="Password",max_length=20,required=True,widget=forms.PasswordInput(attrs={'class':"au-input au-input--full",'placeholder':'Password'}))
    cpassword       = forms.CharField(label="Confirm Password",max_length=20,required=True,widget=forms.PasswordInput(attrs={'class':"au-input au-input--full",'placeholder':'Confirm Password'}))

    class Meta:
        model = Hotel_Management
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