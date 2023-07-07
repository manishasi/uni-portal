from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,Group
from django.db import models
from datetime import date
# from .custom_user import CustomUser
from pytz import all_timezones
import pycountry



class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('user_type', 'superadmin')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    USER_TYPE_CHOICES = (
        ('superadmin', 'Super Admin'),
        ('staff', 'Staff'),
        ('agent', 'Agent'),
        ('student', 'Student'),
    )

    email = models.EmailField(unique=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        # Simplest permission check is superuser status
        return self.is_superuser

    def has_module_perms(self, app_label):
        # Allow access to the app section of the admin site for superusers
        return self.is_superuser

# class University(models.Model):
    # UNIVERSITY_CHOICES = [
    #     ('University of Tasmania', 'University of Tasmania'),
    #     ('Curtin University', 'Curtin University'),
    #     ('Swinburne University - Malaysia', 'Swinburne University - Malaysia'),
    #     ('University of Wollongong - Dubai', 'University of Wollongong - Dubai'),
    #     ('James Cook University (JCU) - Singapore', 'James Cook University (JCU) - Singapore'),
    #     ('Kaplan Business School', 'Kaplan Business School'),
    #     ('Excelsia College', 'Excelsia College'),
    #     ('Monash University', 'Monash University'),
    #     ('University of New South Wales, Sydney', 'University of New South Wales, Sydney'),
    #     ('University of Western Australia', 'University of Western Australia'),
    #     ('La Trobe College', 'La Trobe College'),
    #     ('The University of Queensland', 'The University of Queensland'),
    #     ('Kaplan Higher Education Academy (KHEA)', 'Kaplan Higher Education Academy (KHEA)'),
    #     ('University of South Australia', 'University of South Australia'),
    #     ('Flinders University', 'Flinders University'),
    #     ('Macquarie University', 'Macquarie University'),
    #     ('Western Sydney University, Paramatta', 'Western Sydney University, Paramatta'),
    #     ('Southern Cross University, Lismore and Coffs Harbour', 'Southern Cross University, Lismore and Coffs Harbour'),
    #     ('Deakin University', 'Deakin University'),
    #     ('Australian Catholic University, North Sydney and Strathfield', 'Australian Catholic University, North Sydney and Strathfield'),
    #     ('Queensland University of Technology', 'Queensland University of Technology'),
    # ]
    # university_choice = models.CharField(max_length=100, choices=UNIVERSITY_CHOICES)
class University(models.Model):
    serial_no = models.IntegerField(null=True, blank=True)
    university = models.CharField(max_length=100,blank=True,null=True)
    name = models.CharField(max_length=100,blank=True,null=True)
    concentration = models.CharField(max_length=100,blank=True,null=True)
    website_url = models.URLField()
    campus = models.CharField(max_length=100,blank=True,null=True)
    country = models.CharField(max_length=100,blank=True,null=True)
    study_level = models.CharField(max_length=100,blank=True,null=True)
    duration = models.CharField(max_length=100,blank=True,null=True)
    intakes = models.CharField(max_length=100,blank=True,null=True)
    entry_requirements = models.TextField(blank=True,null=True)
    ielts_score = models.FloatField(null=True,blank=True)
    ielts_no_band_less_than = models.FloatField(null=True,blank=True)
    toefl_score = models.FloatField(blank=True, null=True)
    toefl_no_band_less_than = models.FloatField(blank=True,null=True)
    pte_score = models.FloatField(blank=True, null=True)
    pte_no_band_less_than = models.CharField(max_length=10,null=True,blank=True)
    application_deadline = models.CharField(max_length=10,null=True,blank=True)
    application_fee = models.CharField(max_length=100,blank=True,null=True)
    yearly_tuition_fees = models.CharField(max_length=100,blank=True,null=True)
    scholarship_available = models.BooleanField(default=False,null=True)
    scholarship_detail = models.TextField(blank=True,null=True)
    backlog_range = models.CharField(max_length=100,blank=True,null=True)
    remarks = models.TextField(blank=True,null=True)
    esl_elp_detail = models.TextField(blank=True,null=True)
    application_mode = models.CharField(max_length=100,null=True)
    # application = models.CharField(max_length=100,null=True)
    # det_score = models.FloatField(blank=True,null=True)
    
    def __str__(self):
        return self.name
    
    def set_scholarship_available(self, value):
        if str(value).lower() == "yes":
            self.scholarship_available = True
        elif str(value).lower() == "no":
            self.scholarship_available = False
        else:
            self.scholarship_available = None

   
class Student(models.Model):
    REFERRAL_CHOICES = (
        ('social/facebook', 'Social Media (Facebook)'),
        ('social/instagram', 'Social Media (Instagram)'),
        ('social/tiktok', 'Social Media (TikTok)'),
        ('eDm', 'Email Marketing (EDM)'),
        ('expo', 'Expo or Event'),
        ('referral', 'Referral'),
        ('websearch', 'Web Search'),
        ('advertising/print', 'Advertising (Print)'),
        ('advertising/tv', 'Advertising (TV)'),
        ('advertising/cinema', 'Advertising (Cinema)'),
        ('advertising/radio', 'Advertising (Radio)'),
        ('advertising/outdoor', 'Advertising (Outdoor)'),
        ('advertising/online', 'Advertising (Online)'),
        ('school', 'School'),
        ('other', 'Other'),
    )
    University= models.ManyToManyField(University,related_name='students')
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    name = models.CharField(max_length=100,null= True,blank=True)
    family_name = models.CharField(max_length=100,null= True,blank=True)
    email = models.EmailField(max_length=254,null= True,blank=True)
    nationality=models.CharField(max_length=100,null= True,blank=True)
    region = models.CharField(max_length=50,null= True,blank=True)
    onshore = models.BooleanField(default=False)
    preferred_language = models.CharField(max_length=50,null= True,blank=True)
    contact_number = models.CharField(max_length=12,null= True,blank=True)
    country_of_residence=models.CharField(max_length=50,null= True,blank=True)
    highest_education=models.CharField(max_length=50,null= True,blank=True)
    created_at= models.DateField(auto_now_add=True,null= True,blank=True)
    how_did_you_hear = models.CharField(max_length=100, choices=REFERRAL_CHOICES)
    status=models.CharField(max_length=50,null= True,blank=True)
    STAGE_CHOICES = (
        ('submitted', 'Submitted to Adventus'),
        ('lodged', 'Lodged with Institutions'),
        ('offers_received', 'Offers Received'),
        ('visas_granted', 'Visas Granted'),
        ('students_commenced', 'Students Commenced'),
        ('students_deferred', 'Students Deferred'),
    )
    ApplicationStage = models.CharField(max_length=100, choices=STAGE_CHOICES, default='')

    def __str__(self):
        return self.user.email
    
    # def get_user_email(self):
    #     return self.user.email
    
class Agent(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='agent_profile')
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    messages = models.TextField(blank=True ,null=True)
    tasks = models.CharField(max_length=50,null=True, blank=True)
    timeline = models.CharField(max_length=50,null=True, blank=True)
    owner = models.CharField(max_length=50,null=True, blank=True)
    phase = models.CharField(max_length=50,null=True, blank=True)
    action = models.CharField(max_length=50,null=True, blank=True)
    active_team =models.CharField(max_length=50,null=True, blank=True)
    notes = models.TextField(blank=True ,null=True)
    # Add any additional fields specific to agents

    def __str__(self):
        return self.user.email

class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='staff_profile')
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE)
    # Add any additional fields specific to staff members

    def __str__(self):
        return self.user.email

