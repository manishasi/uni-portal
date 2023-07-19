from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
#import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from .models import University,Staff, Agent,Student
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
# from .forms import SignUpForm, SignInForm
from django.contrib import messages
from .models import CustomUser
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
import pycountry
# from datetime import datetime

def upload_university_data(filepath):
    # Read the Excel file into a pandas ExcelFile object
    filepath = r"C:\Users\Manisha Singh\Downloads\Australia(1).xlsx"
    xls = pd.ExcelFile(filepath)

    # Iterate over each sheet in the Excel file
    for sheet_name in xls.sheet_names:
        # Read the sheet into a pandas DataFrame
        df = xls.parse(sheet_name)

        # Iterate over each row in the DataFrame
        for index, row in df.iterrows():

            raw_serial_no = row.get('Serial No.')
            # Check if raw_serial_no is nan, and if so, set it to None
            if pd.isna(raw_serial_no):
                serial_no = None
            else:
                serial_no = raw_serial_no

            university,created = University.objects.update_or_create(
                # serial_no=row.get('Serial No.'),
                serial_no=serial_no,
                university=row.get('University'),
                name=row.get('Name'),
                concentration=row.get('Concentration'),
                website_url=row.get('Website URL'),
                campus=row.get('Campus'),
                country=row.get('Country'),
                study_level=row.get('Study Level'),
                duration=row.get('Duration'),
                intakes=row.get('Intakes'),
                entry_requirements=row.get('Entry Requirements'),
                ielts_score=row.get('IELTS Score'),
                ielts_no_band_less_than=row.get('IELTS No Band Less Than'),
                toefl_score=row.get('TOEFL Score'),
                toefl_no_band_less_than=row.get('TOEFL No Band Less Than'),
                pte_score=row.get('PTE Score'),
                pte_no_band_less_than=row.get('PTE No Band Less Than'),
                application_deadline=row.get('Application deadline'),
                # application_deadline=application_deadline,
                application_fee=row.get('Application fee'),
                yearly_tuition_fees=row.get('Yearly Tuition Fees'),
                # scholarship_available=row.get('Scholarship Available'),
                scholarship_detail=row.get('Scholarship Detail'),
                backlog_range=row.get('Backlog Range'),
                remarks=row.get('Remarks'),
                esl_elp_detail=row.get('ESL/ELP Detail'),
                application_mode=row.get('ApplicationMode'),
                # application=row.get('Application'),
                # det_score=row.get('DET Score')
            )
            if created:
                scholarship_value = row.get('Scholarship Available')
                university.set_scholarship_available(scholarship_value)

                university.save()

    return HttpResponse("Data uploaded successfully")


# @csrf_exempt
# def sign_in(request):
#     if request.method == 'POST':
#         user_type = request.POST.get('user_type')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         users = CustomUser.objects.filter(email=email, user_type=user_type)
#         if users.exists():
#             user = users.first()
#             if user.check_password(password):
#                 if user_type == 'staff':
#                     # Credentials are valid, log in the staff user
#                     login(request, user)
#                     return redirect('staff-dashboard')
#                 elif user_type == 'agent':
#                     try:
#                         # Check if the user is an agent
#                         agent = Agent.objects.get(user=user)
#                         # Credentials are valid, log in the agent
#                         login(request, user)
#                         return redirect('agent-dashboard')
#                     except Agent.DoesNotExist:
#                         # User is not an agent, display error message
#                         error_message = 'Invalid email or user type'
#                         messages.error(request, error_message)
#                 elif user_type == 'student':
#                     try:
#                         # Check if the user is a student
#                         student = Student.objects.get(user=user)
#                         # Credentials are valid, log in the student
#                         login(request, user)
#                         return redirect('student-dashboard')
#                     except Student.DoesNotExist:
#                         # User is not a student, display error message
#                         error_message = 'Invalid email or user type'
#                         messages.error(request, error_message)
#             else:
#                 # Invalid password, display error message
#                 error_message = 'Invalid password'
#                 messages.error(request, error_message)
#         else:
#             # User does not exist, display error message
#             error_message = 'Invalid email or user type'
#             messages.error(request, error_message)

#     return render(request, 'student/sign-in.html')





