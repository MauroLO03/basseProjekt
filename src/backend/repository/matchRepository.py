from app.database import get_connection
from domains.matchDomain import Match

class MatchRepository:
    
    @staticmethod
    def get_match_by_id(match_id: int):
        conn = get_connection()

        try:
            with conn.cursor() as cursor:
                query = """
                select * from matches where match_id=%s
                """
                cursor.execute(query, (match_id,))
                row = cursor.fetchone()
                if row is None:
                    return None
                
                return Match(
                    id = row[0],
                    league_id=row[1],
                    date=row[2],
                    home_team = row[3],
                    away_team = row[4],
                    referee=row[5]
                )
        finally:
            conn.close()

matchRepository = MatchRepository()