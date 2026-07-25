from fastapi import JSONResponse, status
from services.matchService import MatchService

class MatchController:
    @staticmethod
    def get_match(match_id: int):
        
        match_info  = MatchService.get_match_by_id(match_id)
        



        
        return JSONResponse(content=match_info.model_dump(), status_code=200)