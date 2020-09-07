# Generated by Django 3.0.3 on 2020-03-06 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School_Employee_Data',
            fields=[
                ('superkey', models.CharField(default=None, max_length=100)),
                ('employee_id', models.CharField(default=None, max_length=50, primary_key=True, serialize=False)),
                ('employee_no', models.PositiveIntegerField(default=None)),
                ('fname', models.CharField(default=None, max_length=20)),
                ('mname', models.CharField(default=None, max_length=20, null=True)),
                ('lname', models.CharField(default=None, max_length=20)),
                ('picture', models.ImageField(blank=True, default='profile_pic/profile_picture.jpg', upload_to='profile_pic/')),
                ('phone', models.CharField(default=None, max_length=10)),
                ('father_name', models.CharField(default=None, max_length=50)),
                ('father_phone', models.CharField(default=None, max_length=10, null=True)),
                ('mother_name', models.CharField(default=None, max_length=50)),
                ('mother_phone', models.CharField(default=None, max_length=10, null=True)),
                ('work', models.CharField(default=None, max_length=100, null=True)),
                ('dob', models.DateField()),
                ('salary', models.PositiveIntegerField(null=True)),
                ('state', models.CharField(default=None, max_length=30)),
                ('city', models.CharField(default=None, max_length=30)),
                ('address', models.CharField(default=None, max_length=200)),
                ('pincode', models.CharField(default=None, max_length=10)),
                ('from_date', models.DateField(default=None)),
                ('to_date', models.DateField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='School_Examination_Data',
            fields=[
                ('superkey', models.CharField(default=None, max_length=100)),
                ('examiner_id', models.CharField(default=None, max_length=50, primary_key=True, serialize=False)),
                ('examiner_no', models.PositiveIntegerField(default=None)),
                ('username', models.CharField(default=None, max_length=20, unique=True)),
                ('password', models.CharField(default=None, max_length=20)),
                ('fname', models.CharField(default=None, max_length=20)),
                ('mname', models.CharField(default=None, max_length=20, null=True)),
                ('lname', models.CharField(default=None, max_length=20)),
                ('picture', models.ImageField(blank=True, default='profile_pic/profile_picture.jpg', upload_to='profile_pic/')),
                ('emailid', models.EmailField(max_length=100)),
                ('phone', models.CharField(default=None, max_length=10)),
                ('father_name', models.CharField(default=None, max_length=50)),
                ('father_phone', models.CharField(default=None, max_length=10, null=True)),
                ('mother_name', models.CharField(default=None, max_length=50)),
                ('mother_phone', models.CharField(default=None, max_length=10, null=True)),
                ('dob', models.DateField()),
                ('salary', models.PositiveIntegerField(null=True)),
                ('state', models.CharField(default=None, max_length=30)),
                ('city', models.CharField(default=None, max_length=30)),
                ('address', models.CharField(default=None, max_length=200)),
                ('pincode', models.CharField(default=None, max_length=10)),
                ('from_date', models.DateField(default=None)),
                ('to_date', models.DateField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='School_Faculty_Data',
            fields=[
                ('superkey', models.CharField(default=None, max_length=100)),
                ('faculty_id', models.CharField(default=None, max_length=50, primary_key=True, serialize=False)),
                ('faculty_no', models.PositiveIntegerField(default=None)),
                ('username', models.CharField(default=None, max_length=20, unique=True)),
                ('password', models.CharField(default=None, max_length=20)),
                ('fname', models.CharField(default=None, max_length=20)),
                ('mname', models.CharField(default=None, max_length=20, null=True)),
                ('lname', models.CharField(default=None, max_length=20)),
                ('picture', models.ImageField(blank=True, default='profile_pic/profile_picture.jpg', upload_to='profile_pic/')),
                ('emailid', models.EmailField(max_length=100)),
                ('phone', models.CharField(default=None, max_length=10)),
                ('father_name', models.CharField(default=None, max_length=50)),
                ('father_phone', models.CharField(default=None, max_length=10, null=True)),
                ('mother_name', models.CharField(default=None, max_length=50)),
                ('mother_phone', models.CharField(default=None, max_length=10, null=True)),
                ('subject', models.CharField(default=None, max_length=100, null=True)),
                ('dob', models.DateField()),
                ('salary', models.PositiveIntegerField(null=True)),
                ('state', models.CharField(default=None, max_length=30)),
                ('city', models.CharField(default=None, max_length=30)),
                ('address', models.CharField(default=None, max_length=200)),
                ('pincode', models.CharField(default=None, max_length=10)),
                ('clas', models.CharField(choices=[(None, 'None'), ('nursery', 'Nursery'), ('lkg', 'LKG'), ('pre first', 'Pre First'), ('first', 'First'), ('second', 'Second'), ('third', 'Third'), ('fourth', 'Fourth'), ('fifth', 'Fifth'), ('sixth', 'Sixth'), ('seventh', 'Seventh'), ('eigth', 'Eigth'), ('ninth', 'Ninth'), ('tenth', 'Tenth'), ('eleventh', 'Eleventh'), ('twelveth', 'Twelveth')], default=None, max_length=15, null=True)),
                ('from_date', models.DateField(default=None)),
                ('to_date', models.DateField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='School_Management',
            fields=[
                ('mainkey', models.CharField(default=None, max_length=100)),
                ('superkey', models.CharField(default=None, max_length=100, unique=True)),
                ('user_id', models.CharField(default=None, max_length=50, primary_key=True, serialize=False)),
                ('username', models.CharField(default=None, max_length=20, unique=True)),
                ('password', models.CharField(default=None, max_length=20)),
                ('school_code', models.CharField(default=None, max_length=10, unique=True)),
                ('emailid', models.EmailField(default=None, max_length=100)),
                ('phone', models.CharField(default=None, max_length=10)),
                ('organisation', models.CharField(default=None, max_length=20)),
                ('state', models.CharField(default=None, max_length=30)),
                ('city', models.CharField(default=None, max_length=30)),
                ('pincode', models.CharField(default=None, max_length=10)),
                ('address', models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='School_Marks_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('superkey', models.CharField(default=None, max_length=50)),
                ('student_id', models.CharField(default=None, max_length=100)),
                ('clas', models.CharField(choices=[(None, 'None'), ('nursery', 'Nursery'), ('lkg', 'LKG'), ('pre first', 'Pre First'), ('first', 'First'), ('second', 'Second'), ('third', 'Third'), ('fourth', 'Fourth'), ('fifth', 'Fifth'), ('sixth', 'Sixth'), ('seventh', 'Seventh'), ('eigth', 'Eigth'), ('ninth', 'Ninth'), ('tenth', 'Tenth'), ('eleventh', 'Eleventh'), ('twelveth', 'Twelveth')], default=None, max_length=15, null=True)),
                ('subject', models.CharField(default=None, max_length=40)),
                ('marks', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='School_Student_Data',
            fields=[
                ('superkey', models.CharField(default=None, max_length=100)),
                ('student_id', models.CharField(default=None, max_length=50, primary_key=True, serialize=False)),
                ('scholar_no', models.PositiveIntegerField(default=None)),
                ('fname', models.CharField(default=None, max_length=20)),
                ('mname', models.CharField(default=None, max_length=20, null=True)),
                ('lname', models.CharField(default=None, max_length=20)),
                ('picture', models.ImageField(blank=True, default='profile_pic/profile_picture.jpg', upload_to='profile_pic/')),
                ('father_name', models.CharField(default=None, max_length=50)),
                ('father_phone', models.CharField(default=None, max_length=10, null=True)),
                ('mother_name', models.CharField(default=None, max_length=50)),
                ('mother_phone', models.CharField(default=None, max_length=10, null=True)),
                ('dob', models.DateField()),
                ('fee', models.PositiveIntegerField(null=True)),
                ('fee_submitted', models.PositiveIntegerField(default=0, null=True)),
                ('state', models.CharField(default=None, max_length=30)),
                ('city', models.CharField(default=None, max_length=30)),
                ('address', models.CharField(default=None, max_length=200)),
                ('pincode', models.CharField(default=None, max_length=10)),
                ('clas', models.CharField(choices=[(None, 'None'), ('nursery', 'Nursery'), ('lkg', 'LKG'), ('pre first', 'Pre First'), ('first', 'First'), ('second', 'Second'), ('third', 'Third'), ('fourth', 'Fourth'), ('fifth', 'Fifth'), ('sixth', 'Sixth'), ('seventh', 'Seventh'), ('eigth', 'Eigth'), ('ninth', 'Ninth'), ('tenth', 'Tenth'), ('eleventh', 'Eleventh'), ('twelveth', 'Twelveth')], default=None, max_length=15)),
                ('from_date', models.DateField(default=None)),
                ('to_date', models.DateField(default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='School_Total_Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('superkey', models.CharField(default=None, max_length=50)),
                ('student_id', models.CharField(default=None, max_length=100)),
                ('clas', models.CharField(choices=[(None, 'None'), ('nursery', 'Nursery'), ('lkg', 'LKG'), ('pre first', 'Pre First'), ('first', 'First'), ('second', 'Second'), ('third', 'Third'), ('fourth', 'Fourth'), ('fifth', 'Fifth'), ('sixth', 'Sixth'), ('seventh', 'Seventh'), ('eigth', 'Eigth'), ('ninth', 'Ninth'), ('tenth', 'Tenth'), ('eleventh', 'Eleventh'), ('twelveth', 'Twelveth')], default=None, max_length=12, null=True)),
                ('student_attend', models.PositiveIntegerField(default=0)),
                ('total_working', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
