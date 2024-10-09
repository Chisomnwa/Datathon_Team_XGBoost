select
    *
from 
    {{ source('sec_school_data', 'DimFamily') }} 
