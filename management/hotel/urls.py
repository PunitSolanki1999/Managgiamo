from django.urls import path

app_name = 'hotel'

from .views import hotel_register,hotel_interface, hotel_room_register, update_hotel_room_form, update_hotel_room, hotel_room_detail_form, hotel_room_detail, hotel_employee_register, update_employee_form, update_employee, update_employee_leave_form, update_employee_leave, hotel_account_detail, customer_checkin, customer_checkout_form, customer_checkout, update_days_form, update_days, bill_detail, customer_detail_form, customer_detail, employee_detail_form, employee_detail, bill_generation, update_hotel_detail
urlpatterns = [
    # path('',hotel_login,name="hotel-login"),
    path('hotel_register/',hotel_register,name="hotel-register"),

    # path('logout/',logout,name="logout"),
    path('hotel_interface/',hotel_interface,name="hotel-interface"),
    path('hotel_room_register/',hotel_room_register,name="hotel-room-register"),
    path('update_hotel_room_form/',update_hotel_room_form,name="update-hotel-room-form"),
    path('update_hotel_room/<pk>/',update_hotel_room,name="update-hotel-room"),

    path('hotel_room_detail_form/',hotel_room_detail_form,name="hotel-room-detail-form"),
    path('hotel_room_detail/<pk>/',hotel_room_detail,name="hotel-room-detail"),

    path('hotel_employee_register/',hotel_employee_register,name="hotel-employee-register"),
    path('update_employee_form/',update_employee_form,name="update-employee-form"),
    path('update_employee/<pk>/',update_employee,name="update-employee"),
    path('update_employee_leave_form/',update_employee_leave_form,name='update-employee-leave-form'),
    path('update_employee_leave/<pk>/',update_employee_leave,name='update-employee-leave'),
    path('hotel_account_detail/',hotel_account_detail,name="hotel-account-detail"),

    path('customer_checkin/<pk>/',customer_checkin,name="customer-checkin"),
    path('customer_checkout_form/',customer_checkout_form,name="customer-checkout-form"),
    path('customer_checkout/<pk>/',customer_checkout,name="customer-checkout"),
   
    path('update_days_form/',update_days_form,name="update-days-form"),
    path('update_days/<pk>/',update_days,name="update-days"),

    path('bill_detail/',bill_detail,name="bill-detail"),

    path('customer_detail_form/',customer_detail_form,name="customer-detail-form"),
    path('customer_detail/<pk>/',customer_detail,name="customer-detail"),

    path('employee_detail_form/',employee_detail_form,name="employee-detail-form"),
    path('employee_detail/<pk>/',employee_detail,name="employee-detail"),

    path('bill_genertaion/<pk>/',bill_generation,name="bill-generation"),

    path('update_hotel_detail/',update_hotel_detail,name="update-hotel-detail"),

    
]