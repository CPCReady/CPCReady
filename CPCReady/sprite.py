import argparse
from CPCReady import func_sprite as sprites
from CPCReady import __version__

def main():
    description = 'CPCReady Create sprite.'

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--image', '-i', help='Image Path')
    parser.add_argument('--mode', '-m', type=int, default=0, choices=[0, 1, 2], help='Image Mode (0, 1, 2)')
    parser.add_argument('--out', '-o', help='Folder Path out')
    parser.add_argument('--height', '-e', type=int, help='Height sprite size')
    parser.add_argument('--width', '-w', type=int, help='Width sprite size')
    parser.add_argument('-v', '--version', action='version', version='\nCPCReady - Sprite ' + __version__)
    
    args = parser.parse_args()

    if args.image != "" and args.mode != "" and args.out != "" and args.height != "" and args.width != "":
        sprites.create(args.image, args.mode, args.out, args.height, args.width)
    else:
        handle_image_mode(args, parser)


def handle_image_mode(args, parser):
    parser.print_help()


if __name__ == '__main__':
    main()
