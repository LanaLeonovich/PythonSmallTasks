SELECT pack_id
FROM Packs
GROUP BY pack_id
HAVING COUNT(*) = 1;
