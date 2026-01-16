with source as (
    select * from {{ source('ecommerce_source', 'orders') }}
),

renamed as (
    select
        order_id,
        user_id,
        status,
        order_date as ordered_at,
        cast(total_amount as decimal(10,2)) as total_amount
    from source
)

select * from renamed