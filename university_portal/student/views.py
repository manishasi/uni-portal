from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import pandas as pd
from datetime import date, datetime
import math
from .models import University

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
            
            # Check if TOEFL Score is a number, otherwise assign None
            toefl_score = row.get('TOEFL Score')
            if not isinstance(toefl_score, (int, float)) or math.isnan(toefl_score):
                toefl_score = None

            # Check if TOEFL No Band Less Than is a number, otherwise assign None
            toefl_no_band_less_than = row.get('TOEFL No Band Less Than')
            if not isinstance(toefl_no_band_less_than, (int, float)) or math.isnan(toefl_no_band_less_than):
                toefl_no_band_less_than = None
            
            # Check if PTE Score is a number, otherwise assign None
            pte_score = row.get('PTE Score')
            if not isinstance(pte_score, (int, float)) or math.isnan(pte_score):
                pte_score = None

            # Check if PTE No Band Less Than is valid, otherwise assign default value
            pte_no_band_less_than = row.get('PTE No Band Less Than')
            if not pte_no_band_less_than:
                pte_no_band_less_than = ""  # or None, or any other default value

            # Convert scholarship_available to boolean
            scholarship_available = row.get('Scholarship Available')
            if scholarship_available == "Yes":
                scholarship_available = True
            else:
                scholarship_available = False

            # Get the value from the row
            application_deadline = row.get('Application deadline')
            # Check if the value is a string
            if isinstance(application_deadline, str):
                try:
                    # Try to convert it to a date object
                    application_deadline = date.fromisoformat(application_deadline)
                except ValueError:
                    # Handle the case where the string is not in the correct format
                    print(f"Invalid date format: {application_deadline}")
                    application_deadline = None
            # Check if it is already a datetime object
            elif isinstance(application_deadline, datetime):  # Notice here, we use datetime directly
                # Extract the date part
                application_deadline = application_deadline.date()
            else:
                # Handle other cases (e.g., if it's None or an unexpected type)
                application_deadline = None


            backlog_range = row.get('Backlog Range')
            if backlog_range is None:
                # Handle the case, either set a default value or skip the record
                backlog_range = "default_value"  # Set a default value
                # or skip this record
                
            ielts_score = row.get('IELTS Score')
            # Check if ielts_score is a float and if it is NaN
            if isinstance(ielts_score, float) and math.isnan(ielts_score):
                ielts_score = None  # or assign some default value

            # You can perform similar checks for other fields if necessary
            university = University(
                serial_no=row.get('Serial No.'),
                name=row.get('Name'),
                concentration=row.get('Concentration'),
                website_url=row.get('Website URL'),
                campus=row.get('Campus'),
                country=row.get('Country'),
                study_level=row.get('Study Level'),
                duration=row.get('Duration'),
                intakes=row.get('Intakes'),
                entry_requirements=row.get('Entry Requirements'),
                ielts_score=ielts_score,
                ielts_no_band_less_than=row.get('IELTS No Band Less Than'),
                toefl_score=toefl_score,  # Use the validated toefl_score value
                toefl_no_band_less_than=toefl_no_band_less_than,  # Use the validated toefl_no_band_less_than value
                pte_score=pte_score,  # Use the validated pte_score value
                pte_no_band_less_than=pte_no_band_less_than,
                application_deadline=application_deadline,
                application_fee=row.get('Application fee'),
                yearly_tuition_fees=row.get('Yearly Tuition Fees'),
                scholarship_available=scholarship_available,
                scholarship_detail=row.get('Scholarship Detail'),
                backlog_range=backlog_range,
                remarks=row.get('Remarks'),
                esl_elp_detail=row.get('ESL/ELP Detail'),
                application_mode=row.get('ApplicationMode'),
                application=row.get('Application'),
                det_score=row.get('DET Score')
            )
            university.save()

    return HttpResponse("Done")
