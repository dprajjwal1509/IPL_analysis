import matplotlib.pyplot as plt


def question3_foreign_umpires(list_delivery_match, list_umpire):
    list_foreign_umpire = {}
    number_umpires_country = {}

    """Collect unique umpires from match data"""
    umpire_set = set()
    for matches in list_delivery_match:
        for field in ["umpire1", "umpire2", "umpire3"]:
            if matches[field]:
                umpire_set.add(matches[field])

    """Filter only foreign umpires (non-India)"""
    for umpire_name in umpire_set:
        for umpire in list_umpire:
            if umpire_name == umpire["umpire"]:
                if umpire[" country"].strip().lower() != "india":
                    list_foreign_umpire[umpire_name] = umpire[" country"]

    """Count number of foreign umpires per country"""
    for _, country in list_foreign_umpire.items():
        if country not in number_umpires_country:
            number_umpires_country[country] = 0
        number_umpires_country[country] += 1

    question3_plot(number_umpires_country)


def question3_plot(number_umpires_country):
    """Plot Function"""
    country = list(number_umpires_country.keys())
    frequency = list(number_umpires_country.values())

    plt.figure(figsize=(10, 6))
    plt.bar(country, frequency, color="teal", edgecolor="black")
    plt.title("Foreign umpire analysis")
    plt.xlabel("Country")
    plt.ylabel("Number of Umpires")
    plt.xticks(rotation=45)
    plt.show()
