from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views, HOD_views, Student_views, Staff_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),

    # <LOGIN PATH>
    path('', views.LOGIN, name='land'),
    path('/login', views.LOGIN, name='login'),
    path('doLogin', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='Logout'),

    # <PROFILE UPDATE>
    path('profile', views.PROFILE, name='profile'),
    path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),

    # <HOD PANEL>
    path('HOD/home', HOD_views.HOME, name='HOD_home'),
    path('HOD/Student/Add', HOD_views.ADD_STUDENT, name='add_student'),
    path('HOD/Student/View', HOD_views.VIEW_STUDENT, name='view_student'),
    path('HOD/Student/Edit/<str:id>', HOD_views.EDIT_STUDENT, name='edit_student'),
    path('HOD/Student/Update', HOD_views.UPDATE_STUDENT, name='update_student'),
    path('HOD/Student/Delete/<str:admin>', HOD_views.DELETE_STUDENT, name='delete_student'),
    ####
    path('HOD/Program/Add', HOD_views.ADD_PROGRAM, name='add_program'),
    path('HOD/Program/View', HOD_views.VIEW_PROGRAM, name='view_program'),
    path('HOD/Program/Edit/<str:id>', HOD_views.EDIT_PROGRAM, name='edit_program'),
    path('HOD/Program/Update', HOD_views.UPDATE_PROGRAM, name='update_program'),
    path('HOD/Program/Delete/<str:id>', HOD_views.DELETE_PROGRAM, name='delete_program'),
    ####
    path('HOD/Staff/Add', HOD_views.ADD_STAFF, name='add_staff'),
    path('HOD/Staff/View', HOD_views.VIEW_STAFF, name='view_staff'),
    path('HOD/Staff/Edit/<str:id>', HOD_views.EDIT_STAFF, name='edit_staff'),
    path('HOD/Staff/Update', HOD_views.UPDATE_STAFF, name='update_staff'),
    path('HOD/Staff/Delete/<str:admin>', HOD_views.DELETE_STAFF, name='delete_staff'),
    ####
    path('HOD/Course/Add', HOD_views.ADD_COURSE, name='add_course'),
    path('HOD/Course/View', HOD_views.VIEW_COURSE, name='view_course'),
    path('HOD/Course/Edit/<str:id>', HOD_views.EDIT_COURSE, name='edit_course'),
    path('HOD/Course/Update', HOD_views.UPDATE_COURSE, name='update_course'),
    path('HOD/Course/Delete/<int:id>', HOD_views.DELETE_COURSE, name='delete_course'),
    ####
    path('HOD/Session/Add', HOD_views.ADD_SESSION, name='add_session'),
    path('HOD/Session/View', HOD_views.VIEW_SESSION, name='view_session'),
    path('HOD/Session/Edit/<str:id>', HOD_views.EDIT_SESSION, name='edit_session'),
    path('HOD/Session/Update', HOD_views.UPDATE_SESSION, name='update_session'),
    path('HOD/Session/Delete/<int:id>', HOD_views.DELETE_SESSION, name='delete_session'),
    ####
    path('HOD/Staff/Send_Notification', HOD_views.STAFF_SEND_NOTIFICATIONS, name = 'staff_send_notifications'),
    path('HOD/Staff/Save_Notification', HOD_views.STAFF_SAVE_NOTIFICATIONS, name = 'staff_save_notifications'),

    
    path('HOD/Student/Send_Notification', HOD_views.STUDENT_SEND_NOTIFICATIONS, name = 'student_send_notifications'),
    path('HOD/Student/Save_Notification', HOD_views.STUDENT_SAVE_NOTIFICATIONS, name = 'student_save_notifications'),
    ####
    path('HOD/Staff/Leave_View', HOD_views.STAFF_LEAVE_VIEW, name = 'staff_leave_view'),
    path('HOD/Staff/Approve_Leave/<str:id>', HOD_views.STAFF_APPROVE_LEAVE, name = 'staff_approve_leave'),
    path('HOD/Staff/Dispprove_Leave/<str:id>', HOD_views.STAFF_DISAPPROVE_LEAVE, name = 'staff_disapprove_leave'),
    ####
    path('HOD/Staff/Feedback', HOD_views.STAFF_FEEDBACK_VIEW, name = 'staff_feedback_view'),
    path('HOD/Staff/Feedback_Reply/<str:admin>', HOD_views.STAFF_FEEDBACK_REPLY, name = 'Staff_feedback_reply'),
    path('HOD/Staff/Feedback_Ignore/<str:admin>', HOD_views.STAFF_FEEDBACK_IGNORE, name = 'Staff_feedback_ignore'),
    ####
    path('HOD/Student/Feedback', HOD_views.STUDENT_FEEDBACK_VIEW, name = 'student_feedback_view'),
    path('HOD/Student/Feedback_Reply/<str:admin>', HOD_views.STUDENT_FEEDBACK_REPLY, name = 'Student_feedback_reply'),
    path('HOD/Student/Feedback_Ignore/<str:admin>', HOD_views.STUDENT_FEEDBACK_IGNORE, name = 'Student_feedback_ignore'),
    ####
    path('HOD/Student/Leave_View', HOD_views.STUDENT_LEAVE_VIEW, name = 'student_leave_view'),
    path('HOD/Student/Approve_Leave/<str:id>', HOD_views.STUDENT_APPROVE_LEAVE, name = 'student_approve_leave'),
    path('HOD/Student/Dispprove_Leave/<str:id>', HOD_views.STUDENT_DISAPPROVE_LEAVE, name = 'student_disapprove_leave'),

    # THIS IS FOR STAFF URLS
    path('Staff/home', Staff_views.HOME, name = 'Staff_home'),
    ####
    path('Staff/Notifications', Staff_views.NOTIFICATIONS, name = 'Staff_notifications'),
    path('Staff/Mark_as_done/<str:status>', Staff_views.STAFF_NOTIFICATION_MARK_AS_DONE, name='staff_notification_mark_as_mark'),
    ####
    path('Staff/Apply_Leave', Staff_views.STAFF_APPLY_LEAVE, name = 'Staff_apply_leave'),
    path('Staff/Apply_Leave_Save', Staff_views.STAFF_APPLY_LEAVE_SAVE, name = 'Staff_apply_leave_save'),
    ####
    path('Staff/Feedback', Staff_views.STAFF_FEEDBACK, name = 'Staff_feedback'),
    path('Staff/Feedback/Save', Staff_views.STAFF_FEEDBACK_SAVE, name = 'Staff_feedback_save'),
    ####
    path('Staff/Take_Attendance', Staff_views.STAFF_TAKE_ATTENDANCE, name = 'Staff_take_attendance'),

    # THIS IS FOR THE STUDENT URLS 
     path('Student/home', Student_views.HOME, name = 'Student_home'),
     ####
     path('Student/Notifications', Student_views.NOTIFICATIONS, name = 'student_notifications'),
    path('Student/Mark_as_done/<str:status>', Student_views.STUDENT_NOTIFICATION_MARK_AS_DONE, name='student_notification_mark_as_mark'),
    ####
    path('Student/Feedback', Student_views.STUDENT_FEEDBACK, name = 'Student_feedback'),
    path('Student/Feedback/Save', Student_views.STUDENT_FEEDBACK_SAVE, name = 'Student_feedback_save'),
    ####
    path('Student/Apply_Leave', Student_views.STUDENT_APPLY_LEAVE, name = 'Student_apply_leave'),
    path('Student/Apply_Leave_Save', Student_views.STUDENT_APPLY_LEAVE_SAVE, name = 'Student_apply_leave_save'),
    ####

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
