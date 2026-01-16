
select
    user_id,
    total_spent
from {{ ref('dm_users') }}
where total_spent < 0