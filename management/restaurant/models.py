from django.db import models
# Create your models here.
class Rest_Management(models.Model):
    mainkey        = models.CharField(max_length=100,default=None,null=False)
    superkey        = models.CharField(max_length=100,default=None,unique=True,null=False)
    license_no      = models.CharField(max_length=20,primary_key=True,default=None,null=False)
    username        = models.CharField(max_length=20,default=None,unique=True,null=False)
    password        = models.CharField(max_length=20,default=None,null=False)
    emailid         = models.EmailField(max_length=100,default=None,null=False)
    phone           = models.CharField(max_length=10,default=None,null=False)
    rest_name       = models.CharField(max_length=50,default=None,null=False)
    state           = models.CharField(max_length=30,default=None,null=False)
    city            = models.CharField(max_length=30,default=None,null=False)
    pincode         = models.CharField(max_length=6,default=None,null=False)
    address         = models.CharField(max_length=200,default=None,null=False)

    class Meta:
        verbose_name = 'Restaurant\'s Detail'
    
    def __str__(self):
        return self.username

class Rest_Employee(models.Model):
    superkey        = models.CharField(max_length=100,default=None,null=False)
    employee_id     = models.CharField(max_length=100,primary_key=True,default=None,null=False)
    fname           = models.CharField(max_length=20,default=None,null=False)
    mname           = models.CharField(max_length=20,default=None,null=True)
    lname           = models.CharField(max_length=20,default=None,null=False)
    picture         = models.ImageField(upload_to='profile_pic/',blank=True,default='profile_pic/profile_picture.jpg')
    work            = models.CharField(max_length=50,default=None,null=False)
    salary          = models.IntegerField(default=0,null=False)
    dob             = models.DateField(null=False,default=None)
    phone           = models.CharField(max_length=13,default=None,null=False)
    address         = models.CharField(max_length=200,default=None,null=False)
    state           = models.CharField(max_length=50,default=None,null=False)
    city            = models.CharField(max_length=50,default=None,null=False)
    pincode         = models.CharField(max_length=10,default=None,null=False)
    father_name     = models.CharField(max_length=60,default=None,null=False)
    father_phone    = models.CharField(max_length=13,default=None,null=True)
    from_date       = models.DateField(default=None,null=False)
    to_date         = models.DateField(default=None,null=True)

    class Meta:
        verbose_name = 'Restaurant Employee\'s Detail'

    def __str__(self):
        return self.employee_id

class Rest_Food(models.Model):
    superkey        = models.CharField(max_length=100,default=None,null=False)
    food_id         = models.CharField(max_length=50,primary_key=True,default=None,null=False)
    food_name       = models.CharField(max_length=100,default=None,null=False)
    price           = models.PositiveIntegerField(default=0,null=False)

    class Meta:
        verbose_name = 'Restaurant Meal Detail'

    def __str__(self):
        return self.food_id

class Ingredient_Table(models.Model):
    superkey        = models.CharField(max_length=100,default=None,null=False)
    ingredient_id   = models.CharField(max_length=40,primary_key=True,default=None,null=False)
    ingredient_name = models.CharField(max_length=100,default=None,null=False)
    total           = models.IntegerField(default=0,null=False)
    available       = models.IntegerField(default=0,null=False)

    class Meta:
        verbose_name = 'Restaurant Store Detail'

    def __str__(self):
        return self.ingredient_id  

class Bill(models.Model):
    superkey        = models.CharField(max_length=100,default=None,null=False)
    bill_id         = models.CharField(max_length=50,primary_key=True,default=None,null=False)
    table_no        = models.CharField(max_length=50,default=None,null=False)
    
    class Meta:
        verbose_name = 'Restaurant Bill Detail'

    def __str__(self):
        return self.bill_id

class Bill_Product(models.Model):
    superkey        = models.CharField(max_length=100,default=None,null=False)
    bill_id         = models.CharField(max_length=50,default=None,null=False)
    table_no        = models.CharField(max_length=50,default=None,null=False)
    food_id         = models.CharField(max_length=50,default=None,null=False)
    quantity        = models.IntegerField(default=0,null=False)
    price           = models.IntegerField(default=0,null=False)