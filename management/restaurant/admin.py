from django.contrib import admin
# Register your models here.
from .models import Rest_Employee, Rest_Food, Rest_Management, Ingredient_Table, Bill, Bill_Product

admin.site.register(Rest_Management)
admin.site.register(Rest_Food)
admin.site.register(Rest_Employee)
admin.site.register(Ingredient_Table)
admin.site.register(Bill)
admin.site.register(Bill_Product)