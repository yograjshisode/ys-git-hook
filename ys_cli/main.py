import json
import argparse
from ys_cli.subcommands.hello_world.hello_world import HelloWorld


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--hello_world', help="Hello World")
    parser.add_argument("filenames", nargs="*")

    args = parser.parse_args()

    hello_world = args.hello_world
    if hello_world:
        hello_world_obj = HelloWorld(hello_world)
        hello_world_obj.say_hi()
