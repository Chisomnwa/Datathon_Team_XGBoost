SELECT
    usage_id,	
    student_id,	
    resource_name,	
    usage_date,	
    start_time,	
    duration_minutes,	
    purpose,	
    staff_id
FROM 
    {{ ref('stg_FactResourceUsage') }} 
