import matplotlib.pyplot as plt


def question6_matches_won(list_match):
    matches_team_year = {}
    team_set = set()

    for item in list_match:
        year = item["season"]
        winner = item["winner"]

        if year not in matches_team_year:
            matches_team_year[year] = {}

        if winner not in matches_team_year[year]:
            matches_team_year[year][winner] = 0

        matches_team_year[year][winner] += 1
        team_set.add(winner)

    question6_plot(team_set, matches_team_year)


def question6_plot(team_set, matches_team_year):
    """Plot Function"""
    teams = sorted(list(team_set))
    years = sorted(list(matches_team_year.keys()))

    """Plot stacked bar"""
    bottom = [0] * len(years)
    for team in teams:
        values = [matches_team_year[year].get(team, 0) for year in years]
        plt.bar(years, values, bottom=bottom, label=team)
        bottom = [bottom[i] + values[i] for i in range(len(values))]

    plt.xticks(rotation=30)
    plt.title("Matches Won per Team per Season")
    plt.xlabel("Season")
    plt.ylabel("Wins")
    plt.legend(fontsize=7)
    plt.show()
