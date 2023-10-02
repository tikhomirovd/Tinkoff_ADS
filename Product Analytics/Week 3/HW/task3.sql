SELECT p.partner_nm AS partner_name,
       SUM(g.price) AS total_revenue
FROM partner p
         JOIN
     location l ON p.partner_rk = l.partner_rk
         JOIN
     quest q ON l.location_rk = q.location_rk
         JOIN
     game g ON q.quest_rk = g.quest_rk
GROUP BY p.partner_nm
ORDER BY total_revenue DESC;