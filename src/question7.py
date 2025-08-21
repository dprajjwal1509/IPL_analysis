import matplotlib.pyplot as plt


def question7_extra_runs_2016(list_delivery_match):

    extra_runs_2016 = {}

    for item in list_delivery_match:
        if item["season"] == "2016":  # filter 2016

            bowling_team = item["bowling_team"]
            extra_runs = int(item["extra_runs"])

            if bowling_team not in extra_runs_2016:
                extra_runs_2016[bowling_team] = 0

            extra_runs_2016[bowling_team] += extra_runs

    question7_plot(extra_runs_2016)


def question7_plot(extra_runs_2016):
    """Plot Function"""
    team_2016 = list(extra_runs_2016.keys())
    runs_2016 = list(extra_runs_2016.values())

    plt.figure(figsize=(11, 7))
    plt.bar(team_2016, runs_2016, color="coral", edgecolor="black")
    plt.title("Extra runs conceded per team in the year 2016")
    plt.xlabel("Teams")
    plt.ylabel("Extra Runs")
    plt.xticks(rotation=45, ha="right")
    plt.show()
