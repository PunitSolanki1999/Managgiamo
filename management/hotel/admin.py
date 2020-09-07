from django.contrib import admin
from .models import Hotel_Employee_Register, Hotel_Management, Hotel_Room_Register, Customer_Register, Bill
# Register your models here.

admin.site.register(Hotel_Employee_Register)
admin.site.register(Hotel_Management)
admin.site.register(Hotel_Room_Register)
admin.site.register(Customer_Register)
admin.site.register(Bill)