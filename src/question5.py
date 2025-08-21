import matplotlib.pyplot as plt


def question5_number_matches_year(list_match):
    matches_year = {}
    for item in list_match:
        year = item["season"]
        if year not in matches_year:
            matches_year[year] = 0
        matches_year[year] += 1

    question5_plot(matches_year)


def question5_plot(matches_year):
    year = list(matches_year.keys())
    frequency = list(matches_year.values())

    """Plot"""
    plt.figure(figsize=(10, 6))
    plt.bar(year, frequency, color="skyblue", edgecolor="black")
    plt.title("Number of matches played per year in IPL")
    plt.xlabel("Season")
    plt.ylabel("Number of Matches")
    plt.xticks(rotation=45)
    plt.show()
