from django.db import models
# Create your models here.

class Hotel_Management(models.Model):
    mainkey        = models.CharField(max_length=100,default=None,null=False)
    superkey        = models.CharField(max_length=100,default=None,unique=True,null=False)
    registration_no = models.CharField(max_length=20,primary_key=True,default=None,null=False)
    username        = models.CharField(max_length=20,default=None,unique=True,null=False)
    password        = models.CharField(max_length=20,default=None,null=False)
    emailid         = models.EmailField(max_length=100,default=None,null=False)
    phone           = models.CharField(max_length=10,default=None,null=False)
    hotel_name      = models.CharField(max_length=50,default=None,null=False)
    state           = models.CharField(max_length=30,default=None,null=False)
    city            = models.CharField(max_length=30,default=None,null=False)
    pincode         = models.CharField(max_length=6,default=None,null=False)
    address         = models.CharField(max_length=200,default=None,null=False)

    class Meta:
        verbose_name = 'Hotel\'s Detail'
    
    def __str__(self):
        return self.username

class Hotel_Room_Register(models.Model):
    superkey        = models.CharField(max_length=100,default=None,null=False)
    room_id         = models.CharField(max_length=50,primary_key=True,default=None,null=False)
    room_no         = models.CharField(max_length=20,default=None,null=False)
    room_type       = models.CharField(max_length=100,default=None,null=False)
    ac              = models.BooleanField(default=False,blank=True,null=True)
    room_cost       = models.PositiveIntegerField(default=0,null=False)
    available       = models.BooleanField(default=True,null=False)

    class Meta:
        verbose_name = 'Hotel Room\'s Detail'

    def __str__(self):
        return self.room_id

class Hotel_Employee_Register(models.Model):
    superkey        = models.CharField(max_length=100,default=None,null=False)
    employee_id     = models.CharField(max_length=100,primary_key=True,default=None,null=False)
    fname           = models.CharField(max_length=20,default=None,null=False)
    mname           = models.CharField(max_length=20,default=None,null=True)
    lname           = models.CharField(max_length=20,default=None,null=False)
    picture         = models.ImageField(upload_to='profile_pic/',blank=True,default='profile_pic/profile_picture.jpg')
    designation     = models.CharField(max_length=50,default=None,null=False)
    salary          = models.IntegerField(default=0,null=False)
    dob             = models.DateField(null=False,default=None)
    phone           = models.CharField(max_length=13,default=None,null=False)
    emailid         = models.EmailField(max_length=100,default=None,null=False)
    address         = models.CharField(max_length=200,default=None,null=False)
    state           = models.CharField(max_length=50,default=None,null=False)
    city            = models.CharField(max_length=50,default=None,null=False)
    pincode         = models.CharField(max_length=10,default=None,null=False)
    father_name     = models.CharField(max_length=60,default=None,null=False)
    father_phone    = models.CharField(max_length=13,default=None,null=True)
    mother_name     = models.CharField(max_length=60,default=None,null=False)
    mother_phone    = models.CharField(max_length=13,default=None,null=True)
    from_date       = models.DateField(default=None,null=False)
    to_date         = models.DateField(default=None,null=True)

    class Meta:
        verbose_name = 'Hotel Employee\'s Detail'

    def __str__(self):
        return self.employee_id

class Customer_Register(models.Model):
    superkey        = models.CharField(max_length=100,default=None,null=False)
    customer_id     = models.CharField(max_length=100,primary_key=True,default=None,null=False)
    addar_no        = models.CharField(max_length=15,default=None,null=False)
    room_id         = models.CharField(max_length=50,default=None,null=False)
    fname           = models.CharField(max_length=20,default=None,null=False)
    mname           = models.CharField(max_length=20,default=None,null=True)
    lname           = models.CharField(max_length=20,default=None,null=False)
    no_of_days      = models.CharField(max_length=10,default=None,null=False)
    cost            = models.PositiveIntegerField(default=0,null=False)
    phone           = models.CharField(max_length=13,default=None,null=False)
    address         = models.CharField(max_length=200,default=None,null=False)
    amount_paid     = models.PositiveIntegerField(default=0,null=False)
    checkin_date    = models.DateField(default=None,null=False)
    checkout_date   = models.DateField(default=None,null=True)

    class Meta:
        verbose_name = 'Hotel Customer\'s Detail'

    def __str__(self):
        return self.customer_id

class Bill(models.Model):
    superkey        = models.CharField(max_length=100,default=None,null=False)
    bill_no         = models.CharField(max_length=50,default=None,null=False,primary_key=True)
    room_id         = models.CharField(max_length=50,default=None,null=False)
    customer_id     = models.CharField(max_length=100,default=None,null=False)
    cost            = models.PositiveIntegerField(default=0,null=False)
    type_of_work    = models.CharField(max_length=60,default=None,null=True)
    extra           = models.PositiveIntegerField(default=0,null=True)
    no_of_days      = models.PositiveIntegerField(default=0,null=False)
    day_out         = models.CharField(max_length=100,default=None,null=True)

    class Meta:
        verbose_name = 'Hotel Bill Detail'

    def __str__(self):
        return self.bill_no