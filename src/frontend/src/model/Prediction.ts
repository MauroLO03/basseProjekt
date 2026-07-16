export interface Prediction{
    matchWinner: WinnerOdds;
    halfTimeFullTime: HalfTimeFullTimeOdds;
    goals: GoalsOdds;
    corners: CornerOdds;
    cards: CardOdds;
    bothTeamsScored: BothTeamsScoredOdds;
}

export interface WinnerOdds{
    home: number;
    draw: number;
    away: number;
}

export interface HalfTimeFullTimeOdds{
    homeHome: number;
    homeDraw: number;
    homeAway: number;
    drawHome: number;
    drawDraw: number;
    drawAway: number;
    awayHome: number;
    awayDraw: number;
    awayAway: number;
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


export function getPrediction(): Prediction {
    // här ska vi göra api anropet och hämta prediction data från backend
    const mockPrediction: Prediction = {
        matchWinner: {
            home: 1.11,
            draw: 1.11,
            away: 1.11
        },
        halfTimeFullTime: {
            homeHome: 1.11,
            homeDraw: 15.00,
            homeAway: 28.00,
            drawHome: 1.11,
            drawDraw: 5.00,
            drawAway: 7.00,
            awayHome: 28.00,
            awayDraw: 15.00,
            awayAway: 1.11
        },
        goals: {
            overUnder: [
                { line: 1, over: 1.11, under: 1.11 },
                { line: 1, over: 1.11, under: 1.11 },
                { line: 3.5, over: 3.10, under: 1.35 }
            ]
        },
        corners: {
            overUnder: [
                { line: 8.5, over: 1.65, under: 2.10 },
                { line: 9.5, over: 1.95, under: 1.75 }
            ]
        },
        cards: {
            overUnder: [
                { line: 3.5, over: 1.70, under: 2.05 },
                { line: 4.5, over: 2.20, under: 1.60 }
            ]
        },
        bothTeamsScored: {
            yes: 1.75,
            no: 2.00
        }
    };

    return mockPrediction;
}