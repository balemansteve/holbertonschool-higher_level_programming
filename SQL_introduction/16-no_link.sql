-- Count the number of records per score and sort them in descending order

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY DESC;