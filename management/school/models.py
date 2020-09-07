from django.db import models

from django.core.validators import MaxValueValidator
# Create your models here.
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

class School_Management(models.Model):
    mainkey        = models.CharField(max_length=100,default=None,null=False)
    superkey        = models.CharField(max_length=100,default=None,unique=True,null=False)
    user_id         = models.CharField(max_length=50,default=None,primary_key=True,null=False)
    username        = models.CharField(max_length=20,default=None,unique=True,null=False)
    password        = models.CharField(max_length=20,default=None,null=False)
    school_code     = models.CharField(max_length=10,default=None,unique=True,null=False)
    emailid         = models.EmailField(max_length=100,default=None,null=False)
    phone           = models.CharField(max_length=10,default=None,null=False)
    organisation    = models.CharField(max_length=20,default=None,null=False)
    state           = models.CharField(max_length=30,default=None,null=False)
    city            = models.CharField(max_length=30,default=None,null=False)
    pincode         = models.CharField(max_length=10,default=None,null=False)
    address         = models.CharField(max_length=200,default=None,null=False)

    def __str__(self):
        return self.username

class School_Student_Data(models.Model):  
    superkey        = models.CharField(max_length=100,default=None,null=False)
    student_id      = models.CharField(max_length=50,default=None,primary_key=True,null=False)
    scholar_no      = models.PositiveIntegerField(default=None,null=False)
    fname           = models.CharField(max_length=20,default=None,null=False)
    mname           = models.CharField(max_length=20,default=None,null=True)
    lname           = models.CharField(max_length=20,default=None,null=False)
    picture         = models.ImageField(upload_to='profile_pic/',blank=True,default='profile_pic/profile_picture.jpg')
    father_name     = models.CharField(max_length=50,default=None,null=False)
    father_phone    = models.CharField(max_length=10,default=None,null=True)
    mother_name     = models.CharField(max_length=50,default=None,null=False)
    mother_phone    = models.CharField(max_length=10,default=None,null=True)
    dob             = models.DateField(null=False)
    fee             = models.PositiveIntegerField(null=True)
    fee_submitted   = models.PositiveIntegerField(null=True,default=0)
    state           = models.CharField(max_length=30,default=None,null=False)
    city            = models.CharField(max_length=30,default=None,null=False)
    address         = models.CharField(max_length=200,default=None,null=False)
    pincode         = models.CharField(max_length=10,default=None,null=False)
    clas            = models.CharField(max_length=15,choices=CLASS_CHOICE,default=None,null=False)
    from_date       = models.DateField(default=None,null=False)
    to_date         = models.DateField(default=None,null=True)

    def __str__(self):
        return self.student_id


class School_Faculty_Data(models.Model):
    superkey        = models.CharField(max_length=100,default=None,null=False)
    faculty_id      = models.CharField(max_length=50,default=None,primary_key=True,null=False)
    faculty_no      = models.PositiveIntegerField(default=None,null=False)
    username        = models.CharField(max_length=20,default=None,unique=True,null=False)
    password        = models.CharField(max_length=20,default=None,null=False)
    fname           = models.CharField(max_length=20,default=None,null=False)
    mname           = models.CharField(max_length=20,default=None,null=True)
    lname           = models.CharField(max_length=20,default=None,null=False)
    picture         = models.ImageField(upload_to='profile_pic/',blank=True,default='profile_pic/profile_picture.jpg')
    emailid         = models.EmailField(max_length=100,null=False)
    phone           = models.CharField(max_length=10,default=None,null=False)
    father_name     = models.CharField(max_length=50,default=None,null=False)
    father_phone    = models.CharField(max_length=10,default=None,null=True)
    mother_name     = models.CharField(max_length=50,default=None,null=False)
    mother_phone    = models.CharField(max_length=10,default=None,null=True)
    subject         = models.CharField(max_length=100,default=None,null=True)
    dob             = models.DateField(null=False)
    salary          = models.PositiveIntegerField(null=True)
    state           = models.CharField(max_length=30,default=None,null=False)
    city            = models.CharField(max_length=30,default=None,null=False)
    address         = models.CharField(max_length=200,default=None,null=False)
    pincode         = models.CharField(max_length=10,default=None,null=False)
    clas            = models.CharField(max_length=15,choices=CLASS_CHOICE,default=None,null=True)
    from_date       = models.DateField(default=None,null=False)
    to_date         = models.DateField(default=None,null=True)
    
    def __str__(self):
        return self.username

