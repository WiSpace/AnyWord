import argparse

parser = argparse.ArgumentParser(
    prog="AnyWord",
    description = "programming language with artificial intelligence - anyword"
)
parser.add_argument('path')
parser.add_argument('-l', '--libfile')
parser.add_argument('-d', '--debug', action='store_true')

args = parser.parse_args()
