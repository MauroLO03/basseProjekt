from fastapi import JSONResponse, status
from services import matchService

class MatchController:
    @staticmethod
    def get_match(match_id: int):
        
        match_info  = matchService.get_match_by_id(match_id)

        
        # 3. Combine the data into a single dictionary payload
        response_content = {
            "homeTeam": match_info.home_team,
            "awayTeam": match_info.away_team
        }
        
        # 4. Return the Response with the structured content
        # Note: If this is a fetch/GET action, HTTP_200_OK is usually preferred over HTTP_201_CREATED
        return JSONResponse(content=response_content, status_code=status.HTTP_200_OK)