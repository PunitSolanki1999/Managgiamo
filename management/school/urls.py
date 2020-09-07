from django.urls import path
from .views import school_register,school_interface,faculty_insertion,student_insertion,employee_insertion,student_marks,student_detail_form,student_detail,faculty_detail_form,faculty_detail,employee_detail_form,employee_detail,income,income_class,update_student_form,update_student,update_faculty_form,update_faculty,update_employee_form,update_employee,update_student_fee_form,update_student_fee,update_student_leave_form,update_student_leave,update_faculty_leave_form,update_faculty_leave,update_employee_leave_form,update_employee_leave,school_account_detail,school_examiner_insert,student_attendance,update_examiner_form,update_examiner,student_marks_detail,student_marks_update_form,student_marks_update,examiner_detail_form,examiner_detail,update_examiner_leave_form,update_examiner_leave,update_attendance,update_attendance_form,student_attendance_report,update_school_detail, faculty_student_detail, faculty_student_detail_form, predict

app_name = 'school'

urlpatterns = [
  # path('',school_login,name='school-login'),
  path('register/',school_register,name='school-register'),
  path('school_interface/',school_interface,name='school-interface'),
  path('faculty_insertion/',faculty_insertion,name='faculty-insertion'),
  path('student_insertion/',student_insertion,name='student-insertion'),
  path('employee_insertion/',employee_insertion,name='employee-insertion'),
  # path('faculty_login/',faculty_login,name='faculty-login'),
  path('student_marks/',student_marks,name='student-marks'),
  path('student_detail_form/',student_detail_form,name='student-detail-form'),
  path('student_detail/<pk>/',student_detail,name='student-detail'),
  path('faculty_detail_form/',faculty_detail_form,name='faculty-detail-form'),
  path('faculty_detail/<pk>/',faculty_detail,name='faculty-detail'),
  path('employee_detail_form/',employee_detail_form,name='employee-detail-form'),
  path('employee_detail/<pk>/',employee_detail,name='employee-detail'),
  # path('logout/',logout,name='logout'),
  path('income/',income,name='income'),
  path('income_class/<clas>/<income>',income_class,name='income-class'),
  path('update_student_form/',update_student_form,name='update-student-form'),
  path('update_student/<pk>/',update_student,name='update-student'),
  path('update_faculty_form/',update_faculty_form,name='update-faculty-form'),
  path('update_faculty/<pk>/',update_faculty,name='update-faculty'),
  path('update_employee_form/',update_employee_form,name='update-employee-form'),
  path('update_employee/<pk>/',update_employee,name='update-employee'),
  path('update_student_fee_form/',update_student_fee_form,name='update-student-fee-form'),
  path('update_student_fee/<pk>/',update_student_fee,name='update-student-fee'),
  path('update_student_leave_form/',update_student_leave_form,name='update-student-leave-form'),
  path('update_student_leave/<pk>/',update_student_leave,name='update-student-leave'),
  path('update_faculty_leave_form/',update_faculty_leave_form,name='update-faculty-leave-form'),
  path('update_faculty_leave/<pk>/',update_faculty_leave,name='update-faculty-leave'),
  path('update_employee_leave_form/',update_employee_leave_form,name='update-employee-leave-form'),
  path('update_employee_leave/<pk>/',update_employee_leave,name='update-employee-leave'),
  path('school_account_detail/',school_account_detail,name='school-account-detail'),

  path('school_examiner_insert/',school_examiner_insert,name='school-examiner-insert'),
  path('student_attendance/',student_attendance,name='student-attendance'),
  path('update_examiner_form/',update_examiner_form,name='update-examiner-form'),
  path('update_examiner/<pk>/',update_examiner,name='update-examiner'),
  # path('examiner_login/',examiner_login,name='examiner-login'),
  path('student_marks_detail/',student_marks_detail,name='student-marks-detail'),
  path('student_marks_update_form/',student_marks_update_form,name='student-marks-update-form'),
  path('student_marks_update/<pk>/',student_marks_update,name='student-marks-update'),
  path('examiner_detail_form/',examiner_detail_form,name='examiner-detail-form'),
  path('examiner_detail/<pk>/',examiner_detail,name='examiner-detail'),
  path('update_examiner_leave_form/',update_examiner_leave_form,name='update-examiner-leave-form'),
  path('update_examiner_leave/<pk>/',update_examiner_leave,name='update-examiner-leave'),
  path('update_attendance_form/',update_attendance_form,name='update-attendance-form'),
  path('update_attendance/<pk>/',update_attendance,name='update-attendance'),
  path('student_attendance_report/',student_attendance_report,name='student-attendance-report'),

  path('update_school_detail/',update_school_detail,name="update-school-detail"),

  # path('username/',username,name="username"),
  # path('otp_verification/<username>/',otp_verification,name="otp-verification"),
  # path('change_password/',change_password,name="change-password"),
  # path(r'otp/(?P<otp>\d+)/<school>/',otp_confirm,name="otp"),

  path('faculty_student_detail_form/',faculty_student_detail_form,name='faculty-student-detail-form'),
  path('faculty_student_detail/<pk>/',faculty_student_detail,name='faculty-student-detail'),

  # path('pred1/',predict1,name='predict1'),
  path('pred/',predict,name='predict')
]