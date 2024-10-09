import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Function to generate email address
def generate_email(full_name):
    return f"{full_name.lower().replace(' ', '.')}@fgcilorin.edu.ng"

# Function to create random dates
def random_dates(start, end, n=10):
    return [start + timedelta(days=random.randint(0, (end - start).days)) for _ in range(n)]

# Function to create student data
def create_student_data():
    first_names = ['Chidi', 'Aisha', 'Emeka', 'Fatima', 'Tunde', 'Joy', 'Samuel', 'Olivia', 'Ibrahim', 'Amina']
    last_names = ['Okafor', 'Adedayo', 'Ibrahim', 'Abdullahi', 'John', 'Doe', 'Smith', 'Ali', 'Khan', 'Lee']
    students = []
    
    for i in range(300):
        full_name = f"{random.choice(first_names)} {random.choice(last_names)}"
        date_of_birth = random.choice(random_dates(datetime(2005, 1, 1), datetime(2006, 12, 31)))
        arm = 'A' if i < 100 else 'B' if i < 200 else 'C'
        current_class = 'SS3'
        discipline = 'Art' if arm == 'A' else 'Science' if arm == 'B' else 'Commercial'
        boarding_status = random.choice(['Day Student', 'Boarder'])
        
        students.append({
            'student_id': 1001 + i,
            'admission_number': f"JS1{arm}/2019/{str(i+1).zfill(3)}",
            'full_name': full_name,
            'date_of_birth': date_of_birth.strftime('%Y-%m-%d'),
            'gender': random.choice(['Male', 'Female']),
            'join_date': '2019-09-15',
            'join_class': f"JS1{arm}",
            'current_class': f"SS3{discipline[0]}",
            'discipline': discipline,
            'graduation_date': '2024-07-15',
            'state_of_origin': random.choice(['Lagos', 'Abuja', 'Kano', 'Oyo', 'Rivers']),
            'religion': random.choice(['Christianity', 'Islam']),
            'boarding_status': boarding_status,
            'scholarship_type': random.choice([None, 'Merit', 'Need-based']),
            'health_information': random.choice(['Healthy', 'Asthma', 'Vision Impairment']),
            'distance_to_school_km': None if boarding_status == 'Boarder' else round(random.uniform(1, 20), 2),
            'transport_mode': None if boarding_status == 'Boarder' else random.choice(['Bus', 'Bicycle', 'Walk']),
            'family_id': 5001 + (i % 100),
        })

    return pd.DataFrame(students)

# Function to create academic performance data


# Function to create staff data with real Nigerian names and non-teaching staff
def create_staff_data():
    staff = []
    teaching_staff_names = [
        'Adebayo Adewale', 'Chinaza Nwachukwu', 'Fatimah Yusuf', 'Oluwakemi Okafor', 'Chidera Ikechukwu',
        'Emmanuel Obi', 'Aisha Mohammed', 'Oluwaseun Olagunju', 'Ibrahim Ali', 'Oluwatosin Onabanjo'
    ]
    non_teaching_staff_names = [
        'Bola Adediran', 'Maryam Bello', 'Adeola Afolabi', 'Halima Lawal', 'Gbenga Ojo'
    ]
    
    subjects = [
        'English Language', 'Mathematics', 'Basic Science', 'Basic Technology', 'Social Studies', 'Civic Education', 
        'Physics', 'Chemistry', 'Biology', 'Literature-in-English', 'Government', 'History', 
        'Financial Accounting', 'Commerce', 'Economics'
    ]
    
    staff_id = 201
    for subject, name in zip(subjects, teaching_staff_names):
        for i in range(3):  # Ensure at least 3 teachers per subject
            full_name = f"{name}"
            staff.append({
                'staff_id': staff_id,
                'full_name': full_name,
                'subject_taught': subject,
                'qualification': random.choice(['B.Ed', 'M.Ed']),
                'years_experience': random.randint(1, 20),
                'date_joined': random_dates(datetime(2010, 1, 1), datetime(2023, 12, 31), 1)[0].strftime('%Y-%m-%d'),
                'email': generate_email(full_name),
                'role_type': 'Teaching',
                'job_title': random.choice(['Senior Teacher', 'Head of Department', 'Class Teacher']),
                'is_active': True
            })
            staff_id += 1

    for name in non_teaching_staff_names:
        full_name = f"{name}"
        staff.append({
            'staff_id': staff_id,
            'full_name': full_name,
            'subject_taught': None,
            'qualification': random.choice(['B.Sc', 'M.Sc']),
            'years_experience': random.randint(1, 20),
            'date_joined': random_dates(datetime(2010, 1, 1), datetime(2023, 12, 31), 1)[0].strftime('%Y-%m-%d'),
            'email': generate_email(full_name),
            'role_type': 'Non-Teaching',
            'job_title': random.choice(['Librarian', 'Accountant', 'Clerk']),
            'is_active': True
        })
        staff_id += 1

    return pd.DataFrame(staff)

