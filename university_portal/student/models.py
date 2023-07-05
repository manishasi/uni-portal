from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,Group
from django.db import models

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

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class University(models.Model):
    serial_no = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    concentration = models.CharField(max_length=100)
    website_url = models.URLField()
    campus = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    study_level = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    intakes = models.CharField(max_length=100)
    entry_requirements = models.TextField()
    ielts_score = models.DecimalField(max_digits=4, decimal_places=2)
    ielts_no_band_less_than = models.DecimalField(max_digits=4, decimal_places=2)
    toefl_score = models.PositiveIntegerField()
    toefl_no_band_less_than = models.PositiveIntegerField()
    pte_score = models.PositiveIntegerField()
    pte_no_band_less_than = models.PositiveIntegerField()
    application_deadline = models.DateField()
    yearly_tuition_fees = models.DecimalField(max_digits=10, decimal_places=2)
    backlog_range = models.CharField(max_length=50)
    remarks = models.TextField()
    application_mode = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='student_profile')
    batch = models.CharField(max_length=50)
    major = models.CharField(max_length=100)
    universities = models.ManyToManyField(University, related_name='students')
    # Add any additional fields specific to students


    def __str__(self):
        return self.user.email

class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='staff_profile')
    # Add any additional fields specific to staff members

    def __str__(self):
        return self.user.email

class Agent(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='agent_profile')
    # Add any additional fields specific to agents

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
