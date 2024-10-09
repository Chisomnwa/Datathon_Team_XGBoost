select
    performance_id,
    student_id,
    year,	
    class_name,	
    subject,
    total_score,	
    teacher_id as staff_id,
    family_id
from 
    {{ source('sec_school_data', 'FactAcademicPerformance') }} 
