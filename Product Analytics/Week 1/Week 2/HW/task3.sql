WITH location_of_partner_x AS (SELECT l.location_rk
                               FROM location l
                                        JOIN partner p ON l.partner_rk = p.partner_rk
                               WHERE p.partner_nm = 'ОАО ТелеРыбЖелДорЛизинг'),
     quest_of_partner_x AS (SELECT q.quest_rk, l.location_rk
                            FROM quest q
                                     JOIN location_of_partner_x l ON q.location_rk = l.location_rk),
     games_partner_x AS (SELECT g.game_rk, q.location_rk, g.game_flg
                         FROM game g
                                  JOIN quest_of_partner_x q ON g.quest_rk = q.quest_rk)
SELECT location_rk,
       AVG(game_flg::DECIMAL) * 100 AS percentage_of_games_held
FROM games_partner_x
GROUP BY location_rk;
