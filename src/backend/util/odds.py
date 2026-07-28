from domains.predictions.matchWinnerDomain import MatchWinnerPrediction
def probability_to_odds(
            
    probability: float
) -> float:

    if probability <= 0:
        return 0    

    return round(1 / probability, 2)    



def prediction_to_odds(
    prediction: MatchWinnerPrediction
) -> MatchWinnerPrediction:
    
    return MatchWinnerPrediction (
        home= probability_to_odds(prediction.home),
        draw= probability_to_odds(prediction.draw),
        away= probability_to_odds(prediction.away)
    )