#import mpmath as mp
#from ursina import *
from PIL import Image
import sys

#app = Ursina()

p = int(input('wprowadź rodzaj kompresji (3 lub 6)'))
# mamy 100 milionów liczby pi, dzielimy na 6 (bo potrzenujemy 6 cyfr na pixel). dostajemy ok 16 milionów, robimy z tego sqrt i mamy ok 4082
size = [5700,5700]
img = Image.new("RGB", (size[0], size[1]))
print(f"tworzenie obrazu {size}")


dps : int = size[0]*size[1]*p
sys.set_int_max_str_digits(dps+1)
print(f'utworzono dps: {dps}')

print('przypisano dps, trwa wczytywanie pi')

with open("pi100.txt", "r", encoding="utf-8") as plik:
    pi = plik.read().strip()

#con = Entity()


for y in range(size[1]):
    for x in range(size[0]):
        i = y*size[0]+x
        num = i * p
        if p == 3:
            red : int = pi[num]
            green : int = pi[num+1]
            blue : int = pi[num+2]
            colorDane = [int(red),int(green),int(blue)]
            colorDane = [round((c / 10) * 255) for c in colorDane]
        else:
            red : int = pi[num]+pi[num+1]
            green : int = pi[num+2]+pi[num+3]
            blue : int = pi[num+4]+pi[num+5]
            colorDane = [int(red),int(green),int(blue)]
            colorDane = [round((c / 99) * 255) for c in colorDane]
        
#        colors = color.rgb32(colorDane[0],colorDane[1],colorDane[2])
        img.putpixel((x, y), (colorDane[0],colorDane[1],colorDane[2]))
        # block = Entity(
        #     model='quad',
        #     color=colors,
        #     x=x,
        #     y=y,
        #     scale=(1,1),
        #     parent=con
        # )

    #ZAKOMENTOWAĆ TO A PROGRAM BĘDZIE DZIAŁAŁ SZYBCIEJ
    print(f"narysowano rząd, y:{y}... zostało: {size[1]-y}... czekaj")



img.save("pi.png")
print('zapisano!')
# con.combine()

# camera.orthographic = True
# camera.fov = 10

# camera_speed = 5
# zoom_speed = 1

# czy wspominałem kiedyś jak bardzo nienawidze pisać kamer nie godotowych?
# def update():
#     global camera_speed

#     # ruch kamery
#     camera.x += (held_keys['d'] - held_keys['a']) * camera_speed * time.dt
#     camera.y += (held_keys['w'] - held_keys['s']) * camera_speed * time.dt

#     # również strzałki
#     camera.x += (held_keys['right arrow'] - held_keys['left arrow']) * camera_speed * time.dt
#     camera.y += (held_keys['up arrow'] - held_keys['down arrow']) * camera_speed * time.dt


# def input(key):
#     # zoom
#     if key == 'scroll up':
#         camera.fov -= zoom_speed

#     if key == 'scroll down':
#         camera.fov += zoom_speed

#     # żeby nie dało się odwrócić zoomu
#     camera.fov = max(1, camera.fov)






# #print(pi)

# app.run()