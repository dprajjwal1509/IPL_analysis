import matplotlib.pyplot as plt


def question1_total_runs(list_delivery_match):
    total_runs_each_team = {}

    for runs in list_delivery_match:
        total_runs = int(runs["total_runs"])
        batting_team = runs["batting_team"]

        if batting_team not in total_runs_each_team:
            total_runs_each_team[batting_team] = 0

        total_runs_each_team[batting_team] += total_runs

    """Calling Plot function"""
    question1_plot(total_runs_each_team)


def question1_plot(total_runs_each_team):
    """Plot function"""
    teams = list(total_runs_each_team.keys())
    runs = list(total_runs_each_team.values())

    plt.figure(figsize=(10, 6))
    plt.bar(teams, runs)
    plt.xticks(rotation=30, ha="right")
    plt.title("Total Runs Scored by Each Team")
    plt.xlabel("Team")
    plt.ylabel("Runs")
    plt.show()
