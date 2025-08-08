from sys import exit, argv, stdout
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import os.path as op

DEFAULT_STYLE = 1
BASE_PATH = Path(".")
LOG_FILE = "history.log"

def main(args: list[str]):

    with open(Path.joinpath(BASE_PATH, LOG_FILE), "a") as f:
        f.write(f"Got called with args {args[0]}, {args[1]}\n")
    Name = args[0].title()

    if (args[1] == 1):
        background = Path.joinpath(BASE_PATH, "assets", "invite card 1.png")
    if (args[1] == 2):
        background = Path.joinpath(BASE_PATH, "assets", "invite card 2.png")

    # if not english assume Arabic.
    if (isEnglish(Name)):
        font = ImageFont.truetype(Path.joinpath(BASE_PATH, "assets", "Ubuntu", "Ubuntu-Regular.ttf"), size=scale_font_size(Name))
        language = 'en'
    else:
        font = ImageFont.truetype(Path.joinpath(BASE_PATH, "assets", "Rubik", "static","Rubik-Regular.ttf"), size=scale_font_size(Name))
        language = 'ar'

    with Image.open(background) as im:
        d = ImageDraw.Draw(im)
        x, y = im.size
        d.text((x/2, (y * 0.7)), Name, anchor="mm", font=font, language=language)
        if (args[2]):
            im.save(stdout.buffer, format="png")
        else:
            im.save(Path.joinpath(BASE_PATH, "..", "output.png"), format="png")


def validate_args(args: list[str]):
    """
    checks if at least 1 argument was passed. 
    any more arguments are ignored
    returns: [name, style, is_stdout]
    """
    length = 3
    new_args = list([None for x in range(length)]) # new list with None * length
    #  if missing arguments print help message
    if (len(args) <= 1):
        with open(Path.joinpath(BASE_PATH, "help.txt"), "r") as help_menu:
            for line in help_menu.readlines():
                print(line, end="")
        exit(0)
    else:
        new_args[0] = args[1]
    if ("--style" in args):
        i = args.index("--style") + 1
        new_args[1] = int(args[i])
    else:
        new_args[1] = DEFAULT_STYLE
    if ("--stdout" in args):
        new_args[2] = True
    else:
        new_args[2] = False
    return new_args

def scale_font_size(Name: str = "Your Name"):
    """
    scales the font size Down as the Name's length gets longer

    the scale factor is based on an arbitariy choices I made for 'what looks good (not a UI guy so take that with a grain of salt)'

    """
    BASE_CHAR_LENGTH = 16
    BASE_FONT_SIZE  = 100
    if (len(Name) < BASE_CHAR_LENGTH):
        return BASE_FONT_SIZE
    else:
        return (BASE_FONT_SIZE * (BASE_CHAR_LENGTH / ((len(Name)) * 0.7)) )

def isEnglish(Name):
    """
    a (very very) basic function to determine if a name is in english or not

    the function simply looks at the first character and checks if its unicode code point 
    is within the ASCII characters e.g < 127
    """
    if (ord(Name[0]) < 127):
        return True
    else:
        return False

if __name__ == "__main__":
    Name = validate_args(argv)
    main(Name)