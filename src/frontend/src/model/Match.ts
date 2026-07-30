import type { Prediction } from "./Prediction";


export interface Match{
    id:number;
    homeTeam:string;
    awayTeam:string;
    league:string;
    prediction:Prediction;
}


