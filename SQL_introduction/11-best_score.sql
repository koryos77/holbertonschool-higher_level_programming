-- Lists all records with a score > 10 in second_table
SELECT score, name
FROM second_table
WHERE >= 10
ORDER BY score DESC;
