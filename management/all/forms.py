from django import forms
from .models import User_Data

school      = 'school'
library     = 'library'
hotel       = 'hotel'
restaurant  = 'rest'
MANA_CHOICE = (
    (school,'School'),
    (library,'Library'),
    (hotel,'Hotel'),
    (restaurant,'Restaurant')
)

class User_Login(forms.Form):
    username = forms.CharField(label="Username",max_length=20,required=True,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Username'}))
    password = forms.CharField(label="Password",max_length=20,widget=forms.PasswordInput(attrs={'class':"au-input au-input--full",'placeholder':'Password'}))

    class Meta:
        fields = [
            'username',
            'password',
        ]

class User_register(forms.ModelForm):
    username        = forms.CharField(label="Username",max_length=20,widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Username'}))
    password        = forms.CharField(label="Password",max_length=20,widget=forms.PasswordInput(attrs={'class':"au-input au-input--full",'placeholder':'Password'}))
    cpassword       = forms.CharField(label="Confirm Password",max_length=20,widget=forms.PasswordInput(attrs={'class':"au-input au-input--full",'placeholder':'Confirm Password'}))
    emailid         = forms.EmailField(label="Email ID",max_length=100,widget=forms.EmailInput(attrs={'class':"au-input au-input--full",'placeholder':'Email ID'}))
    phone           = forms.IntegerField(label="Contact Number",widget=forms.TextInput(attrs={'class':"au-input au-input--full",'placeholder':'Contact Number'}))
    management      = forms.ChoiceField(label='Management',choices=MANA_CHOICE,required=True,widget=forms.Select())
    organization    = forms.CharField(label='Organization Name',max_length=100,widget=forms.TextInput())
    state           = forms.CharField(label='State',max_length=30,widget=forms.TextInput())
    city            = forms.CharField(label='City',max_length=30,widget=forms.TextInput())
    pincode         = forms.CharField(label='Pincode',max_length=10,widget=forms.TextInput())
    address         = forms.CharField(label='Address',max_length=200,widget=forms.TextInput())
    
    class Meta:
        model = User_Data
        fields = [
            'username',
            'password',
            'cpassword',
            'emailid',
            'phone',
            'management',
            'organization',
            'state',
            'city',
            'pincode',
            'address',
        ]

class Change_Password(forms.ModelForm):
    password        = forms.CharField(label="Password",max_length=20,required=True,widget=forms.PasswordInput(attrs={'class':"au-input au-input--full"}))
    cpassword       = forms.CharField(label="Confirm Password",max_length=20,required=True,widget=forms.PasswordInput(attrs={'class':"au-input au-input--full"}))

    class Meta:
        model = User_Data
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