from gfxhat import lcd,  fonts
from PIL import Image, ImageFont, ImageDraw
from sys

def wrapArround(x, y):
    x = 0
    y = 0
    while True:
        if x > 127:
            return x = 0
        if x < 0:
            return x = 127
        if y > 63:
            return y = 0
        if y < 0:
            return y = 63

def get():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='s':
            lcd.clear()
        if k=='q':
            sys.exit()
        if k=='\x1b[A':
                print "up"
        elif k=='\x1b[B':
                print "down"
        elif k=='\x1b[C':
                print "right"
        elif k=='\x1b[D':
                print "left"

def main():
        for i in range(0,20):
                get()

if __name__=='__main__':
        main()
        
def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayText(text,lcd,x,y):
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.AmaticSCBold, 24)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show() 