import argparse
from CPCReady import func_screen as screen

def main():
    description = 'CPCReady Create SCR image.'

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--image', '-i', help='Image Path')
    parser.add_argument('--mode', '-m', type=int, default=0, choices=[0, 1, 2], help='Image Mode (0, 1, 2)')
    parser.add_argument('--out', '-o', help='Folder Path out')
    parser.add_argument('--dsk', '-d', action='store_true', help='Convert image in dsk', default=False)

    args = parser.parse_args()

    if args.image and args.out:
        screen.create(args.image, args.mode, args.out, args.dsk)
    else:
        handle_image_mode(args, parser)


def handle_image_mode(args, parser):
    parser.print_help()


if __name__ == '__main__':
    main()
