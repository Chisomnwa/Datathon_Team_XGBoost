select
    usage_id,	
    student_id,	
    resource_name,	
    usage_date,	
    start_time,	
    duration_minutes,	
    purpose,	
    supervised_by as staff_id
from 
    {{ source('sec_school_data', 'FactResourceUsage') }} 
