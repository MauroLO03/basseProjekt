CREATE OR REPLACE VIEW team_match_history AS

-- HOME teams
SELECT
    m.match_id,
    m.league_id,
    m.match_date,

    m.home_team_id AS team_id,
    m.away_team_id AS opponent_id,

    'HOME' AS venue,

    r.hthg AS ht_for,
    r.htag AS ht_against,

    r.fthg AS ft_for,
    r.ftag AS ft_against,


    -- CORNERS
    r.home_corners AS corners_for,
    r.away_corners AS corners_against,


    -- CARDS
    r.home_yellow AS yellow_cards_for,
    r.away_yellow AS yellow_cards_against,

    r.home_red AS red_cards_for,
    r.away_red AS red_cards_against,


    CASE
        WHEN r.hthg > r.htag THEN '1'
        WHEN r.hthg = r.htag THEN 'X'
        ELSE '2'
    END AS ht_result,


    CASE
        WHEN r.fthg > r.ftag THEN '1'
        WHEN r.fthg = r.ftag THEN 'X'
        ELSE '2'
    END AS ft_result,


    CONCAT(
        CASE
            WHEN r.hthg > r.htag THEN '1'
            WHEN r.hthg = r.htag THEN 'X'
            ELSE '2'
        END,
        '/',
        CASE
            WHEN r.fthg > r.ftag THEN '1'
            WHEN r.fthg = r.ftag THEN 'X'
            ELSE '2'
        END
    ) AS ht_ft_combo


FROM matches m
JOIN match_results_stats r
ON m.match_id = r.match_id



UNION ALL



-- AWAY teams
SELECT
    m.match_id,
    m.league_id,
    m.match_date,

    m.away_team_id AS team_id,
    m.home_team_id AS opponent_id,

    'AWAY' AS venue,


    r.htag AS ht_for,
    r.hthg AS ht_against,

    r.ftag AS ft_for,
    r.fthg AS ft_against,


    -- CORNERS
    r.away_corners AS corners_for,
    r.home_corners AS corners_against,


    -- CARDS
    r.away_yellow AS yellow_cards_for,
    r.home_yellow AS yellow_cards_against,

    r.away_red AS red_cards_for,
    r.home_red AS red_cards_against,


    CASE
        WHEN r.htag > r.hthg THEN '1'
        WHEN r.htag = r.hthg THEN 'X'
        ELSE '2'
    END AS ht_result,


    CASE
        WHEN r.ftag > r.fthg THEN '1'
        WHEN r.ftag = r.fthg THEN 'X'
        ELSE '2'
    END AS ft_result,


    CONCAT(
        CASE
            WHEN r.htag > r.hthg THEN '1'
            WHEN r.htag = r.hthg THEN 'X'
            ELSE '2'
        END,
        '/',
        CASE
            WHEN r.ftag > r.fthg THEN '1'
            WHEN r.ftag = r.fthg THEN 'X'
            ELSE '2'
        END
    ) AS ht_ft_combo


FROM matches m
JOIN match_results_stats r
ON m.match_id = r.match_id;