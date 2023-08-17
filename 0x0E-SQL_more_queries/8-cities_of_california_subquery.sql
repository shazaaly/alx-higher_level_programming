-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa.

-- The states table contains only one record where name = California (but the id can be different, as per the example)
-- Results must be sorted in ascending order by cities.id


USE `hbtn_0d_usa`

SELECT id, name
FROM `cities`
WHERE state_id = (
	SELECT id FROM `states`
	WHERE name = 'California'

)
ORDER BY `id` ASC;
;
