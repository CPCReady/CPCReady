import argparse
from functions import create


def main():
    description = 'CPCReady Create Project.'

    parser = argparse.ArgumentParser(description=description)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--project', '-p', help='Project name')
    group.add_argument('--cpc', '-c', type=int, choices=[464, 664, 6128], help='CPC Model (464, 664, 6128)')

    args = parser.parse_args()

    if args.project:
        create(args.project, args.model)
    else:
        handle_image_mode(args, parser)


def handle_image_mode(args, parser):
    parser.print_help()


if __name__ == '__main__':
    main()
