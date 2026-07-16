from app.database import get_connection

class StatRepository:
    @staticmethod
    def get_goals_from_team(team_id: int, matches: int):
        conn = get_connection()

        try:
            with conn.cursor() as cursor:
                query = """
                    SELECT 
                        m.match_date,
                        m.home_team_id,
                        m.away_team_id,

                        CASE 
                            WHEN m.home_team_id = %s THEN s.fthg
                            ELSE s.ftag
                        END AS team_goals,

                        CASE 
                            WHEN m.home_team_id = %s THEN s.ftag
                            ELSE s.fthg
                        END AS opponent_goals

                    FROM matches m

                    JOIN match_results_stats s
                        ON m.match_id = s.match_id

                    WHERE 
                        m.home_team_id = %s
                        OR m.away_team_id = %s

                    ORDER BY m.match_date DESC

                    LIMIT %s
                """

                cursor.execute(
                    query,
                    (
                        team_id,
                        team_id,
                        team_id,
                        team_id,
                        matches
                    )
                )

                rows = cursor.fetchall()

                if not rows:
                    return None

                return [
                    {
                        "match_date": row[0],
                        "home_team_id": row[1],
                        "away_team_id": row[2],
                        "team_goals": row[3],
                        "opponent_goals": row[4]
                    }
                    for row in rows
                ]

        finally:
            conn.close()



class StatRepository:
    @staticmethod
    def get_goals_from_team(team_id: int, matches: int):
        conn = get_connection()

        try:
            with conn.cursor() as cursor:
                query = """
                    SELECT 
                        m.match_date,
                        s.fthg as team_goals,
                        s.ftag as opponent_goals,
                        s.hthg as team_ht_goals,
                        s.htag as opponent_ht_goals,
                        s.home_corners as team_corners,
                        s.away_corners as opponent_corners,
                        s.home_yellow as team_yellow,
                        s.away_yellow as opponent_yellow,
                        s.

                        CASE 
                            WHEN m.home_team_id = %s THEN s.fthg
                            ELSE s.ftag
                        END AS team_goals,

                        CASE 
                            WHEN m.home_team_id = %s THEN s.ftag
                            ELSE s.fthg
                        END AS opponent_goals

                    FROM matches m

                    JOIN match_results_stats s
                        ON m.match_id = s.match_id

                    WHERE 
                        m.home_team_id = %s
                        OR m.away_team_id = %s

                    ORDER BY m.match_date DESC

                    LIMIT %s
                """

                cursor.execute(
                    query,
                    (
                        team_id,
                        team_id,
                        team_id,
                        team_id,
                        matches
                    )
                )

                rows = cursor.fetchall()

                if not rows:
                    return None

                return [
                    {
                        "match_date": row[0],
                        "home_team_id": row[1],
                        "away_team_id": row[2],
                        "team_goals": row[3],
                        "opponent_goals": row[4]
                    }
                    for row in rows
                ]

        finally:
            conn.close()

statRepository = StatRepository()