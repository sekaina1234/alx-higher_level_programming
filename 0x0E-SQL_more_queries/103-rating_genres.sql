-- a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT a.name, SUM(c.rate) AS rating
FROM tv_genres AS a
JOIN tv_show_genres AS b
ON a.id = b.genre_id
JOIN tv_show_ratings AS c
ON b.show_id = c.show_id
GROUP BY a.name
ORDER BY rating DESC;
