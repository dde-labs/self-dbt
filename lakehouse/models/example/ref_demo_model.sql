-- Use the `ref` function to select from other models
select *
from {{ ref('demo_model') }}
where id = 1
