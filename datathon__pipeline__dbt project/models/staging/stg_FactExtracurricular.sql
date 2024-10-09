select
    extracurricular_id,	
    student_id,	
    activity_name,	
    activity_date,	
    duration_minutes,	
    instructor as staff_id
from 
    {{ source('sec_school_data', 'FactExtracurricular') }} 
