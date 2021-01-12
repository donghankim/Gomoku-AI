import argparse

def get_args():
    argp = argparse.ArgumentParser(description='Gomoku AI game', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # argp.add_argument('--player', )

    return argp.parse_args()
