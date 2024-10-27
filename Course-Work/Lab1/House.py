""" This Course-Work Activity is to dra a model of a house
using py cairo with the knowledge that we have gained
 from previous topics
 GROUP MEMBERS
 151097 Barasa Conslata
 151344 Mbindyo Ryan
 Kahindo Victor
 Maximilian Mwenda
 Melissa Ndeti
 """
import cairo
import math

OUTPUT_DIR = "../../Test Labs/output_directory/"

surface = cairo.ImageSurface(cairo.FORMAT_RGB24,800, 600)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 1, 1)
line = ctx.line_to
color = ctx.set_source_rgba
ctx.paint()

#drawing the frame by connecting the lines
ctx.move_to(250, 550)
line(650, 550) #A
line(650, 285) #B
line(700,285) #C
line(700,205) #D
line(200,205) #E
line(200,285) #F
line(250,285) #G

ctx.close_path() #H

#Drawing the arc from with the center of the frame as the radius
ctx.move_to(250,205)
ctx.arc(450, 205,150,math.pi,0)

#addig the colour of  the frame/ structure of the house
color(0.23,0.53,0.85)

ctx.stroke()

#The door
ctx.rectangle(395,335,110,215)
color(0.45,0.8,0.43)
ctx.stroke()

#the dor knob
ctx.arc(493,442.5,7,0,2*math.pi)
color(0.23,0.53,0.85)
ctx.fill_preserve()
color(0,0.,1)
ctx.set_line_width(2)
ctx.stroke()

#The left window
ctx.rectangle(275, 335, 85,85)
color(0.45,0.8,0.43)
ctx.stroke()

ctx.move_to(317.5, 335)
line(317.5, 420) #divider from top to bottom

ctx.move_to(275,377.5)
line(360,377.5 )# divider from left to right
color(0.23,0.53,0.85)
ctx.stroke()

# The right window
ctx.rectangle(540, 335, 85,85)
color(0.45,0.8,0.43)
ctx.stroke()

ctx.move_to(582.5,335)
line(582.5,420)#the divider top to bottom

ctx.move_to(540, 377.5)
line(625, 377.5)# left to right divider
color(0.23,0.53,0.85)
ctx.stroke()

#Bezier curve and acrc for the moon
ctx.arc(700, 100, 80, 0, 2 * math.pi)
"""ctx.move_to(300, 0)
ctx.curve_to(700,205)"""

color(0.23,0.53,0.85)
ctx.stroke()



# Save the result to a PNG file
surface.write_to_png(f'{OUTPUT_DIR}house.png')