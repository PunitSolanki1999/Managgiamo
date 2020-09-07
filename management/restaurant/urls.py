from django.urls import path

app_name = 'rest'

from .views import rest_register, rest_interface, rest_employee_register, rest_account_detail, update_employee_form, update_employee, update_employee_leave_form, update_employee_leave, food_insert, ingredient_entry, update_ingredient_detail_form, update_ingredient_detail, bill_data_entry, bill_food_entry, bill_final, bill_search, employee_detail_form, employee_detail, update_rest_detail, predict

urlpatterns = [
    # path('',rest_login,name='rest-login'),
    path('rest_register/',rest_register,name="rest-register"),
    path('rest_interface/',rest_interface,name="rest-interface"),
    # path('logout/',logout,name="logout"),
    path('rest_employee_register/',rest_employee_register,name="rest-employee-register"),
    path('rest_account_detail/',rest_account_detail,name="rest-account-detail"),
    path('update_employee_form/',update_employee_form,name="update-employee-form"),
    path('update_employee/<pk>/',update_employee,name="update-employee"),
    path('update_employee_leave_form/',update_employee_leave_form,name="update-employee-leave-form"),
    path('update_employee_leave/<pk>/',update_employee_leave,name="update-employee-leave"),
    path('food_insert/',food_insert,name="food-insert"),
    path('ingredient_entry/',ingredient_entry,name="ingredient-entry"),
    path('update_ingredient_detail_form/',update_ingredient_detail_form,name="update-ingredient-detail-form"),
    path('update_ingredient_detail/<pk>/',update_ingredient_detail,name="update-ingredient-detail"),
    path('bill_data_entry/',bill_data_entry,name="bill-data-entry"),
    path('bill_food_entry/<pk>/',bill_food_entry,name="bill-food-entry"),
    path('bill_final/<pk>/',bill_final,name="bill-final"),
    path('bill_search/',bill_search,name="bill-search"),
    
    path('employee_detail_form/',employee_detail_form,name="employee-detail-form"),
    path('employee_detail/<pk>/',employee_detail,name="employee-detail"),

    path('update_rest_detail/',update_rest_detail,name="update-rest-detail"),

    # path('username/',username,name="username"),
    # path('otp_verification/<username>/',otp_verification,name="otp-verification"),
    # path('change_password/',change_password,name="change-password"),
    # path(r'otp/(?P<otp>\d+)/<rest>/',otp_confirm,name="otp"),

    path('pred/',predict,name='predict'),
]