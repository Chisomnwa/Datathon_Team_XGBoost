SELECT
    -- FactAcademicPerformance columns
    a.performance_id,
    a.student_id,
    a.year,	
    a.class_name,
    a.subject,
    a.total_score,	
    a.staff_id,  
    a.family_id,

    -- FactExtracurricular columns
    e.extracurricular_id,	
    e.activity_name,	
    e.activity_date,	
    e.duration_minutes,	

    -- FactResourceUsage columns
    r.usage_id,	
    r.resource_name,	
    r.usage_date,	
    r.start_time,	
    r.duration_minutes AS resource_duration,  -- Renamed to avoid ambiguity with extracurricular duration
    r.purpose
FROM 
    {{ ref('stg_FactAcademicPerformance') }} a  -- Staging table for FactAcademicPerformance
LEFT JOIN 
    {{ ref('stg_FactExtracurricular') }} e  -- Staging table for FactExtracurricular
    ON a.student_id = e.student_id  -- Joining on student_id
LEFT JOIN 
    {{ ref('stg_FactResourceUsage') }} r  -- Staging table for FactResourceUsage
    ON a.student_id = r.student_id  -- Joining on student_id
