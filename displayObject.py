from gfxhat import lcd

def displayObject(obj, x, y):
    a = 0
    while a <=len(obj) - 1:
        w = 0
        while w <= len(obj[a]) - 1:
            if obj[a][b] == 1:
                lcd.set-pixel(x, y, 1)
                lcd.show()
                b += 1
                x += 1
            else:
                b += 1
                x += 1
                continue
        x = x - len(obj[a])
        y += 1
        a += 1
                
    