@csrf_exempt
def sign_in(request):
    if request.method == 'POST':
        # import pdb
        # pdb.set_trace()
        user_type = request.POST.get('user_type')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,"--------------username--------------")
        print(password,"--------------password--------------")
        print(user_type,"-------------user_type-------------")
        

        users = CustomUser.objects.filter(email=email, user_type=user_type)
        print(users,"--------------users--------------")
        # users.set_password(password)
        if users.exists():
            user = users.first()
            print(user,"--------------user_first--------------")  
            
            if user.check_password(password):
                print("password check kiya ")
                # Credentials are valid, log in the user
                login(request, user)
                print(user_type,"--------------user_type--------------")
                # Redirect to the appropriate dashboard based on user type
                if user_type == 'staff':
                    
                    return redirect('staff-dashboard')
                elif user_type == 'agent':
                    return redirect('agent-dashboard')
                elif user_type == 'student':
                    return redirect('student-dashboard')
            else:

                # Invalid password, display error message
            
                error_message = 'Invalid password'
                messages.error(request, error_message)
        else:
            # User does not exist, display error message
            error_message = 'Invalid email or user type'
            messages.error(request, error_message)

    return render(request, 'student/sign-in.html')

def logout_view(request):
    logout(request)
    return render(request, 'student/sign-in.html') 

@login_required(login_url='sign-in')  # Add this decorator to enforce login requirement
def staff_dashboard(request):
    if request.user.user_type == 'staff':
        try:
            staff = Staff.objects.get(user=request.user)
            # You can access the staff's fields like staff.agent, staff.user, etc.
            context = {
                'staff': staff
            }
            return render(request, 'student/staff_dashboard.html', context)
        except ObjectDoesNotExist:
            # Handle the case when Staff object does not exist for the current user
            error_message = 'You are not authorized to access the staff dashboard.'
            return render(request, 'student/staff_dashboard.html', {'error_message': error_message})
    else:
        error_message = 'You are not authorized to access the staff dashboard.'
        return render(request, 'student/staff_dashboard.html', {'error_message': error_message})


@login_required(login_url='sign-in')
def staff_profile(request):
    if request.user.user_type == 'staff':
        try:
            staff = Staff.objects.get(user=request.user)
            # You can access the staff's fields like staff.agent, staff.user, etc.
            context = {
                'staff': staff
            }
            return render(request, 'student/staff_profile.html', context)
        except Staff.DoesNotExist:
            # Handle the case when Staff object does not exist for the current user
            error_message = 'Staff profile not found.'
            return render(request, 'student/staff_profile.html', {'error_message': error_message})
    else:
        error_message = 'You are not authorized to access the staff profile.'
        return render(request, 'student/staff_profile.html', {'error_message': error_message})

