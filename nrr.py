def calculate_nrr(runs_scored,
                  overs_faced,
                  runs_conceded,
                  overs_bowled):

    run_rate_for = runs_scored / overs_faced

    run_rate_against = runs_conceded / overs_bowled

    return round(run_rate_for - run_rate_against, 3)


def required_runs_to_beat_nrr(
        current_nrr,
        target_nrr,
        overs=20):

    diff = target_nrr - current_nrr

    return int(diff * overs + 1)
