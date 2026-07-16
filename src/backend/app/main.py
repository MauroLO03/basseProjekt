from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.Schemas.matchSchema import Match, Prediction, WinnerOdds, HalfTimeFullTimeOdds, GoalsOdds, GoalLine, CornerOdds, CornerLine, CardOdds, CardLine, BothTeamsScoredOdds
app = FastAPI()

# ---------------------------------------------------------
#  ENABLE CORS (Crucial for Frontend-Backend Communication)
# ---------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------
#  API ENDPOINTS
# ---------------------------------------------------------
@app.get("/api/match", response_model=Match)
def get_match_prediction():
    # This mock data mimics exactly what your createMatch() function did.
    # Later, you will fetch this dynamically from your database!
    mock_prediction = Prediction(
        matchWinner=WinnerOdds(home=1.11, draw=1.11, away=1.11),
        halfTimeFullTime=HalfTimeFullTimeOdds(
            homeHome=1.11, homeDraw=15.00, homeAway=28.00,
            drawHome=1.11, drawDraw=5.00, drawAway=7.00,
            awayHome=28.00, awayDraw=15.00, awayAway=1.11
        ),
        goals=GoalsOdds(overUnder=[
            GoalLine(line=1.5, over=1.11, under=1.11),
            GoalLine(line=2.5, over=1.11, under=1.11),
            GoalLine(line=3.5, over=3.10, under=1.35)
        ]),
        corners=CornerOdds(overUnder=[
            CornerLine(line=8.5, over=1.65, under=2.10),
            CornerLine(line=9.5, over=1.95, under=1.75)
        ]),
        cards=CardOdds(overUnder=[
            CardLine(line=3.5, over=1.70, under=2.05),
            CardLine(line=4.5, over=2.20, under=1.60)
        ]),
        bothTeamsScored=BothTeamsScoredOdds(yes=1.75, no=2.00)
    )

    mock_match = Match(
        id=69,
        homeTeam="West Ham",
        awayTeam="Man City",
        matchWinner="N/A",
        league="Premier League",
        prediction=mock_prediction
    )
    
    return mock_match