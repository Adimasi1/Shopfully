USE orders_db;

SELECT 
    order_month,
    order_type,
    SUM(clicks) AS total_clicks,
    SUM(visualizations) AS total_visualizations,
    ROUND(SUM(clicks) / NULLIF(SUM(visualizations), 0), 2) AS CTR  -- rounded to 2 decimals
FROM orders_kpi
WHERE customer_id = 123
AND order_year = 2024
AND order_month IN (10, 11)  -- filter october and november
GROUP BY order_month, order_type
ORDER BY order_month, order_type;


