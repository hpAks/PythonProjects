import random

import colorgram
import turtle as t

imgs = ["image.jpg", "image3.jpg"]
choice = random.choice(imgs)
print(f"selected image:{choice}")
colors = colorgram.extract(choice, 1000)
color_list = []

for i in range(1,len(colors)):
    r = colors[i].rgb.r
    g = colors[i].rgb.g
    b = colors[i].rgb.b
    new_color = (r,g,b)
    color_list.append(new_color)

screen = t.Screen()
screen.colormode(255)
my_tuple = tuple()
tim = t.Turtle()
tim.shape("circle")
tim.speed("fastest")
tim.hideturtle()
index=0

for y in range(0,5):
    for x in range(0,5):
        tim.penup()
        tim.goto(x*50,y*50)
        my_tuple = color_list[index]
        tim.dot(10,my_tuple)
        index += 1
        tim.pendown()

tim.penup()
tim.goto(350,350)


screen.exitonclick()




# rgb_color =[]
# colors = colorgram.extract("image.jpg", 1500)
# for color in colors:
#     new_color = (color.rgb.r, color.rgb.g, color.rgb.b)
#     rgb_color.append(new_color)
#
# print(rgb_color)