class School_Employee_Data(models.Model):
    superkey        = models.CharField(max_length=100,default=None,null=False)
    employee_id     = models.CharField(max_length=50,default=None,primary_key=True,null=False)
    employee_no     = models.PositiveIntegerField(default=None,null=False)
    fname           = models.CharField(max_length=20,default=None,null=False)
    mname           = models.CharField(max_length=20,default=None,null=True)
    lname           = models.CharField(max_length=20,default=None,null=False)
    picture         = models.ImageField(upload_to='profile_pic/',blank=True,default='profile_pic/profile_picture.jpg')
    phone           = models.CharField(max_length=10,default=None,null=False)
    father_name     = models.CharField(max_length=50,default=None,null=False)
    father_phone    = models.CharField(max_length=10,default=None,null=True)
    mother_name     = models.CharField(max_length=50,default=None,null=False)
    mother_phone    = models.CharField(max_length=10,default=None,null=True)
    work            = models.CharField(max_length=100,default=None,null=True)
    dob             = models.DateField(null=False)
    salary          = models.PositiveIntegerField(null=True)
    state           = models.CharField(max_length=30,default=None,null=False)
    city            = models.CharField(max_length=30,default=None,null=False)
    address         = models.CharField(max_length=200,default=None,null=False)
    pincode         = models.CharField(max_length=10,default=None,null=False)
    from_date       = models.DateField(default=None,null=False)
    to_date         = models.DateField(default=None,null=True)

    def __str__(self):
        return self.employee_id

class School_Examination_Data(models.Model):
    superkey        = models.CharField(max_length=100,default=None,null=False)
    examiner_id     = models.CharField(max_length=50,default=None,primary_key=True,null=False)
    examiner_no     = models.PositiveIntegerField(default=None,null=False)
    username        = models.CharField(max_length=20,default=None,unique=True,null=False)
    password        = models.CharField(max_length=20,default=None,null=False)
    fname           = models.CharField(max_length=20,default=None,null=False)
    mname           = models.CharField(max_length=20,default=None,null=True)
    lname           = models.CharField(max_length=20,default=None,null=False)
    picture         = models.ImageField(upload_to='profile_pic/',blank=True,default='profile_pic/profile_picture.jpg')
    emailid         = models.EmailField(max_length=100,null=False)
    phone           = models.CharField(max_length=10,default=None,null=False)
    father_name     = models.CharField(max_length=50,default=None,null=False)
    father_phone    = models.CharField(max_length=10,default=None,null=True)
    mother_name     = models.CharField(max_length=50,default=None,null=False)
    mother_phone    = models.CharField(max_length=10,default=None,null=True)
    dob             = models.DateField(null=False)
    salary          = models.PositiveIntegerField(null=True)
    state           = models.CharField(max_length=30,default=None,null=False)
    city            = models.CharField(max_length=30,default=None,null=False)
    address         = models.CharField(max_length=200,default=None,null=False)
    pincode         = models.CharField(max_length=10,default=None,null=False)
    from_date       = models.DateField(default=None,null=False)
    to_date         = models.DateField(default=None,null=True)
    
    def __str__(self):
        return self.username

class School_Marks_Data(models.Model):
    superkey        = models.CharField(max_length=50,default=None,null=False)
    student_id      = models.CharField(max_length=100,default=None,null=False)
    clas            = models.CharField(max_length=15,choices=CLASS_CHOICE,default=None,null=True)
    subject         = models.CharField(max_length=40,default=None,null=False)
    marks           = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.student_id

class School_Total_Attendance(models.Model):
    superkey        = models.CharField(max_length=50,default=None,null=False)
    student_id      = models.CharField(max_length=100,default=None,null=False)
    clas            = models.CharField(max_length=12,choices=CLASS_CHOICE,default=None,null=True)
    student_attend  = models.PositiveIntegerField(default=0)
    total_working   = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.student_id