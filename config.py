import argparse

def get_args():
    argp = argparse.ArgumentParser(description='Gomoku AI game', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    argp.add_argument('--rows', type = int, default = 19)
    argp.add_argument('--cols', type = int, default = 19)

    return argp.parse_args()
