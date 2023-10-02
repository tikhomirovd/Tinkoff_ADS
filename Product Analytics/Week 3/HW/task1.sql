SELECT q.quest_nm   AS quest_name,
       l.complexity AS legend_complexity,
       AVG(g.time)  AS average_time
FROM quest q
         JOIN
     legend l ON q.legend_rk = l.legend_rk
         JOIN
     game g ON q.quest_rk = g.quest_rk
WHERE g.time != '00:00:00'
GROUP BY q.quest_nm,
         l.complexity
ORDER BY l.complexity,
         AVG(g.time);