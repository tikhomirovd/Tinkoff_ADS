WITH Clients AS (SELECT DISTINCT c.client_rk,
                                 c.first_name,
                                 c.last_name,
                                 c.phone_num
                 FROM client c
                          JOIN
                      account a ON c.client_rk = a.client_rk
                          JOIN
                      application ap ON a.account_rk = ap.account_rk
                 WHERE EXTRACT(MONTH FROM ap.application_dttm) = 9
                   AND EXTRACT(YEAR FROM ap.application_dttm) = 2022),
     VisitedQuests AS (SELECT c.client_rk,
                              g.quest_rk
                       FROM Clients c
                                JOIN
                            account a ON c.client_rk = a.client_rk
                                JOIN
                            application ap ON a.account_rk = ap.account_rk
                                JOIN
                            game g ON ap.game_rk = g.game_rk),
     AllQuests AS (SELECT quest_rk,
                          quest_nm
                   FROM quest)

SELECT c.first_name,
       c.last_name,
       c.phone_num,
       STRING_AGG(aq.quest_nm, ', ') AS unvisited_quests
FROM Clients c
         JOIN
     AllQuests aq ON TRUE
         LEFT JOIN
     VisitedQuests vq ON c.client_rk = vq.client_rk AND aq.quest_rk = vq.quest_rk
WHERE vq.quest_rk IS NULL
GROUP BY c.client_rk,
         c.first_name,
         c.last_name,
         c.phone_num
ORDER BY c.last_name,
         c.first_name;
