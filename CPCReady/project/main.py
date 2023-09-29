import argparse
from .functions import *


def main():

    description = 'CPCReady Create a new Project.'

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--project', '-p', help='Project name')
    parser.add_argument('--cpc', '-c', type=int, default=664, choices=[464, 664, 6128], help='CPC Model (464, 664, 6128)')

    args = parser.parse_args()

    if args.project:
        create(args.project,args.cpc)
    else:
        handle_image_mode(args, parser)

def handle_image_mode(args, parser):
    parser.print_help()


if __name__ == '__main__':
    main()
