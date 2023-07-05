from django.contrib import admin

# Register your models here.
from .models import University,Student

class UniversityAdmin(admin.ModelAdmin):
    list_display = ['serial_no', 'name', 'concentration', 'website_url', 'campus', 'country', 'study_level', 'duration', 'intakes', 'entry_requirements', 'ielts_score', 'ielts_no_band_less_than', 'toefl_score', 'toefl_no_band_less_than', 'pte_score', 'pte_no_band_less_than', 'application_deadline', 'application_fee', 'yearly_tuition_fees', 'scholarship_available','scholarship_detail','backlog_range', 'remarks', 'esl_elp_detail', 'application_mode',' det_score']
    list_filter = ['campus', 'country', 'study_level']  # Add the fields you want to enable filtering on
    search_fields = ['name', 'country']  # Add the fields you want to enable searching on

admin.site.register(University, UniversityAdmin)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'family_name', 'email', 'university','region','preferred_language','contact_number','country_of_residence','highest_education')
    list_filter = ('university', 'nationality','region', 'onshore')
    search_fields = ('name', 'family_name', 'email', 'university__university')

