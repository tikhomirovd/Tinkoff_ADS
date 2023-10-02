WITH PopularQuest AS (SELECT q.quest_rk, q.quest_nm
                      FROM quest q
                               JOIN game g ON q.quest_rk = g.quest_rk
                      GROUP BY q.quest_rk, q.quest_nm
                      ORDER BY COUNT(g.game_rk) DESC
                      LIMIT 1),
     QuestResults AS (SELECT a.login,
                             pq.quest_nm,
                             g.time,
                             g.game_dttm
                      FROM game g
                               JOIN application ap ON g.game_rk = ap.game_rk
                               JOIN account a ON ap.account_rk = a.account_rk
                               JOIN PopularQuest pq ON g.quest_rk = pq.quest_rk
                      WHERE g.time != '00:00:00'
                      ORDER BY g.time
                      LIMIT 3)
SELECT *
FROM QuestResults;
