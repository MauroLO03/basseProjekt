from app.database import get_connection
from domains.matchDomain import Match

class TeamRepository:
    
    @staticmethod
    def get_team_by_id(team_id: int):
        conn = get_connection()

        try:
            with conn.cursor() as cursor:
                query = """
                select * from teams where team_id=%s
                """
                cursor.execute(query, (team_id,))
                row = cursor.fetchone()
                if row is None:
                    return None
                
                return {
                    "id": row[0],
                    "name": row[1],
                    "league_id": row[2]
                }
        finally:
            conn.close()

    @staticmethod
    def get_team_name_by_id(team_id: int):
        conn = get_connection()

        try:
            with conn.cursor() as cursor:
                query = """
                select * from teams where team_id=%s
                """
                cursor.execute(query, (team_id,))
                row = cursor.fetchone()
                if row is None:
                    return None
                
                return {
                    "id": row[0],
                    "name": row[1],
                    "league_id": row[2]
                }
        finally:
            conn.close()

    @staticmethod
    def get_team_by_name(team_name: str):
        conn = get_connection()

        try:
            with conn.cursor() as cursor:
                query = """
                select * from teams where team_name=%s
                """
                cursor.execute(query, (team_name,))
                row = cursor.fetchone()
                if row is None:
                    return None
                
                return {
                    "id": row[0],
                    "name": row[1],
                    "league_id": row[2]
                }
        finally:
            conn.close()
    
    


teamRepository = TeamRepository()