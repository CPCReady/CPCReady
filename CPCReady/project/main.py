import argparse
from .functions import *


def main():
    description = 'CPCReady Create a new Project.'

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--project', '-p', help='Project name')
    parser.add_argument('--cpc', '-c', type=int, default=6128, choices=[464, 664, 6128],
                        help='CPC Model (464, 664, 6128)')
    parser.add_argument('--testing', '-t', type=str, default="web", choices=["web", "desktop"],
                        help='Retrovirtual Machine Testing (Web, Desktop)')

    args = parser.parse_args()

    if args.project:
        create(args.project, args.cpc, args.testing)
    else:
        handle_image_mode(args, parser)


def handle_image_mode(args, parser):
    parser.print_help()


if __name__ == '__main__':
    main()
