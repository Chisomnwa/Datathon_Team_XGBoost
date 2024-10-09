SELECT
    performance_id,
    student_id,
    year,	
    class_name,	
    subject,
    total_score,	
    staff_id,
    family_id
FROM 
    {{ ref('stg_FactAcademicPerformance') }}