from django.db import models

# Create your models here.

class Library_Management(models.Model):
    mainkey        = models.CharField(max_length=100,default=None,null=False)
    superkey        = models.CharField(max_length=100,default=None,unique=True,null=False)
    user_id         = models.CharField(max_length=50,default=None,primary_key=True,null=False)
    username        = models.CharField(max_length=20,default=None,unique=True,null=False)
    password        = models.CharField(max_length=20,default=None,null=False)
    emailid         = models.EmailField(max_length=100,default=None,null=False)
    phone           = models.CharField(max_length=10,default=None,null=False)
    library_name    = models.CharField(max_length=50,default=None,null=False)
    state           = models.CharField(max_length=30,default=None,null=False)
    city            = models.CharField(max_length=30,default=None,null=False)
    pincode         = models.CharField(max_length=6,default=None,null=False)
    address         = models.CharField(max_length=200,default=None,null=False)
    fine            = models.IntegerField(default=None,null=True)
    no_of_days      = models.IntegerField(default=None,null=True)

    class Meta:
        verbose_name = 'Library\'s Detail'

    def __str__(self):
        return self.username

class Library_Book_Register(models.Model):
    superkey        = models.CharField(max_length=100,default=None,null=False)
    isbn_number     = models.CharField(max_length=50,default=None,null=False)
    accession_no    = models.IntegerField(default=0,null=False)
    book_name       = models.CharField(max_length=100,default=None,null=False)
    publication     = models.CharField(max_length=60,default=None,null=False)
    author1         = models.CharField(max_length=60,default=None,null=False)
    author2         = models.CharField(max_length=60,default=None,null=True)
    with_cd         = models.BooleanField(default=False,null=False)
    no_of_pages     = models.CharField(max_length=1000,default=None,null=False)
    edition         = models.CharField(max_length=40,default=None,null=False)
    category        = models.CharField(max_length=60,default=None,null=False)
    issue           = models.BooleanField(default=False,null=False)
    
    class Meta:
        verbose_name = 'Library Book\'s Detail'

    def __str__(self):
        return self.book_name

class Library_Member_Register(models.Model):
    
    male = 'male'
    female = 'female'
    other = 'other'

    GENDER = (
        (male,"Male"),
        (female,"Female"),
        (other,"Other"),
    )
    superkey        = models.CharField(max_length=100,default=None,null=False)
    member_id       = models.CharField(max_length=50,default=None,primary_key=True,null=False)
    fname           = models.CharField(max_length=20,default=None,null=False)
    mname           = models.CharField(max_length=20,default=None,null=True)
    lname           = models.CharField(max_length=20,default=None,null=False)
    gender          = models.CharField(max_length=7,default=None,choices=GENDER,null=False)
    dob             = models.DateField(default=None,null=False)
    emailid         = models.EmailField(max_length=100,default=None,null=False)
    phone           = models.CharField(max_length=10,default=None,null=False)
    address         = models.CharField(max_length=200,default=None,null=False)

    class Meta:
        verbose_name = 'Library Member\'s Detail'

    def __str__(self):
        return self.member_id

class Book_Issue(models.Model):
    superkey        = models.CharField(max_length=100,default=None,null=False)
    isbn_number     = models.CharField(max_length=50,default=None,null=False)
    member_id       = models.CharField(max_length=100,default=None,null=False)
    accession_no    = models.IntegerField(default=None,null=False)
    date_of_issue   = models.DateField(default=None)
    date_of_return  = models.DateField(default=None)
    
    class Meta:
        verbose_name = 'Library Book\'s Issue Detail'

    def __str__(self):
        return self.member_id

class Library_Fine(models.Model):
    superkey        = models.CharField(max_length=100,default=None,null=False)
    accession_no    = models.IntegerField(default=0,null=False)
    isbn_number     = models.CharField(max_length=50,default=None,null=False)
    member_id       = models.CharField(max_length=100,default=None,null=False)
    date_of_issue   = models.DateField(default=None,null=False)
    date_of_return  = models.DateField(default=None,null=False)
    return_date     = models.DateField(default=None,null=False)
    fine            = models.IntegerField(default=None,null=False)

    class Meta:
        verbose_name = 'Library Fine Collection Detail'

    def __str__(self):
        return self.member_id