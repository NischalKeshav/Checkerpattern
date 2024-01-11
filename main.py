import turtle as trtle
import math


########################################Settings########################################
indent=3
length=300
amount=90
color="red"
fill=False
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^Settings^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
# make sure indent*mount<length
painter=trtle.Turtle()
painter.speed(0)
painter.penup()
painter.goto(0,0)
painter.pendown()
painter.color(color,"white")

painter.begin_fill()
def square(length):
  loop_times=0
  painter.color("red")
  while loop_times<4:
    painter.forward(length)
    painter.left(90)
    loop_times=loop_times+1
  loop_times=1
square(length)
painter.begin_fill()
for i in range(amount):
  i=i+ 1
  painter.goto(300,i*indent)#vertical wall at x=300

  painter.goto(300-i * indent,300)  # roof
  painter.goto(0,300-i * indent)  # vertical wall at x=300
  painter.goto(i * indent,0)
  pass
print(painter.ycor())
if fill:
  painter.end_fill()
print(range(0,1))










import turtle as trtle
import math


########################################Settings########################################
indent=3
length=300
amount=90
color="red"
fill=False
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^Settings^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
# make sure indent*mount<length
painter=trtle.Turtle()
painter.speed(0)
painter.penup()
painter.goto(0,0)
painter.pendown()
painter.color(color,"white")

painter.begin_fill()
def square(length):
  loop_times=0
  painter.color("red")
  while loop_times<4:
    painter.forward(length)
    painter.left(90)
    loop_times=loop_times+1
  loop_times=1
square(length)
painter.begin_fill()
for i in range(amount):
  i=i+ 1
  painter.goto(300,i*indent)#vertical wall at x=300

  painter.goto(300-i * indent,300)  # roof
  painter.goto(0,300-i * indent)  # vertical wall at x=300
  painter.goto(i * indent,0)
  pass
print(painter.ycor())
if fill:
  painter.end_fill()
print(range(0,1))











wn=trtle.Screen()

wn=trtle.Screen()
wn.mainloop()