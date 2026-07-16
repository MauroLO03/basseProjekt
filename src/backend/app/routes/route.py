from fastapi import APIRouter, HTTPException
from Schemas.matchSchema import MatchResponse
from services.matchService import MatchService

# Create the router instance
router = APIRouter()

@router.get("/matches/{match_id}", response_model=MatchResponse)
def get_match_prediction(match_id: int):
    try:
        return MatchService.get_match_by_id(match_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e)) 
    except Exception as e:
        print(f"🔴 DATABASE/SERVER CRASH DETAILS: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")