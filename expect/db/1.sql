SELECT *
FROM info
JOIN roe
ON info.symbol = roe.symbol
WHERE roe.`type` = 'tb'
and info.symbol IN(
SELECT symbol
FROM jlr
WHERE r0> 10
AND r1 > 10
AND r2 > 10
AND s0 > 10
AND s1 > 10
AND s2 > 10
AND s3 > 10)
