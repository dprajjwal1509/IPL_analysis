import matplotlib.pyplot as plt


def question4_matches_played(list_delivery_match):
    list_total_match_team_season = {}

    """
    Count matches played by each team per season
    """
    for item in list_delivery_match:
        season = item["season"]
        team1 = item["team1"]
        team2 = item["team2"]

        if season not in list_total_match_team_season:
            list_total_match_team_season[season] = {}

        if team1 not in list_total_match_team_season[season]:
            list_total_match_team_season[season][team1] = 0
        list_total_match_team_season[season][team1] += 1

        if team2 not in list_total_match_team_season[season]:
            list_total_match_team_season[season][team2] = 0
        list_total_match_team_season[season][team2] += 1

    """
    Plotting using stacked bar graph
    """
    seasons = list(list_total_match_team_season.keys())
    bottom = [0] * len(seasons)

    """
    Collect unique teams
    """
    team_set = set()
    for season, teams in list_total_match_team_season.items():
        for t in teams.keys():
            if t.strip():
                team_set.add(t)
    teams = list(team_set)

    """
    Pass bottom here 👇
    """
    question4_plot(teams, list_total_match_team_season, seasons, bottom)


def question4_plot(teams, list_total_match_team_season, seasons, bottom):
    plt.figure(figsize=(12, 6))

    for t in teams:
        matches = [list_total_match_team_season[s].get(t, 0) for s in seasons]
        plt.bar(seasons, matches, bottom=bottom, label=t)
        bottom = [bottom[i] + matches[i] for i in range(len(seasons))]

    plt.title("Matches Played by Team per Season (IPL)")
    plt.xlabel("Season")
    plt.ylabel("Matches Played")
    plt.xticks(rotation=45)
    plt.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    plt.show()
