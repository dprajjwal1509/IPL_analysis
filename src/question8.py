import matplotlib.pyplot as plt

# ---------------------------
# Question 8 : Top 10 Economical bowler in 2015
# ---------------------------


def question8_top_economical_bowlers(list_delivery_match):
    number_legal_overs = {}
    for item in list_delivery_match:
        if item["season"] == "2015":
            bowler = item["bowler"]
            wide_runs = item["wide_runs"]
            noball_runs = item["noball_runs"]

            if bowler not in number_legal_overs:
                number_legal_overs[bowler] = 0

            if wide_runs == "0" and noball_runs == "0":
                number_legal_overs[bowler] += 1

    """Removing bowlers who bowled less than 10 overs"""
    for bowler in list(number_legal_overs.keys()):
        overs = number_legal_overs[bowler] // 6
        number_legal_overs[bowler] = overs
        if overs < 10:
            number_legal_overs.pop(bowler)

    """Step 2 : Runs Conceded"""
    number_runs_conceded = {}
    for item in list_delivery_match:
        if item["season"] == "2015":
            bowler = item["bowler"]
            if bowler in number_legal_overs:  # Only consider bowlers with >=10 overs
                runs = (
                    int(item["wide_runs"])
                    + int(item["batsman_runs"])
                    + int(item["noball_runs"])
                    + int(item["penalty_runs"])
                )
                if bowler not in number_runs_conceded:
                    number_runs_conceded[bowler] = 0
                number_runs_conceded[bowler] += runs

    """Step 3 : Find Economy"""
    economy_bowler = {}
    for bowler, overs in number_legal_overs.items():
        runs = number_runs_conceded[bowler]
        economy_bowler[bowler] = runs / overs
    economy_bowler = dict(sorted(economy_bowler.items(), key=lambda x: x[1])[:10])

    """Calling plot function"""
    question8_plot(economy_bowler)


def question8_plot(economy_bowler):
    """Plot function"""
    bowler = list(economy_bowler.keys())
    economy = list(economy_bowler.values())
    plt.figure(figsize=(10, 6))
    plt.bar(bowler, economy)
    plt.title("Top 10 Economical bowler in 2015")
    plt.xlabel("Bowler")
    plt.ylabel("Economy")
    plt.xticks(rotation=45)
    plt.show()
