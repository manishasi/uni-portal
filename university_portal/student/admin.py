from django.contrib import admin

# Register your models here.
from .models import University,Student,AcademicAchievement,StudyPreference,LeadTracking,CampaignData,PersonalDetails

class UniversityAdmin(admin.ModelAdmin):
    list_display = ['serial_no', 'name', 'concentration', 'website_url', 'campus', 'country', 'study_level', 'duration', 'intakes', 'entry_requirements', 'ielts_score',
                    'ielts_no_band_less_than', 'toefl_score', 'toefl_no_band_less_than', 'pte_score', 'pte_no_band_less_than', 'application_deadline', 'application_fee', 'yearly_tuition_fees',
                    'scholarship_available','scholarship_detail','backlog_range', 'remarks', 'esl_elp_detail', 'application_mode','det_score']
    list_filter = ['campus', 'country', 'study_level']  # Add the fields you want to enable filtering on
    search_fields = ['name', 'country']  # Add the fields you want to enable searching on

admin.site.register(University, UniversityAdmin)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'family_name', 'email','region','preferred_language','contact_number','country_of_residence','highest_education','how_did_you_hear','status','ApplicationStage')
    list_filter = ('nationality','region', 'onshore')
    search_fields = ('name', 'family_name', 'email')

@admin.register(AcademicAchievement)
class AcademicAchievementAdmin(admin.ModelAdmin):
    list_display = ('highest_education', 'country_where_study_completed')

@admin.register(StudyPreference)
class StudyPreferenceAdmin(admin.ModelAdmin):
    list_display = ('intended_area_of_study', 'intended_course_level', 'courses_and_fields_comments','career_paths',
                    'intended_institutions', 'intended_intake_quarter', 'intended_intake_year',
                    'intended_intake_comments', 'funding_source', 'intended_destination_1',
                    'intended_destination_2', 'intended_destination_3', 'intended_destination_comments')

    # def get_courses(self, obj):
    #     return ', '.join(obj.courses.all())
    # get_courses.short_description = 'Courses'

@admin.register(LeadTracking)
class LeadTrackingAdmin(admin.ModelAdmin):
    list_display = ['id', 'lead_status', 'prospect_rating', 'preference_appointment_date', 'lead_source',
                    'candidate_comments','signup_country','signup_city','signup_state_province','signup_ip']

@admin.register(PersonalDetails)
class PersonalDetailsAdmin(admin.ModelAdmin):
    list_display = ('address_1','address_2', 'city','state_province','country','postcode_zipcode', 
                    'date_of_birth','marital_status','timezone','currency','image')

@admin.register(CampaignData)
class CampaignDataAdmin(admin.ModelAdmin):
    list_display = ['lead_id', 'campaign_id', 'campaign_name', 'form_id', 'form_name', 'ad_id', 'ad_name']

