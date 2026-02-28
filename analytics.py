import pandas as pd
from tabulate import tabulate
from nrr import calculate_nrr


def load_table(path):

    df = pd.read_csv(path)

    df["NRR"] = df.apply(
        lambda x:
        calculate_nrr(
            x.runs_scored,
            x.overs_faced,
            x.runs_conceded,
            x.overs_bowled),
        axis=1
    )

    df["Points"] = df.wins * 2

    return df.sort_values("Points",
                          ascending=False)


def print_table(df):

    print(
        tabulate(
            df,
            headers="keys",
            tablefmt="psql"
        )
    )