# Create groups for each user type and assign appropriate permissions
group_superadmin, _ = Group.objects.get_or_create(name='Super Admin')
group_staff, _ = Group.objects.get_or_create(name='Staff')
group_agent, _ = Group.objects.get_or_create(name='Agent')
group_student, _ = Group.objects.get_or_create(name='Student')

# Assign permissions to groups
# Example permissions - replace with actual permissions based on your requirements
group_superadmin.permissions.add(
    # List of permissions for the super admin group
)

group_staff.permissions.add(
    # List of permissions for the staff group
)

group_agent.permissions.add(
    # List of permissions for the agent group
)

group_student.permissions.add(
    # List of permissions for the student group
)

class StudentApplication(models.Model):
    student= models.ManyToManyField(Student)
    application_id=models.IntegerField(null=True, blank=True)
    application_status = models.CharField(max_length=50,null=True, blank=True)
    save_date = models.DateField(auto_now=False, auto_now_add=False)
    shortlisted_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    first_submitted = models.DateField(auto_now=False, auto_now_add=False)
    declaration = models.BooleanField(default=False)
    medical_condition = models.BooleanField(default=False)


class AcademicAchievement(models.Model):
    HIGHEST_EDUCATION_CHOICES = (
        ('highschool', 'High School'),
        ('language_pathway', 'Language Pathway'),
        ('undergraduate-foundation', 'Undergraduate Foundation'),
        ('undergraduate-certificate', 'Undergraduate Certificate'),
        ('undergraduate-diploma', 'Undergraduate Diploma'),
        ('undergraduate-associate_degree', 'Undergraduate Associate Degree'),
        ('undergraduate-bachelor', 'Undergraduate Bachelor'),
        ('postgraduate-certificate', 'Postgraduate Certificate'),
        ('postgraduate-diploma', 'Postgraduate Diploma'),
        ('masters', 'Master\'s Degree'),
        ('doctrate_phd', 'Doctorate/PhD'),
    )
    student= models.ForeignKey(Student,on_delete=models.CASCADE)
    highest_education = models.CharField(max_length=50, choices=HIGHEST_EDUCATION_CHOICES)
    country_where_study_completed = models.CharField(max_length=100,null=True, blank=True)
    start_date = models.DateField(default=date.today)
    # school_institute_name = models.CharField(max_length=50)
    school_institute_name = models.CharField(max_length=100, null=True, blank=True)
    completed_date = models.DateField(default=date.today)
    title_of_your_course = models.CharField(max_length=50,null=True, blank=True)
    result = models.FloatField(default=0.0,null=True, blank=True)

    def __str__(self):
        return f"Highest Education: {self.highest_education}"

