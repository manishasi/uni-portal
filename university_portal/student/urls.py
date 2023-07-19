from django.urls import path
from . import views


urlpatterns = [
    path('', views.upload_university_data,name='upload_university_data'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('logout/', views.logout_view, name='logout'),
    
    
    path('staff/', views.staff_dashboard, name='staff-dashboard'),
    path('staff-profile/', views.staff_profile, name='staff-profile'),
    path('sign-up-agent/', views.sign_up_agent, name='sign-up-agent'),
    
    
    path('agent/', views.agent_dashboard, name='agent-dashboard'),
    path('agent-profile/', views.agent_profile, name='agent-profile'),
    path('sign-up-student/', views.sign_up_student, name='sign-up-student'),
    
    path('student/', views.student_dashboard, name='student-dashboard'),
    # path('student-profile/', views.student_profile, name='student-profile'),
    
    path('active-students/', views.active_students, name='active-students'),
    path('unassigned-students/', views.unassigned_students, name='unassigned-students'),
    
    path('country/', views.country, name='country'),
    path('country/<str:country>/', views.country_detail, name='country_detail'),
    
    
    # path('fake',views.fake_data,name='fake_data')
]