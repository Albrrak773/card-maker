import sys
from PIL import Image, ImageDraw, ImageFont

DEFAULT_STYLE = 1

def main(args: str):

    Name = args[0].title()

    if (args[1] == 1):
        background = "./assets/invite card 1.png"
    if (args[1] == 2):
        background = "./assets/invite card 2.png"

    # if not english assume Arabic.
    if (isEnglish(Name)):
        font = ImageFont.truetype('./assets/Ubuntu/Ubuntu-Regular.ttf', size=scale_font_size(Name))
        language = 'en'
    else:
        font = ImageFont.truetype('./assets/Rubik/static/Rubik-Regular.ttf', size=scale_font_size(Name))
        language = 'ar'

    with Image.open(background) as im:
        d = ImageDraw.Draw(im)
        x, y = im.size
        d.text((x/2, (y * 0.7)), Name, anchor="mm", font=font, language=language)
        im.show()


def validate_args(args: list[str]):
    """
    checks if at least 1 argument was passed. 
    any more arguments are ignored
    """
    # if missing arguments print help message
    if (len(args) <= 1):
        with open("./help.txt") as help_menu:
            for line in help_menu.readlines():
                print(line, end="")
        sys.exit(0)
    if (len(args) <= 2):
        args.append(DEFAULT_STYLE)
    if (len(args) >= 3):
        args[2] = int(args[2])
    return args[1:]

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
    

Name = validate_args(sys.argv)
main(Name)