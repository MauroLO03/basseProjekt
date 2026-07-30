export interface Prediction {
    matchWinner: WinnerOdds;
    htFtOdds: HalfTimeFullTimeOdds;
    overUnderOdds: GoalsOdds;
    cornerOdds: CornerOdds;
    yellowCardOdds: CardOdds;
}

export interface WinnerOdds{
    home: number;
    draw: number;
    away: number;
}

export interface HalfTimeFullTimeOdds {
    home: HtFtProbability;
    away: HtFtProbability;
}


export interface HtFtProbability {
    htft_1_1: number;
    htft_1_x: number;
    htft_1_2: number;

    htft_x_1: number;
    htft_x_x: number;
    htft_x_2: number;

    htft_2_1: number;
    htft_2_x: number;
    htft_2_2: number;
}

export interface GoalsOdds{
    overUnder: GoalLine[];
}

export interface GoalLine{
    line: number;
    over: number;
    under: number;
}

export interface CornerOdds{
    overUnder: CornerLine[];
}

export interface CornerLine{
    line: number;
    over: number;
    under: number;
}

export interface CardOdds{
    overUnder: CardLine[];
}

export interface CardLine{
    line: number;
    over: number;
    under: number;
}

export interface BothTeamsScoredOdds{
    yes: number;
    no: number;
}

