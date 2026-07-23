from scipy.stats import poisson

MAX_GOALS = 8 

#calculates how strong the teams offensive is relative to the rest of the league
def calculate_attack_strength(
        team_goals_scored: float, 
        league_average_goals: float
        ) -> float:
 
    if league_average_goals == 0:
        return 0
    
    return team_goals_scored / league_average_goals


#calculates how strong a teams defense is relative to the reest of the league
def calculate_defense_strength(
        team_goals_conceded: float, 
        league_average_goals: float
) -> float:
    if league_average_goals == 0:
        return 0
    
    return team_goals_conceded / league_average_goals
    

#calculates how many goals a team is expected to score on their opponent (lambda)
def calculate_expected_goals(
        attack_strength: float, 
        opponent_defense_strength: float,
        league_average_goals: float
        )-> float:
    return( attack_strength * opponent_defense_strength * league_average_goals)


#creates the poisson distribution up to 8 goals
def calculate_goal_probabilities(
        expected_goals: float,
        max_goals: int = MAX_GOALS
) ->list[float]:
    
    return poisson.pmf(
        range(max_goals+1),
        mu = expected_goals
    ).tolist()


#creates the probability of every possible scoreline
def build_score_matrix(
        home_probabilities: list[float],
        away_probabilities: list[float]
)-> list[list[float]]:
    
    matrix = []

    for home_probability in home_probabilities:
        row = []

        for away_probability in away_probabilities:
            row.append(
                home_probability*away_probability
            )
        matrix.append(row)
    
    return matrix


#transforms all possible scorelines into three outcomes (1/X/2)
def calculate_match_probabilities(
        score_matrix: list[list[float]]
) -> dict:
    home_win = 0.0
    draw = 0.0
    away_win = 0.0

    for home_goals, row in enumerate(score_matrix):
        for away_goals, probability in enumerate(row):
            
            if home_goals > away_goals:
                home_win += probability

            elif home_goals== away_goals:
                draw += probability
            
            else:
                away_win += probability
            
    return{  #överväg att skapa en datatyp för detta objekt och returnera den
        "1": home_win  ,
        "X": draw,
        "2": away_win
    }

def probabilities_to_odds(
        probabilities: dict[str,float]
)-> dict[str, float]:
    
    odds = {}

    for outcome, probability in probabilities.items():
        odds[outcome] = round(
            1/probability,
            2
        )
    return odds