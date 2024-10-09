select
    *
from 
    {{ source('sec_school_data', 'DimStaff') }} 
