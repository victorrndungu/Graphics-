""" This Course-Work Activity is to dra a model of a house
using py cairo with the knowledge that we have gained
 from previous topics
 GROUP MEMBERS
 151097 Barasa Conslata
 151344 Mbindyo Ryan
 150668 Kahindo Victor
 150651 Maximilian Mwenda
 150851Melissa Ndeti
 """
from os import close

import cairo
import math

OUTPUT_DIR = "../../output_directory/"

surface = cairo.ImageSurface(cairo.FORMAT_RGB24,800, 600)
ctx = cairo.Context(surface)
ctx.set_source_rgb(1, 1, 1)
line = ctx.line_to
color = ctx.set_source_rgba
rectangle = ctx.rectangle
ctx.paint()

#drawing the frame by connecting the lines
rectangle(160, 405, 600,25) #The bottom rectangle
color(0,0,0)
rectangle(425,225,320,180) #First Rectangle to the left
ctx.move_to(170,405)
line(170,205)#right line completing the house

ctx.move_to(105,245) #Control point for the first line of the roof
line(298 ,75 ) #The outer tip of the roof to the center
line(475,245) #outer left part of the roof
line(450, 270)
line(298, 120) #Inner tip of the roof
line(120, 275)#inner right roof
ctx.close_path()

ctx.move_to(350, 125)
line

ctx.set_line_width(4)
ctx.stroke()



# Save the result to a PNG file
surface.write_to_png(f'{OUTPUT_DIR}house1.png')