def sign_up_agent(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('sign-up-agent')  # Replace 'sign_up' with the URL name for the sign-up page

        # Check if an agent with the same email already exists
        if CustomUser.objects.filter(email=email, user_type='agent').exists():
            messages.error(request, "Agent with this email already exists")
            return redirect('sign-up-agent')  # Replace 'sign_up' with the URL name for the sign-up page

        # Create a new CustomUser object with user_type='agent'
        user = CustomUser.objects.create(email=email, user_type='agent',password=password)
        user.set_password(password)
        agent= Agent.objects.create(user=user)
        return redirect('staff-dashboard')
        
    return render(request, 'student/sign-up-agent.html')


@login_required(login_url='sign-in')
def agent_dashboard(request):
    if request.user.user_type == 'agent':
        try:
            agent = Agent.objects.get(user=request.user)
            # You can access the agent's fields like agent.agent, agent.user, etc.
            context = {
                'agent': agent
            }
            return render(request, 'student/agent_dashboard.html', context)
        except ObjectDoesNotExist:
            # Handle the case when agent object does not exist for the current user
            error_message = 'You are not authorized to access the agent dashboard.'
            return render(request, 'student/agent_dashboard.html', {'error_message': error_message})
    else:
        error_message = 'You are not authorized to access the agent dashboard.'
        return render(request, 'student/agent_dashboard.html', {'error_message': error_message})
    

@login_required(login_url='sign-in')
def agent_profile(request):
    if request.user.user_type == 'agent':
        try:
            agent = Agent.objects.get(user=request.user)
            # You can access the staff's fields like agent.agent, agent.user, etc.
            context = {
                'agent': agent
            }
            return render(request, 'student/agent_profile.html', context)
        except Agent.DoesNotExist:
            # Handle the case when agent object does not exist for the current user
            error_message = ' profile not found.'
            return render(request, 'student/agent_profile.html', {'error_message': error_message})
    else:
        error_message = 'You are not authorized to access the agent profile.'
        return render(request, 'student/agent_profile.html', {'error_message': error_message})

def sign_up_student(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('sign-up-student')  # Replace 'sign_up' with the URL name for the sign-up page

        # Check if an agent with the same email already exists
        if CustomUser.objects.filter(email=email, user_type='student').exists():
            messages.error(request, "Student with this email already exists")
            return redirect('sign-up-student')  # Replace 'sign_up' with the URL name for the sign-up page
    
        # Create a new CustomUser object with user_type='student'
        user = CustomUser.objects.create(email=email, user_type='student',password=password)
        user.set_password(password)
        # user.save()
        student= Student.objects.create(user=user)
        
        return redirect('agent-dashboard')
        
    return render(request, 'student/sign-up-student.html')


@login_required(login_url='sign-in')
def student_dashboard(request):
    if request.user.user_type == 'student':
        try:
            student = Student.objects.get(user=request.user)
            # You can access the agent's fields like student.student, studemt.user, etc.
            search_query = request.GET.get('search')
            if search_query:
                students = students.filter(name__icontains=search_query)
            
            # Check for the status filtering
            status = request.GET.get('status')
            if status == 'active':
                students = Student.objects.filter(status='active')
            elif status == 'unassigned':
                students = Student.objects.filter(status='unassigned')
            else:
                students = None

            context = {
                'student': student,
                'students': students,
                'selected_status': status,
                'search_query': search_query
            }
            
            # context = {
            #     'student': student
            # }
            return render(request, 'student/student_dashboard.html', context)
        except ObjectDoesNotExist:
            # Handle the case when student object does not exist for the current user
            error_message = 'You are not authorized to access the student dashboard.'
            return render(request, 'student/student_dashboard.html', {'error_message': error_message})
    else:
        error_message = 'You are not authorized to access the student dashboard.'
        return render(request, 'student/student_dashboard.html', {'error_message': error_message})


def country(request):
    # countries = University.objects.filter(country=country)
    countries = University.objects.values_list('country', flat=True).distinct()
    
    context = {
        'countries': countries
    } 
    return render(request, 'student/country.html', context)
    
    
def country_detail(request, country):
    universities = University.objects.filter(country=country)
    
    context = {
        'country': country,
        'universities': universities
    } 
    return render(request, 'student/country_detail.html', context)

def active_students(request):
    students = Student.objects.filter(status='active')
    context = {
        'students': students,
        'selected_status': 'active'
    }
    return render(request, 'student/staff_dashboard.html', context)

def unassigned_students(request):
    students = Student.objects.filter(status='unassigned')
    context = {
        'students': students,
        'selected_status': 'unassigned'
    }
    return render(request, 'student/staff_dashboard.html', context)



# from django.db import models
# from django.contrib.auth.models import User
# from faker import Faker
# import random

# fake = Faker()
# def fake_data(request): 
# # Generate fake data for Student model
#     for _ in range(100):
#         user = CustomUser.objects.create_user(
#             password='password',
#             email=fake.email(),
#             user_type='student'
#         )
#         student = Student.objects.create(
#             user=user,
#             name=fake.first_name(),
#             family_name=fake.last_name(),
#             email=user.email,
#             nationality=fake.country(),
#             region=fake.city(),
#             onshore=random.choice([True, False]),
#             preferred_language=fake.language_name(),
#             contact_number=fake.phone_number(),
#             country_of_residence=fake.country(),
#             highest_education=random.choice(['High School', 'Bachelor', 'Master', 'PhD']),
#             how_did_you_hear=random.choice(['social/facebook', 'social/instagram', 'eDm', 'expo', 'referral']),
#             status=random.choice(['active', 'unassigned', 'inactive','completed', 'paused']),
#             ApplicationStage=random.choice(['submitted', 'lodged', 'offers_received', 'visas_granted', 'students_commenced', 'students_deferred'])
#         )
#     return "Done!"