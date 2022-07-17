{{
  config(
    materialized='view'
  )
}}

select
sum(total_amount)
from yellow_taxi_data
