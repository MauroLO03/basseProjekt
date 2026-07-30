from app.database import get_connection


class StatRepository:

    @staticmethod
    def _get_stat_average(
        team_id: int,
        venue: str,
        num_matches: int,
        column: str
    ) -> float:

        conn = get_connection()

        try:
            with conn.cursor() as cursor:

                query = f"""
                    SELECT COALESCE(AVG({column}), 0)
                    FROM (
                        SELECT {column}
                        FROM team_match_history
                        WHERE team_id = %s
                        AND venue = %s
                        ORDER BY match_date DESC
                        LIMIT %s
                    ) recent_matches;
                """

                cursor.execute(
                    query,
                    (
                        team_id,
                        venue,
                        num_matches
                    )
                )

                return float(cursor.fetchone()[0])

        finally:
            conn.close()

    # --- GOALS SCORED & CONCEDED ---

    @staticmethod
    def get_home_goals_scored(team_id: int, num_matches: int) -> float:
        return StatRepository._get_stat_average(team_id, "HOME", num_matches, "ft_for")

    @staticmethod
    def get_away_goals_scored(team_id: int, num_matches: int) -> float:
        return StatRepository._get_stat_average(team_id, "AWAY", num_matches, "ft_for")

    @staticmethod
    def get_home_goals_conceded(team_id: int, num_matches: int) -> float:
        return StatRepository._get_stat_average(team_id, "HOME", num_matches, "ft_against")

    @staticmethod
    def get_away_goals_conceded(team_id: int, num_matches: int) -> float:
        return StatRepository._get_stat_average(team_id, "AWAY", num_matches, "ft_against")

    # --- CORNERS ---

    @staticmethod
    def get_home_corners(team_id: int, num_matches: int) -> float:
        return StatRepository._get_stat_average(team_id, "HOME", num_matches, "corners_for")

    @staticmethod
    def get_away_corners(team_id: int, num_matches: int) -> float:
        return StatRepository._get_stat_average(team_id, "AWAY", num_matches, "corners_for")

    # --- CARDS ---

    @staticmethod
    def get_home_yellow_cards(team_id: int, num_matches: int) -> float:
        return StatRepository._get_stat_average(team_id, "HOME", num_matches, "yellow_cards_for")

    @staticmethod
    def get_away_yellow_cards(team_id: int, num_matches: int) -> float:
        return StatRepository._get_stat_average(team_id, "AWAY", num_matches, "yellow_cards_for")

    # --- WIN RATES ---

    @staticmethod
    def get_home_win_rate(team_id: int, num_matches: int) -> float:
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                query = """
                    SELECT COALESCE(
                        AVG(CASE WHEN ft_result = '1' THEN 1 ELSE 0 END), 0
                    )
                    FROM (
                        SELECT ft_result
                        FROM team_match_history
                        WHERE team_id = %s AND venue = 'HOME'
                        ORDER BY match_date DESC
                        LIMIT %s
                    ) recent_matches;
                """
                cursor.execute(query, (team_id, num_matches))
                return float(cursor.fetchone()[0])
        finally:
            conn.close()

    @staticmethod
    def get_away_win_rate(team_id: int, num_matches: int) -> float:
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                query = """
                    SELECT COALESCE(
                        AVG(CASE WHEN ft_result = '2' THEN 1 ELSE 0 END), 0
                    )
                    FROM (
                        SELECT ft_result
                        FROM team_match_history
                        WHERE team_id = %s AND venue = 'AWAY'
                        ORDER BY match_date DESC
                        LIMIT %s
                    ) recent_matches;
                """
                cursor.execute(query, (team_id, num_matches))
                return float(cursor.fetchone()[0])
        finally:
            conn.close()

    # --- LEAGUE AVERAGES ---

    @staticmethod
    def get_league_home_goal_average() -> float:
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                query = "SELECT AVG(s.fthg) FROM match_results_stats s;"
                cursor.execute(query)
                return float(cursor.fetchone()[0])
        finally:
            conn.close()

    @staticmethod
    def get_league_away_goal_average() -> float:
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                query = "SELECT AVG(s.ftag) FROM match_results_stats s;"
                cursor.execute(query)
                return float(cursor.fetchone()[0])
        finally:
            conn.close()

    @staticmethod
    def get_league_total_goal_average() -> float:
        conn = get_connection()
        try:
            with conn.cursor() as cursor:
                query = "SELECT AVG(s.fthg + s.ftag) FROM match_results_stats s;"
                cursor.execute(query)
                return float(cursor.fetchone()[0])
        finally:
            conn.close()

    # --- HT/FT PROBABILITIES ---

    @staticmethod
    def get_team_htft_probabilities(team_id: int, venue: str, num_matches: int) -> list[tuple]:
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
                cursor.execute(query, (team_id, venue, num_matches))
                return cursor.fetchall()
        finally:
            conn.close()