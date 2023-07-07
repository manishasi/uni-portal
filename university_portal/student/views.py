from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import pandas as pd
# import numpy as np
from .models import University
from datetime import datetime

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

            university = University(
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
                scholarship_available=row.get('Scholarship Available'),
                scholarship_detail=row.get('Scholarship Detail'),
                backlog_range=row.get('Backlog Range'),
                remarks=row.get('Remarks'),
                esl_elp_detail=row.get('ESL/ELP Detail'),
                application_mode=row.get('ApplicationMode'),
                # application=row.get('Application'),
                # det_score=row.get('DET Score')
            )

            # Call the set_scholarship_available method
            scholarship_value = row.get('Scholarship Available')
            university.set_scholarship_available(scholarship_value)

            university.save()

    return HttpResponse("Data uploaded successfully")