# Additional tables generation
def create_fact_resource_usage(student_ids):
    resource_usage = []
    for i in range(300):
        usage_id = 30001 + i
        student_id = random.choice(student_ids)
        resource_usage.append({
            'usage_id': usage_id,
            'student_id': student_id,
            'resource_name': random.choice(['Library', 'Computer Lab', 'Science Lab']),
            'usage_date': random_dates(datetime(2023, 1, 1), datetime(2023, 12, 31), 1)[0].strftime('%Y-%m-%d'),
            'start_time': random.choice(['10:00:00', '12:30:00', '14:00:00']),
            'duration_minutes': random.choice([30, 45, 60]),
            'purpose': random.choice(['Study', 'Research', 'Practical']),
            'supervised_by': random.randint(201, 210)
        })
    return pd.DataFrame(resource_usage)

def create_fact_discipline(student_ids):
    discipline_records = []
    for i in range(100):
        discipline_id = 40001 + i
        student_id = random.choice(student_ids)
        discipline_records.append({
            'discipline_id': discipline_id,
            'student_id': student_id,
            'incident_date': random_dates(datetime(2023, 1, 1), datetime(2023, 12, 31), 1)[0].strftime('%Y-%m-%d'),
            'incident_type': random.choice(['Lateness', 'Disrespect', 'Damage to Property']),
            'action_taken': random.choice(['Warning', 'Suspension', 'Fine']),
            'handled_by': random.randint(201, 210)
        })
    return pd.DataFrame(discipline_records)

def create_fact_extracurricular(student_ids):
    extracurricular = []
    for i in range(150):
        extra_id = 50001 + i
        student_id = random.choice(student_ids)
        extracurricular.append({
            'extracurricular_id': extra_id,
            'student_id': student_id,
            'activity_name': random.choice(['Football', 'Debate', 'Music Club', 'Drama']),
            'activity_date': random_dates(datetime(2023, 1, 1), datetime(2023, 12, 31), 1)[0].strftime('%Y-%m-%d'),
            'duration_minutes': random.choice([60, 90, 120]),
            'instructor': random.randint(201, 210)
        })
    return pd.DataFrame(extracurricular)



# Function to create family data (DimFamily)
def create_family_data():
    families = []
    socioeconomic_status = ['Lower', 'Middle', 'Upper']
    family_structures = ['Both parents', 'Single parent']
    
    for i in range(100):
        families.append({
            'family_id': 5001 + i,
            'socioeconomic_status': random.choice(socioeconomic_status),
            'parent_education_level': random.choice(['Primary', 'Secondary', 'Tertiary']),
            'number_of_siblings': random.randint(1, 5),
            'family_structure': random.choice(family_structures)
        })
    return pd.DataFrame(families)

# Generate the data
students_df = create_student_data()
staff_df = create_staff_data()

resource_usage_df = create_fact_resource_usage(students_df['student_id'].tolist())
discipline_df = create_fact_discipline(students_df['student_id'].tolist())
extracurricular_df = create_fact_extracurricular(students_df['student_id'].tolist())
family_data = create_family_data()



# Save to CSV
students_df.to_csv('legits/DimStudent.csv', index=False)
staff_df.to_csv('legits/DimStaff.csv', index=False)
resource_usage_df.to_csv('legits/FactResourceUsage.csv', index=False)
discipline_df.to_csv('legits/FactDiscipline.csv', index=False)
extracurricular_df.to_csv('legits/FactExtracurricular.csv', index=False)
family_data.to_csv('legits/family_data.csv', index=False)
