import matplotlib.pyplot as plt


def question2_top_batsman_rcb(list_delivery_match):
    rcb_batsman_score = {}

    for item in list_delivery_match:
        if item["batting_team"] == "Royal Challengers Bangalore":
            batsman = item["batsman"]
            runs = int(item["batsman_runs"])

            if batsman not in rcb_batsman_score:
                rcb_batsman_score[batsman] = 0
            rcb_batsman_score[batsman] += runs

    """Top 10 batsmen"""
    rcb_batsman_score = dict(
        sorted(rcb_batsman_score.items(), key=lambda x: x[1], reverse=True)[:10]
    )

    question2_plot(rcb_batsman_score)


#
def question2_plot(rcb_batsman_score):
    """Plot Function"""
    rcb_batsman = list(rcb_batsman_score.keys())
    rcb_runs = list(rcb_batsman_score.values())

    plt.figure(figsize=(10, 6))
    plt.bar(rcb_batsman, rcb_runs)
    plt.title("Top batsman for Royal Challengers Bangalore (Top 10)")
    plt.xlabel("Batsman")
    plt.ylabel("Runs")
    plt.xticks(rotation=45, ha="right")
    plt.show()
