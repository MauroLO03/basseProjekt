import type { Prediction } from "./Prediction";
import{ getPrediction } from "../model/Prediction";


export interface Match{
    id: number;
    homeTeam: string;
    awayTeam: string;
    matchWinner: string;
    league: string;
    prediction: Prediction;

}


export function createMatch(): Match {
    const mockPrediction = getPrediction();
    const mockMatch: Match = {
        id: 420,
        homeTeam: "West Ham",
        awayTeam: "Man City",
        matchWinner: "N/A",
        league: "Premier League",
        prediction: mockPrediction
    };



    return mockMatch;
}