class StudyPreference(models.Model):
    student= models.ForeignKey(Student,on_delete=models.CASCADE)
    intended_area_of_study = models.CharField(max_length=100,null=True, blank=True)
    # intended_course_level = models.CharField(max_length=50, choices=INTENDED_COURSE_LEVEL_CHOICES)
    intended_course_level = models.CharField(max_length=50,null=True, blank=True)
    courses_and_fields_comments = models.TextField(null=True, blank=True)
    career_paths = models.TextField(null=True, blank=True)
    intended_institutions = models.TextField(null=True, blank=True)
    intended_intake_quarter = models.CharField(max_length=50,null=True, blank=True)
    intended_intake_year = models.IntegerField(null=True, blank=True)
    intended_intake_comments = models.TextField(null=True, blank=True)
    funding_source = models.CharField(max_length=100,null=True, blank=True)
    intended_destination_1 = models.CharField(max_length=100,null=True, blank=True)
    intended_destination_2 = models.CharField(max_length=100,null=True, blank=True)
    intended_destination_3 = models.CharField(max_length=100,null=True, blank=True)
    intended_destination_comments = models.TextField(null=True, blank=True)

class LeadTracking(models.Model):
    LEAD_STATUS_CHOICES = (
        ('cold', 'Cold'),
        ('warm', 'Warm'),
        ('hot', 'Hot'),
        ('pending', 'Pending'),
    )

    PROSPECT_RATING_CHOICES = (
        ('not_rated', 'Not Rated'),
        ('1_star', '1 Star'),
        ('2_star', '2 Star'),
        ('3_star', '3 Star'),
    )
    student= models.ForeignKey(Student,on_delete=models.CASCADE)
    # agent = models.ForeignKey(Agent,on_delete=models.CASCADE)
    lead_status = models.CharField(max_length=50, choices=LEAD_STATUS_CHOICES)
    prospect_rating = models.CharField(max_length=50, choices=PROSPECT_RATING_CHOICES)
    preference_appointment_date = models.DateTimeField(null=True, blank=True)
    lead_source = models.CharField(max_length=100,null=True, blank=True)
    candidate_comments = models.TextField(null=True, blank=True)
    signup_country = models.CharField(max_length=100,null=True, blank=True)
    signup_city = models.CharField(max_length=100,null=True, blank=True)
    signup_state_province = models.CharField(max_length=100,null=True, blank=True)
    signup_ip = models.GenericIPAddressField(null=True, blank=True)

class PersonalDetails(models.Model):
    student= models.ForeignKey(Student,on_delete=models.CASCADE)
    address_1 = models.CharField(max_length=100,null=True, blank=True)
    address_2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100,null=True, blank=True)
    state_province = models.CharField(max_length=100,null=True, blank=True)
    country = models.CharField(max_length=100,null=True, blank=True)
    postcode_zipcode = models.CharField(max_length=20,null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    marital_status = models.CharField(max_length=50,null=True, blank=True)
    # timezone = models.CharField(max_length=100,null=True, blank=True)
    timezone = models.CharField(max_length=32,choices=[(tz, tz) for tz in all_timezones],blank=True,null=True)
    # currency = models.CharField(max_length=50,null=True, blank=True)
    CURRENCY_CHOICES = [(currency.alpha_3, currency.name) for currency in pycountry.currencies]
    currency = models.CharField(max_length=3,choices=CURRENCY_CHOICES,blank=True,null=True)
    image = models.ImageField(upload_to='personal_images/')

class CampaignData(models.Model):
    student= models.ForeignKey(Student,on_delete=models.CASCADE)
    lead_id = models.IntegerField(null=True, blank=True)
    campaign_id = models.IntegerField(null=True, blank=True)
    campaign_name = models.CharField(max_length=100,null=True, blank=True)
    form_id = models.IntegerField(null=True, blank=True)
    form_name = models.CharField(max_length=100,null=True, blank=True)
    ad_id = models.IntegerField(null=True, blank=True)
    ad_name = models.CharField(max_length=100,null=True, blank=True)
