from PIL import Image, ImageFont, ImageDraw  
import io

# BIGGIE FONTS, CODE STYLED LIKE MY PYGAME GAME LMAO
class Fonts:
    futura_large = ImageFont.truetype(r'/app/modules/Futura Condensed.ttf', 50)
    futura_medium = ImageFont.truetype(r'/app/modules/Futura Condensed.ttf', 40)

# LIMITS THE CHARACTER
def limitify(raw, linelimit, maxlimit):
    text = ''
    for i in range(0, len(raw)):
        if len(text.split('\n'))>maxlimit:
            text = text[:-1]
            break
        if i>2:
            if i%linelimit==0:
                text += '\n'
        text += list(raw)[i]
    return text

# COMPILES ALL OF THAT TO THE DISCORD.FILE THINGY
#273
def compile(data):
    arr = io.BytesIO()
    data.save(arr, format='PNG')
    arr.seek(0)
    return arr

def simpleTopMeme(text, src, linelimit, maxlimit):
    image = Image.open(r'{}'.format(src))
    draw = ImageDraw.Draw(image)
    text = limitify(text, linelimit, maxlimit)
    draw.text((5, 5), text, fill ="black", font = Fonts.futura_large, align ="left") 
    data = compile(image)
    return data

def presentationMeme(text):
    link = "../assets/pics/presentation.jpg"
    image = Image.open(r'{}'.format(link))
    text = limitify(text, 31, 5)
    draw = ImageDraw.Draw(image)
    draw.text((130, 55), text, fill ="black", font = Fonts.futura_medium, align ="left")  
    data = compile(image)
    return data