from django.urls import path
from .views import register,library_interface,library_book_register,library_member_register,update_fine,book_issue,return_book_form,return_book,book_in_library,book_in_library_form,member_in_library_form,member_in_library,book_issue_detail_form,library_book_fine,library_account_detail,  update_library_detail

app_name = 'library'

urlpatterns = [
    # path('',login,name='library-login'),
    path('register/',register,name='library-register'),
    path('library_interface/',library_interface,name='library-interface'),
    path('library_book_register/',library_book_register,name='book-register'),
    path('library_member_register/',library_member_register,name='member-register'),
    path('update_fine/',update_fine,name='update-fine'),
    path('book_issue/',book_issue,name='book-issue'),
    path('return_book_form/',return_book_form,name='return-book-form'),
    path('return_book/<int:pk>/',return_book,name='return-book'),
    path('book_in_library_form/',book_in_library_form,name='book-in-library-form'),
    path('book_in_library/<int:pk>/',book_in_library,name='book-in-library'),
    path('member_in_library_form/',member_in_library_form,name='member-in-library-form'),
    path('member_in_library/<pk>/',member_in_library,name='member-in-library'),
    path('book_issue_detail_form/',book_issue_detail_form,name='book-issue-detail-form'),
    path('library_book_fine/',library_book_fine,name='library-book-fine'),
    path('library_account_detail/',library_account_detail,name='library-account-detail'),
    # path('logout/',logout,name='logout'),
    path('update_library_detail/',update_library_detail,name="update-library-detail"),

]