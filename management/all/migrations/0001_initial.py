# Generated by Django 3.0.3 on 2020-03-06 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_Data',
            fields=[
                ('mainkey', models.CharField(default=None, max_length=100, unique=True)),
                ('user_id', models.CharField(default=None, max_length=50, primary_key=True, serialize=False)),
                ('username', models.CharField(default=None, max_length=20, unique=True)),
                ('password', models.CharField(default=None, max_length=20)),
                ('management', models.CharField(default=None, max_length=1000)),
                ('organization', models.CharField(default=None, max_length=100, unique=True)),
                ('emailid', models.EmailField(default=None, max_length=100)),
                ('phone', models.CharField(default=None, max_length=10)),
                ('state', models.CharField(default=None, max_length=30)),
                ('city', models.CharField(default=None, max_length=30)),
                ('pincode', models.CharField(default=None, max_length=10)),
                ('address', models.CharField(default=None, max_length=200)),
            ],
        ),
    ]
