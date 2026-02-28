import argparse
from analytics import load_table, print_table
from simulator import simulate_t20
from nrr import calculate_nrr


parser = argparse.ArgumentParser()

parser.add_argument("--table",
                    help="Load points table CSV")

parser.add_argument("--simulate",
                    action="store_true")

parser.add_argument("--nrr",
                    nargs=4,
                    type=float)

args = parser.parse_args()


if args.table:

    df = load_table(args.table)

    print_table(df)


if args.simulate:

    match = simulate_t20()

    print(match)


if args.nrr:

    r1,o1,r2,o2 = args.nrr

    print(
        calculate_nrr(
            r1,
            o1,
            r2,
            o2
        )
    )
