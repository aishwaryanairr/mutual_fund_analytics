-- Top 5 funds by AUM

SELECT *
FROM fact_aum
ORDER BY aum DESC
LIMIT 5;
-- Average NAV per month
SELECT
strftime('%Y-%m',date)
AS month,

AVG(nav)

FROM fact_nav

GROUP BY month;