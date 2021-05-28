SELECT * FROM levelupapi_gametype;


SELECT
        e.id as EventId,
        e.datetime,
        g.title as game_name,
        gr.id as HOST,
        u.first_name ||' '|| u.last_name as full_name
    FROM
        levelupapi_event e
    JOIN
        levelupapi_game g ON e.game_id = g.id
    JOIN
        levelupapi_gamer gr ON e.host_id = gr.id
    JOIN
        auth_user u ON gr.id = u.id