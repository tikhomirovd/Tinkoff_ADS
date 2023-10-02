WITH
    -- Завершённые Игры
    game_finished AS (
        SELECT game_rk
        FROM game
        WHERE finish_flg = 1
    ),
    -- Заявки на завершённую игру
    application_game_finished AS (
        SELECT a.application_rk, a.client_rk
        FROM application a
        JOIN game_finished gf ON a.game_rk = gf.game_rk
    ),
    -- Клиенты, зарегистрированные в 2022 году
    clients_registered_2022 AS (
        SELECT a.client_rk
        FROM account a
        WHERE EXTRACT(YEAR FROM registration_dttm) = 2022
    ),
    -- Завершённые игры клиентов, зарегистрированных в 2022 году
    finished_games_clients_2022 AS (
        SELECT agf.application_rk, cr.client_rk
        FROM application_game_finished agf
        JOIN clients_registered_2022 cr ON agf.client_rk = cr.client_rk
    )
-- Группировка по client_rk и подсчет количества игр для каждого клиента
, client_game_counts AS (
    SELECT client_rk, COUNT(application_rk) AS game_count
    FROM finished_games_clients_2022
    GROUP BY client_rk
)
-- Вычисление среднего количества завершенных игр на клиента
SELECT AVG(game_count) AS average_completed_games_per_client
FROM client_game_counts;
