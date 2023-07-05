from django.db import models

# Create your models here.

class User(models.Model):
    ADMIN = 'admin'
    AGENT = 'agent'
    STUDENT = 'student'
    SUPERUSER = 'superuser'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (AGENT, 'Agent'),
        (STUDENT, 'Student'),
        (SUPERUSER, 'Superuser'),
    ]

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.name


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
    serial_no = models.IntegerField()
    name = models.CharField(max_length=100)
    concentration = models.CharField(max_length=100)
    website_url = models.URLField()
    campus = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    study_level = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    intakes = models.CharField(max_length=100)
    entry_requirements = models.TextField()
    ielts_score = models.DecimalField(max_digits=4, decimal_places=2)
    ielts_no_band_less_than = models.DecimalField(max_digits=4, decimal_places=2)
    toefl_score = models.IntegerField()
    toefl_no_band_less_than = models.IntegerField()
    pte_score = models.IntegerField()
    pte_no_band_less_than = models.CharField(max_length=10)
    application_deadline = models.DateField(null=True)
    application_fee = models.DecimalField(max_digits=10, decimal_places=2 ,null=True)
    yearly_tuition_fee = models.DecimalField(max_digits=10, decimal_places=2)
    scholarship_available = models.BooleanField(default=False ,null=True)
    scholarship_detail = models.TextField(blank=True ,null=True)
    backlog_range = models.CharField(max_length=100, blank=True)
    remarks = models.TextField(blank=True)
    esl_elp_detail = models.TextField(blank=True ,null=True)
    application_mode = models.CharField(max_length=100 ,null=True)
    application = models.CharField(max_length=100,null=True)
    det_score = models.IntegerField()
    
    def __str__(self):
        return self.name


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
    University= models.ManyToManyField("University")
    name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    nationality=models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    onshore = models.BooleanField()
    preferred_language = models.CharField(max_length=50)
    contact_number = models.IntegerField()
    country_of_residence=models.CharField(max_length=50)
    highest_education=models.CharField(max_length=50)
    how_did_you_hear = models.CharField(max_length=100, choices=REFERRAL_CHOICES)
   

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

    what_is_your_highest_level_of_education = models.CharField(max_length=50, choices=HIGHEST_EDUCATION_CHOICES)
    country_where_study_completed = models.CharField(max_length=100)


class StudyPreference(models.Model):
    # INTENDED_COURSE_LEVEL_CHOICES = (
    #     ('undergraduate', 'Undergraduate'),
    #     ('postgraduate', 'Postgraduate'),
    #     ('diploma', 'Diploma'),
    #     ('certificate', 'Certificate'),
    #     ('language', 'Language Program'),
    #     ('foundation', 'Foundation Program'),
    # )

    intended_area_of_study = models.CharField(max_length=100)
    # intended_course_level = models.CharField(max_length=50, choices=INTENDED_COURSE_LEVEL_CHOICES)
    intended_course_level = models.CharField(max_length=50)
    courses_and_fields_comments = models.TextField()
    career_paths = models.TextField()
    intended_institutions = models.TextField()
    intended_intake_quarter = models.CharField(max_length=50)
    intended_intake_year = models.IntegerField()
    intended_intake_comments = models.TextField()
    funding_source = models.CharField(max_length=100)
    intended_destination_1 = models.CharField(max_length=100)
    intended_destination_2 = models.CharField(max_length=100)
    intended_destination_3 = models.CharField(max_length=100)
    intended_destination_comments = models.TextField()