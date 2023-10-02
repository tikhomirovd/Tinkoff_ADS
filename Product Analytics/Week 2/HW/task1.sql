WITH employee_last_x AS (SELECT employee_rk
                         FROM employee
                         WHERE last_name = 'Петухов'
),
     game_2023 AS (SELECT game_rk, employee_rk
                   FROM game
                   WHERE EXTRACT(YEAR FROM game_dttm) = 2022
                     AND game_flg = 1),
     games_2023_last_x_games AS (SELECT g.game_rk, e.employee_rk
                                 FROM game_2023 g
                                          JOIN employee_last_x e ON g.employee_rk = e.employee_rk)
SELECT employee_rk,
       COUNT(game_rk) AS total_games
FROM games_2023_last_x_games
GROUP BY employee_rk;
