from django.contrib import admin

from .models import Library_Management, Library_Book_Register, Library_Member_Register, Book_Issue, Library_Fine
# Register your models here.
admin.site.register(Library_Management)
admin.site.register(Library_Book_Register)
admin.site.register(Library_Member_Register)
admin.site.register(Book_Issue)
admin.site.register(Library_Fine)