CREATE database plStats;

create table league(
    league_id int generated always as identity,
    div_code varchar(10),
    country varchar(20),

    constraint pk_league primary key (league_id)
);


create table teams(
    team_id int generated always as identity,
    team_name varchar(50),

    constraint pk_teams primary key (team_id)
);

create table matches(
    match_id int generated always as identity,
    league_id int not null,
    match_date date,
    home_team_id int not null,
    away_team_id int not null,
    referee varchar(50),

    constraint pk_matches primary key (match_id),
    
    constraint fk_home_team 
        foreign key (home_team_id)
        references teams(team_id),

    constraint fk_away_team
        foreign key (away_team_id)
        references teams(team_id),

    constraint fk_league_id
        foreign key (league_id)
        references league(league_id)
        on delete cascade
);

create table match_results_stats(
    match_id int,
    hthg int,
    htag int,
    htr char(1) CHECK (htr IN ('H', 'D', 'A')),
    fthg int,
    ftag int,
    ftr char(1) CHECK (ftr IN ('H', 'D', 'A')),
    attendance int,
    home_shots int,
    away_shots int,
    home_shots_target int,
    away_shots_target int,
    home_corners int,
    away_corners int,
    home_fouls int,
    away_fouls int,
    home_yellow int,
    away_yellow int,
    home_red int,
    away_red int,

    constraint pk_match_results_stats primary key (match_id),
    constraint fk_match_id
        foreign key (match_id)
        references matches(match_id)
    
    
);