from app.database import get_connection


class StatRepository:

    @staticmethod
    def _get_average(
        team_id: int,
        num_matches: int,
        goal_column: str,
        team_filter: str
    ) -> float:

        conn = get_connection()

        try:
            with conn.cursor() as cursor:

                query = f"""
                    SELECT COALESCE(AVG(team_goals), 0)
                    FROM (
                        SELECT {goal_column} AS team_goals
                        FROM matches m
                        JOIN match_results_stats s
                            ON m.match_id = s.match_id
                        WHERE {team_filter}
                        ORDER BY m.match_date DESC
                        LIMIT %s
                    ) recent_matches;
                """

                cursor.execute(
                    query,
                    (
                        team_id,
                        num_matches
                    )
                )

                return float(cursor.fetchone()[0])

        finally:
            conn.close()


    @staticmethod
    def get_home_goals_scored(
        team_id: int,
        num_matches: int
    ) -> float:

        return StatRepository._get_average(
            team_id,
            num_matches,
            "s.fthg",
            "m.home_team_id = %s"
        )


    @staticmethod
    def get_away_goals_scored(
        team_id: int,
        num_matches: int
    ) -> float:

        return StatRepository._get_average(
            team_id,
            num_matches,
            "s.ftag",
            "m.away_team_id = %s"
        )


    @staticmethod
    def get_home_goals_conceded(
        team_id: int,
        num_matches: int
    ) -> float:

        return StatRepository._get_average(
            team_id,
            num_matches,
            "s.ftag",
            "m.home_team_id = %s"
        )


    @staticmethod
    def get_away_goals_conceded(
        team_id: int,
        num_matches: int
    ) -> float:

        return StatRepository._get_average(
            team_id,
            num_matches,
            "s.fthg",
            "m.away_team_id = %s"
        )


    @staticmethod
    def get_home_win_rate(
        team_id: int,
        num_matches: int
    ) -> float:

        conn = get_connection()

        try:
            with conn.cursor() as cursor:

                query = """
                    SELECT COALESCE(
                        AVG(
                            CASE
                                WHEN s.fthg > s.ftag THEN 1
                                ELSE 0
                            END
                        ),
                        0
                    )
                    FROM matches m
                    JOIN match_results_stats s
                        ON m.match_id = s.match_id
                    WHERE m.home_team_id = %s
                    ORDER BY m.match_date DESC
                    LIMIT %s;
                """

                cursor.execute(
                    query,
                    (
                        team_id,
                        num_matches
                    )
                )

                return float(cursor.fetchone()[0])

        finally:
            conn.close()


    @staticmethod
    def get_away_win_rate(
        team_id: int,
        num_matches: int
    ) -> float:

        conn = get_connection()

        try:
            with conn.cursor() as cursor:

                query = """
                    SELECT AVG(win)
                    FROM (
                        SELECT
                            CASE
                                WHEN s.fthg > s.ftag THEN 1
                                ELSE 0
                            END AS win
                        FROM matches m
                        JOIN match_results_stats s
                            ON m.match_id = s.match_id
                        WHERE m.home_team_id = %s
                        ORDER BY m.match_date DESC
                        LIMIT %s
                    ) recent_matches;
                """

                cursor.execute(
                    query,
                    (
                        team_id,
                        num_matches
                    )
                )

                return float(cursor.fetchone()[0])

        finally:
            conn.close()


    @staticmethod
    def get_league_home_goal_average() -> float:

        conn = get_connection()

        try:
            with conn.cursor() as cursor:

                query = """
                    SELECT AVG(s.fthg)
                    FROM match_results_stats s;
                """

                cursor.execute(query)

                return float(cursor.fetchone()[0])

        finally:
            conn.close()


    @staticmethod
    def get_league_away_goal_average() -> float:

        conn = get_connection()

        try:
            with conn.cursor() as cursor:

                query = """
                    SELECT AVG(s.ftag)
                    FROM match_results_stats s;
                """

                cursor.execute(query)

                return float(cursor.fetchone()[0])

        finally:
            conn.close()

    @staticmethod
    def get_league_total_goal_average() -> float:
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                query = """
                    SELECT AVG(s.fthg + s.ftag)
                    FROM match_results_stats s;
                """
                cursor.execute(query)
                return float(cursor.fetchone()[0])
        finally:
            conn.close()


    @staticmethod
    def get_team_htft_probabilities (team_id: int, venue: str, num_matches: int) -> list[tuple]:
        conn = get_connection()
        try: 
            with conn.cursor() as cursor:
                query = """
                    WITH recent_matches AS (
                        SELECT *
                        FROM team_match_history
                        WHERE team_id = %s
                        AND venue = %s
                        ORDER BY match_date DESC
                        LIMIT %s
                    )

                    SELECT
                        ht_ft_combo,
                        COUNT(*) AS occurrences,
                        COUNT(*) * 1.0 / SUM(COUNT(*)) OVER() AS probability
                    FROM recent_matches
                    GROUP BY ht_ft_combo
                    ORDER BY probability DESC;
                    """

                cursor.execute(
                    query,
                    (team_id,
                     venue,
                     num_matches)
                )

                return cursor.fetchall()
        finally:
            conn.close()
