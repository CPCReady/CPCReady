import argparse
from CPCReady import func_palette as palette
from CPCReady import __version__

def main():
    description = 'CPCReady Get palette image.'

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--image', '-i', help='Image Path')
    parser.add_argument('--mode', '-m', type=int, default=0, choices=[0, 1, 2], help='Image Mode (0, 1, 2)')
    parser.add_argument('-v', '--version', action='version', version='\nCPCReady - Palette ' + __version__)

    args = parser.parse_args()
    
    if args.image and args.mode:
        palette.getData(args.image, args.mode)
    else:
        handle_image_mode(args, parser)


def handle_image_mode(args, parser):
    parser.print_help()


if __name__ == '__main__':
    main()
