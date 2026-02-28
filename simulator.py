import random


def simulate_t20():

    teamA = random.randint(120,220)

    teamB = random.randint(120,220)

    if teamA > teamB:
        winner = "Team A"

    else:
        winner = "Team B"

    return {

        "TeamA": teamA,
        "TeamB": teamB,
        "Winner": winner
    }
