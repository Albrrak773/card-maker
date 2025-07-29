import sys
from PIL import Image, ImageDraw, ImageFont


def main(Name: str):
    language = 'en'
    Name = Name.title()

    with Image.open("./assets/invite card 1.png") as im:
        if (isEnglish(Name)):
            font = ImageFont.truetype('./assets/Ubuntu/Ubuntu-Regular.ttf', size=scale_font_size(Name))
        # if not english assume Arabic.
        else:
            
            font = ImageFont.truetype('./assets/Rubik/static/Rubik-Regular.ttf', size=scale_font_size(Name))
        d = ImageDraw.Draw(im)
        x, y = im.size
        d.text((x/2, (y * 0.7)), Name, anchor="mm", font=font, language=language)

        im.show()


def validate_args(args: list[str]):
    """
    checks if at least 1 argument was passed. 
    any more arguments are ignored
    """
    if (not len(args) > 1):
        raise Exception("Missing Required argument/s") 
    else:
        return args[1]

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