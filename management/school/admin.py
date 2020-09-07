from django.contrib import admin
from .models import School_Management, School_Student_Data, School_Faculty_Data, School_Employee_Data, School_Marks_Data, School_Examination_Data, School_Total_Attendance
# Register your models here.

admin.site.register(School_Management)
admin.site.register(School_Student_Data)
admin.site.register(School_Faculty_Data)
admin.site.register(School_Employee_Data)
admin.site.register(School_Marks_Data)
admin.site.register(School_Examination_Data)
admin.site.register(School_Total_Attendance)


