import csv
import matplotlib.pyplot as plt
import question1_total_runs as q1
import question2 as q2
import question3 as q3
import question4 as q4
import question5 as q5
import question6 as q6
import question7 as q7
import question8 as q8


def testrunner():
    """Load datasets"""
    list_match = []
    with open("data/matches.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            list_match.append(row)

    list_delivery = []
    with open("data/deliveries.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            list_delivery.append(row)

    """Read umpire data from CSV"""
    list_umpire = []
    with open("data/umpires.csv") as umpire_file:
        umpire_dict = csv.DictReader(umpire_file)
        for row in umpire_dict:
            list_umpire.append(row)

    """Merge deliveries + matches (if needed)"""
    list_delivery_match = []
    for delivery in list_delivery:
        for matches in list_match:
            if delivery["match_id"] == matches["id"]:
                merged_item = {**delivery, **matches}
                list_delivery_match.append(merged_item)

    q1.question1_total_runs(list_delivery_match)
    q2.question2_top_batsman_rcb(list_delivery_match)
    q3.question3_foreign_umpires(list_delivery_match, list_umpire)
    q4.question4_matches_played(list_delivery_match)
    q5.question5_number_matches_year(list_match)
    q6.question6_matches_won(list_match)
    q7.question7_extra_runs_2016(list_delivery_match)
    q8.question8_top_economical_bowlers(list_delivery_match)
