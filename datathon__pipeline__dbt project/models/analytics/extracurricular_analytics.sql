SELECT
    extracurricular_id,	
    student_id,	
    activity_name,	
    activity_date,	
    duration_minutes,	
    staff_id
FROM 
    {{ ref('stg_FactExtracurricular') }} 
