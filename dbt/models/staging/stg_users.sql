with source as (
    select * from {{ source('ecommerce_source', 'users') }}
),

renamed as (
    select
        user_id,
        email,
        first_name,
        last_name,
        address,
        cast(created_at as timestamp) as created_at
    from source
)

select * from renamed