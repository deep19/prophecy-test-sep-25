{{
  config({    
    "materialized": "ephemeral",
    "database": "kaustubh_keskar",
    "schema": "default"
  })
}}

WITH t1 AS (

  SELECT * 
  
  FROM {{ source('deeptanshu.default', 't1') }}

),

variable_column_selection AS (

  SELECT 
    {{ var('abc') }} AS tCol,
    {{ var('projectConfVar') }} AS tColProjectConf
  
  FROM t1 AS in0

),

Limit_1 AS (

  SELECT * 
  
  FROM variable_column_selection AS in0
  
  LIMIT 5

)

SELECT *

FROM Limit_1
